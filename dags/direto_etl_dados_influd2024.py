from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import pandas as pd
import requests
import psycopg2
from sqlalchemy import create_engine


# Função para baixar o arquivo CSV
def extrair_dados():
    url = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2024/INFLUD24-20-01-2025.csv"
    diretorio_data = "/opt/airflow/data"

    if not os.path.exists(diretorio_data):
        os.makedirs(diretorio_data)

    caminho_arquivo = os.path.join(diretorio_data, "INFLUD24-20-01-2025.csv")

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(caminho_arquivo, "wb") as file:
            file.write(response.content)
        print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")
        raise


# Função para transformar e salvar os dados
def transformar_salvar_dados():
    caminho_csv = "/opt/airflow/data/INFLUD24-20-01-2025.csv"
    dados = pd.read_csv(caminho_csv, delimiter=';')

    colunas_selecionadas = [
        "SG_UF_NOT", "ID_MUNICIP", "CO_MUN_NOT", "ESTRANG", "CS_SEXO",
        "DT_NASC", "NU_IDADE_N", "CS_GESTANT", "CS_RACA", "FATOR_RISC",
        "VACINA_COV", "CLASSI_FIN", "EVOLUCAO"
    ]

    dados_selecionados = dados[colunas_selecionadas]
    dados_pe_ou_26 = dados_selecionados[
        dados_selecionados["SG_UF_NOT"].isin(["PE", "26"])
    ]

    dados_limpos = dados_pe_ou_26.dropna()

    def converter_para_inteiro(coluna):
        return pd.to_numeric(coluna, errors='coerce', downcast='integer')

    colunas_a_converter = ["ESTRANG", "VACINA_COV", "CLASSI_FIN", "EVOLUCAO"]
    for coluna in colunas_a_converter:
        dados_limpos[coluna] = converter_para_inteiro(dados_limpos[coluna])

    dados_limpos = dados_limpos.dropna(subset=colunas_a_converter)

    dados_exibicao = dados_limpos.head(5)
    print(dados_exibicao)

    caminho_saida = "/opt/airflow/data/transformado_INFLUD24-20-01-2025.csv"
    dados_limpos.to_csv(caminho_saida, index=False, sep=';')
    print(f"Arquivo CSV gerado: {caminho_saida}")

    return caminho_saida


# Função para carregar os dados no PostgreSQL
def carregar_no_postgres(caminho_arquivo):
    # Configurações do banco de dados PostgreSQL
    usuario = 'ngisecoge'
    senha = 'ngisecoge'
    dbname = 'ngisecoge'
    host = '127.0.0.1'
    porta = '5432'

    # Criação da URL de conexão
    url_conexao = f"postgresql://{usuario}:{senha}@{host}:{porta}/{dbname}"

    # Criando o engine de conexão com o PostgreSQL
    engine = create_engine(url_conexao)

    # Carregar os dados no PostgreSQL
    dados = pd.read_csv(caminho_arquivo, delimiter=';')

    # Especificar o nome da tabela no banco de dados
    tabela_nome = "dados_influd24"

    # Carregar os dados no banco de dados PostgreSQL
    dados.to_sql(tabela_nome, con=engine, if_exists='replace', index=False)
    print(f"Dados carregados com sucesso na tabela {tabela_nome}")


# Argumentos padrão da DAG
definir_dag_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


# Definir a DAG
with DAG(
    "processar_dados_influd",
    default_args=definir_dag_args,
    description="DAG para baixar, transformar e carregar dados do INFLUD",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # Tarefa de extração
    tarefa_extracao = PythonOperator(
        task_id="executar_extracao",
        python_callable=extrair_dados,
    )

    # Tarefa de transformação
    tarefa_transformacao = PythonOperator(
        task_id="executar_transformacao",
        python_callable=transformar_salvar_dados,
    )

    # Tarefa de carregamento no PostgreSQL
    tarefa_carregamento = PythonOperator(
        task_id="carregar_no_postgres",
        python_callable=carregar_no_postgres,
        op_args=["/opt/airflow/data/transformado_INFLUD24-20-01-2025.csv"],
    )

    # Definir a ordem das tarefas
    tarefa_extracao >> tarefa_transformacao >> tarefa_carregamento
