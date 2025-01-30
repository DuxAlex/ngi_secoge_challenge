ferramentas 
1. extração: pandas e request.
2. transformação: pandas.
3. Carregar: 
4. orquestração de processos: Airflow ou Airbyte.
5. banco de dados: PostgreSQL(docker)
6. Linguagem: python e SQL.
7. Outra bibliotecas:Psycopg2
8. setup de ambiente: docker


instalar a versão mais atual do python
site python

ambiente virtual
1. pip install virtualenv
2. virtualenv venv

No Linux:
bash
source .venv/bin/activate

No Windows:

venv\Scripts\activate

3. pip install -r requirements.txt


pip freeze > requirements.txt

sudo docker compose down
sudo docker compose up -d

Para reiniciar o container do PostgreSQL:
sudo docker restart ngi_secoge_postgres

ver log de erro do container
sudo docker logs ngi_secoge_postgres

entrar no container do postgres
sudo docker exec -it ngi_secoge_postgres psql -U ngisecoge
1. Listar Bancos de Dados
Para listar todos os bancos de dados no PostgreSQL, use o comando:

sql
\l
2. Conectar-se a um Banco de Dados
Se você quiser se conectar a um banco de dados específico (caso já tenha mais de um), use o comando:

sql
\c nome_do_banco
3. Listar Tabelas
Para listar todas as tabelas no banco de dados atual, use:

sql

\dt
4. Consultar Dados de uma Tabela
Para realizar uma consulta simples, como selecionar todos os registros de uma tabela, você pode usar o comando SQL:

sql

SELECT * FROM dados_influd24;
Substitua nome_da_tabela pelo nome da tabela que você deseja consultar.

5. Mostrar Estrutura de uma Tabela
Se você quiser ver a estrutura de uma tabela (colunas, tipos de dados, etc.), use:

sql

\d nome_da_tabela
6. Sair do PostgreSQL
Para sair do terminal do PostgreSQL, use o comando:

sql
\q

