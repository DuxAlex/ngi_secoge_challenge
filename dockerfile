FROM apache/airflow:latest-python3.8

USER root

# Definir variáveis de ambiente
ARG AIRFLOW_HOME=/opt/airflow

# Adicionar os dags e os arquivos de configuração necessários
ADD dags /opt/airflow/dags
ADD transformado_INFLUD24-20-01-2025.csv /docker-entrypoint-initdb.d/
ADD setup.sql /docker-entrypoint-initdb.d/

# Instalar dependências adicionais
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3

# Ajustar as permissões para os arquivos no diretório de inicialização
#RUN chown -R postgres:postgres /docker-entrypoint-initdb.d/

# Voltar para o usuário airflow
USER ${AIRFLOW_UID}

# Definir o comando de inicialização padrão (caso necessário)
CMD ["bash", "-c", "airflow scheduler & airflow webserver"]
