from sqlalchemy import create_engine, text

# Substitua pela sua URL de conexão com o PostgreSQL
engine = create_engine("postgresql://ngisecoge:ngisecoge@127.0.0.1:5432/ngisecoge")

# Estabelece a conexão com o banco
with engine.connect() as connection:
    # Executa a consulta SQL
    result = connection.execute(text("SELECT 1"))
    # Imprime o resultado
    print(result.fetchone())
