# Usar a imagem base do Airflow
FROM apache/airflow:latest-python3.8

# Instalar o sudo (se necessário)
RUN apt-get update && apt-get install -y sudo

# Permitir que o usuário airflow execute sudo sem senha
RUN echo "airflow ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Instalar dependências adicionais (pandas e outras bibliotecas necessárias)
RUN pip install --no-cache-dir pandas

# (Opcional) Se você tiver um arquivo requirements.txt, pode instalá-lo também
# COPY requirements.txt /requirements.txt
# RUN pip install --no-cache-dir -r /requirements.txt

# Definir o diretório de trabalho
WORKDIR /opt/airflow

# Definir o usuário padrão (airflow)
USER airflow