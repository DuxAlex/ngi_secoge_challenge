from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import pandas as pd
import requests
from sqlalchemy import create_engine

# Configurações gerais
definir_dag_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

URL_CSV = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2024/INFLUD24-20-01-2025.csv"
DIRETORIO_DATA = "/opt/airflow/data"
CAMINHO_ARQUIVO = os.path.join(DIRETORIO_DATA, "INFLUD24-20-01-2025.csv")
CAMINHO_ARQUIVO_TRANSFORMADO = os.path.join(DIRETORIO_DATA, "transformado_INFLUD24-20-01-2025.csv")

# Configurações do banco de dados PostgreSQL
POSTGRES_CONFIG = {
    "usuario": "ngisecoge",
    "senha": "ngisecoge",
    "dbname": "ngisecoge",
    "host": "postgres",
    "porta": "5432",
}

# Função para baixar o arquivo CSV
def extrair_dados():
    if not os.path.exists(DIRETORIO_DATA):
        os.makedirs(DIRETORIO_DATA)

    try:
        response = requests.get(URL_CSV)
        response.raise_for_status()
        with open(CAMINHO_ARQUIVO, "wb") as file:
            file.write(response.content)
        print(f"Arquivo salvo com sucesso em: {CAMINHO_ARQUIVO}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")
        raise

# Função para transformar e salvar os dados
def transformar_salvar_dados():
    try:
        dados = pd.read_csv(CAMINHO_ARQUIVO, delimiter=';')
        
        colunas_selecionadas = [
            "SG_UF_NOT", "ID_MUNICIP", "CO_MUN_NOT", "ESTRANG", "CS_SEXO",
            "DT_NASC", "NU_IDADE_N", "CS_GESTANT", "CS_RACA", "FATOR_RISC",
            "VACINA_COV", "CLASSI_FIN", "EVOLUCAO"
        ]
        
        dados_selecionados = dados[colunas_selecionadas]
        dados_filtrados = dados_selecionados[dados_selecionados["SG_UF_NOT"].isin(["PE", "26"])]
        dados_limpos = dados_filtrados.dropna()

        colunas_a_converter = ["ESTRANG", "VACINA_COV", "CLASSI_FIN", "EVOLUCAO"]
        for coluna in colunas_a_converter:
            dados_limpos[coluna] = pd.to_numeric(dados_limpos[coluna], errors='coerce', downcast='integer')
        
        dados_limpos = dados_limpos.dropna(subset=colunas_a_converter)
        dados_limpos.to_csv(CAMINHO_ARQUIVO_TRANSFORMADO, index=False, sep=';')
        print(f"Arquivo transformado salvo em: {CAMINHO_ARQUIVO_TRANSFORMADO}")
    except Exception as e:
        print(f"Erro ao transformar os dados: {e}")
        raise

# Função para carregar os dados no PostgreSQL
def carregar_no_postgres():
    url_conexao = (
        f"postgresql://{POSTGRES_CONFIG['usuario']}:{POSTGRES_CONFIG['senha']}"
        f"@{POSTGRES_CONFIG['host']}:{POSTGRES_CONFIG['porta']}/{POSTGRES_CONFIG['dbname']}"
    )

    try:
        engine = create_engine(url_conexao)
        dados = pd.read_csv(CAMINHO_ARQUIVO_TRANSFORMADO, delimiter=';')
        tabela_nome = "dados_influd24"
        dados.to_sql(tabela_nome, con=engine, if_exists='replace', index=False)
        print(f"Dados carregados com sucesso na tabela {tabela_nome}")
    except Exception as e:
        print(f"Erro ao carregar os dados no PostgreSQL: {e}")
        raise

# Definir a DAG
with DAG(
    "processar_dados_influd",
    default_args=definir_dag_args,
    description="DAG para baixar, transformar e carregar dados do INFLUD",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    tarefa_extracao = PythonOperator(
        task_id="executar_extracao",
        python_callable=extrair_dados,
    )

    tarefa_transformacao = PythonOperator(
        task_id="executar_transformacao",
        python_callable=transformar_salvar_dados,
    )

    tarefa_carregamento = PythonOperator(
        task_id="carregar_no_postgres",
        python_callable=carregar_no_postgres,
    )

    tarefa_extracao >> tarefa_transformacao >> tarefa_carregamento
