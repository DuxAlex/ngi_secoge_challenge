FROM apache/airflow:latest-python3.8
USER root

ARG AIRFLOW_HOME=/opt/airflow
ADD dags /opt/airflow/dags

USER airflow # Make sure the airflow user is set before running commands
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3

USER ${AIRFLOW_UID}