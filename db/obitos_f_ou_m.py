from sqlalchemy import create_engine
import pandas as pd

# Configurações de conexão com o banco de dados PostgreSQL
usuario = 'ngisecoge'
senha = 'ngisecoge'
dbname = 'ngisecoge'
host = '127.0.0.1'
porta = '5432'

# Criando a URL de conexão
url_conexao = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{dbname}"

# Criando o engine de conexão com o PostgreSQL
engine = create_engine(url_conexao)

# Definindo a consulta SQL
consulta_sql = """
SELECT 
    CS_SEXO, 
    COUNT(*) AS num_obitos
FROM 
    dados_influd24
WHERE 
    EVOLUCAO = '2' -- Óbito
GROUP BY 
    CS_SEXO
ORDER BY 
    num_obitos DESC 
LIMIT 100;
"""

# Usando o engine diretamente com o pandas
dados_resultado = pd.read_sql_query(consulta_sql, engine)

# Exibindo o resultado
print(dados_resultado)
