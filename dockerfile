# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /src

# Copie os arquivos do projeto
COPY . .

# Instale as dependências
RUN pip install -r requirements.txt

# Comando para iniciar o aplicativo
CMD ["python", "app.py"]


# # Use uma imagem base oficial do Python
# FROM python:3.9-slim

# # Instale o Poetry
# RUN pip install poetry

# # Crie um diretório para o seu projeto
# WORKDIR /app

# # Copie os arquivos do projeto para o contêiner
# COPY . .

# # Instale as dependências usando o Poetry
# RUN poetry install --no-root

# # Exponha a porta que seu aplicativo usará (caso tenha um servidor web)
# EXPOSE 8000

# # Defina o comando para rodar seu aplicativo
# CMD ["poetry", "run", "python", "app.py"]  # Ajuste conforme necessário
