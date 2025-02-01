import os
import requests

# URL do arquivo CSV
url = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2024/INFLUD24-20-01-2025.csv"

# Caminho do diretório "data"
diretorio_data = "../data"

# Criar o diretório "data" se ele não existir
if not os.path.exists(diretorio_data):
    os.makedirs(diretorio_data)

# Caminho completo para salvar o arquivo CSV
caminho_arquivo = os.path.join(diretorio_data, "INFLUD24-20-01-2025.csv")

# Baixar o arquivo CSV
try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    with open(caminho_arquivo, "wb") as file:
        file.write(response.content)
    print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao baixar o arquivo: {e}")