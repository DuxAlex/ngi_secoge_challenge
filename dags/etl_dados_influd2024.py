from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# Caminhos dos scripts externos
caminho_extracao = "../scripts/extracao.py"
caminho_transformacao = "../scripts/transformar_salvar.py"


def executar_script(caminho_script):
    if os.path.exists(caminho_script):
        exec(open(caminho_script).read())
    else:
        raise FileNotFoundError(f"Script não encontrado: {caminho_script}")


definir_dag_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "processar_dados_influd",
    default_args=definir_dag_args,
    description="DAG para baixar e transformar dados do INFLUD",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    tarefa_extracao = PythonOperator(
        task_id="executar_extracao",
        python_callable=executar_script,
        op_kwargs={"caminho_script": caminho_extracao},
    )

    tarefa_transformacao = PythonOperator(
        task_id="executar_transformacao",
        python_callable=executar_script,
        op_kwargs={"caminho_script": caminho_transformacao},
    )

    tarefa_extracao >> tarefa_transformacao
