import pandas as pd

# Caminho do arquivo CSV
url_csv = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2024/INFLUD24-20-01-2025.csv"

# Carregar o CSV especificando o delimitador correto
dados = pd.read_csv(url_csv, delimiter=';')

# Definir as colunas desejadas
colunas_selecionadas = [
    "SG_UF_NOT", "ID_MUNICIP", "CO_MUN_NOT", "ESTRANG", "CS_SEXO",
    "DT_NASC", "NU_IDADE_N", "CS_GESTANT", "CS_RACA", "FATOR_RISC",
    "VACINA_COV", "CLASSI_FIN", "EVOLUCAO"
]

dados_selecionados = dados[colunas_selecionadas]

# Filtrar os dados onde SG_UF_NOT é "PE" ou "26"
dados_pe_ou_26 = dados_selecionados[dados_selecionados["SG_UF_NOT"].isin(["PE", "26"])]

# Excluir as linhas que possuam dados nulos ou vazios
dados_limpos = dados_pe_ou_26.dropna()

# Função para garantir que uma coluna seja convertida para inteiros
def converter_para_inteiro(coluna):
    return pd.to_numeric(coluna, errors='coerce', downcast='integer')

# Converter as colunas com valores decimais para inteiros
colunas_a_converter = ["ESTRANG", "VACINA_COV", "CLASSI_FIN", "EVOLUCAO"]
for coluna in colunas_a_converter:
    dados_limpos[coluna] = converter_para_inteiro(dados_limpos[coluna])

# Excluir as linhas onde a conversão não foi possível (resultou em NaN)
dados_limpos = dados_limpos.dropna(subset=colunas_a_converter)

# Exibir as 5 primeiras linhas
dados_exibicao = dados_limpos.head(5)

# Exibir as linhas filtradas e limpas
print(dados_exibicao)

# Gerar o arquivo CSV com os dados limpos (sem limitar às 5 primeiras linhas)
caminho_saida = "../data/transformado_INFLUD24-20-01-2025.csv"
dados_limpos.to_csv(caminho_saida, index=False, sep=';')

print(f"Arquivo CSV gerado: {caminho_saida}")
