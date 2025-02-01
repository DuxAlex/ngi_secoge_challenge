from sqlalchemy import create_engine

# Configurações de conexão
usuario = 'ngisecoge'
senha = 'ngisecoge'
dbname = 'ngisecoge'
host = '0.0.0.0'
porta = '5432'

# Criando a URL de conexão
url_conexao = f"postgresql://{usuario}:{senha}@{host}:{porta}/{dbname}"

# Criando o engine de conexão com o PostgreSQL
engine = create_engine(url_conexao)

# Tentando uma conexão simples
with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    print("Conexão bem-sucedida:", result.fetchone())
