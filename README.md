# Desafio: Construção de um Pipeline de Dados

## Objetivo

O objetivo geral desse desafio é a construção de um pipeline de dados utilizando Python e SQL. Mais especificamente, você vai:

1. Construir um pipeline para extrair, transformar e carregar dados à sua escolha, usando Python e/ou SQL.
2. Elaborar duas consultas sobre esses dados, usando SQL.
3. Escrever um breve relatório sobre esses dados.

---

## Passos

### **1. Extração de Dados usando Python**

#### **Dados**

Escolha um conjunto de dados abertos ao público para utilizar nesse desafio.  
Recomenda-se que você escolha dados que ache interessantes ou que conheça bem. Não é necessário se limitar a dados de saúde!  

Você pode utilizar dados prontos (como arquivos `.csv`) ou criá-los você mesmo (por exemplo, com web scraping).

**Sugestões de fontes de dados:**

- [Base dos Dados](https://basedosdados.org/)
- [Kaggle](https://www.kaggle.com/)
- [openDataSUS](https://opendatasus.saude.gov.br/)
- Redes sociais (Letterboxd, Reddit, etc.)

#### **Extração**

Utilize Python para extrair os dados escolhidos.  
Exemplo: Se a fonte disponibiliza arquivos `.csv`, use Python para baixá-los automaticamente.

**Regras:**

- O código deve realizar a extração. Não é permitido baixar ou criar os arquivos manualmente.
- É permitido usar bibliotecas Python instaláveis via `pip`, como `requests`.
- É fortemente recomendado o uso de ferramentas de gerenciamento de dependências como `requirements.txt` ou `Poetry`.

---

### **2. Transformação e Carregamento dos Dados em um Banco SQL**

#### **Transformação**

Realize as transformações necessárias nos dados antes ou depois de carregá-los no banco de dados.  
Exemplo: Consolidar múltiplos arquivos `.csv` em um único dataframe, renomear colunas, ou criar chaves primárias.

#### **Carregamento**

Carregue os dados transformados em um banco SQL usando Python.  
Exemplos de bancos suportados:

- PostgreSQL (requer especificar nome da DB, porta e credenciais).
- SQLite (criar o arquivo `.db` via código Python).

**Regras:**

- É permitido usar Docker para rodar o banco ou o projeto.
- Se utilizar SQLite, o código deve gerar o arquivo `.db`.

---

### **3. Consultas SQL**

Escreva **duas consultas** ao banco de dados, buscando gerar dados interessantes.  
Exemplo: Dados de vacinação filtrados por cidade ou agrupados por cidadão.

**Regras:**

- Não é necessário realizar análises sobre os dados.
- O foco é gerar dados utilizáveis para análises futuras.

---

### **4. Relatório**

Escreva um breve relatório descrevendo o processo do desafio.  
Inclua, no mínimo, as seguintes informações:

#### **Dados**

- Breve descrição dos dados escolhidos.
- Link(s) para as fontes.
- Razão para a escolha dos dados.

#### **Extração e Transformação**

- Descrição geral do processo: como os dados foram extraídos e qual banco foi utilizado.

#### **Consultas**

- Explicação das duas consultas criadas.
- Justificativa das escolhas das consultas.

#### **Reflexões**

- Dificuldades enfrentadas e como foram resolvidas.
- O que poderia ser feito de forma diferente no projeto.

---

## Avaliação

O projeto será avaliado com base nos seguintes critérios:

1. **Conformidade:** O projeto segue as instruções descritas.
2. **Execução:** O código roda sem erros e conforme esperado.
3. **Compreensão:** Demonstra entendimento dos dados e ferramentas, seja por meio de comentários ou pelo relatório.

**Dica:** Prefira qualidade ao invés de quantidade ou complexidade!
