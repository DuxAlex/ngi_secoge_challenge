# Relatório: Projeto NGI Secoge Challenge

Este relatório apresenta a estrutura, objetivos, ferramentas e metodologia utilizada no **NGI Secoge Challenge**, um projeto de ETL (Extração, Transformação e Carregamento) para análise de dados.

---

## Descrição dos Dados Escolhidos

Os dados escolhidos para este projeto são provenientes do **Banco de Dados de Síndrome Respiratória Aguda Grave (SRAG) 2021 a 2024**, disponibilizado pelo Ministério da Saúde do Brasil. Esse banco de dados inclui informações sobre casos de SRAG, incluindo aqueles relacionados à COVID-19, coletados pela rede de vigilância epidemiológica do país.

Os dados contêm algumas informações como:

- Unidade Federativa (UF) e município onde está localizada a Unidade que realizou a notificação.
- Indicação se o paciente é estrangeiro.
- Sexo, data de nascimento e idade do paciente.
- Status gestacional e raça/cor do paciente.
- Presença de fatores de risco e vacinação contra COVID-19.
- Classificação final do caso (e.g., SRAG por influenza, SRAG por COVID-19).
- Evolução do caso (e.g., cura, óbito).

### Dados Filtrados
Para este projeto, os dados foram filtrados para incluir apenas os casos registrados no estado de **Pernambuco**. Essa filtragem permite uma análise mais focada e relevante para a região.

---

## Link(s) para a(s) Fonte(s) de Dados

- **Base de Dados SRAG 2024 (20/01/2025)**:
  - URL: [SRAG 2024 - 20/01/2025](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2024/INFLUD24-20-01-2025.csv)
- **Página Oficial do Ministério da Saúde**:
  - Gripe/Influenza: [https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/g/gripe-influenza](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/g/gripe-influenza)
  - COVID-19: [https://www.gov.br/saude/pt-br/coronavirus](https://www.gov.br/saude/pt-br/coronavirus)
  - Guia de Vigilância Epidemiológica da COVID-19: [https://www.gov.br/saude/pt-br/coronavirus/publicacoes-tecnicas/guias-e-planos/guia-de-vigilancia-epidemiologica-covid-19/view](https://www.gov.br/saude/pt-br/coronavirus/publicacoes-tecnicas/guias-e-planos/guia-de-vigilancia-epidemiologica-covid-19/view)

---

## Motivação para a Escolha dos Dados

Escolhi esses dados porque:
1. **Relevância**: A SRAG e a COVID-19 são temas de grande importância para a saúde pública, especialmente após a pandemia.
2. **Potencial de Análise**: Os dados permitem explorar tendências epidemiológicas, como a evolução de casos e óbitos, distribuição geográfica e impacto de comorbidades.
3. **Foco Regional**: A filtragem dos dados para Pernambuco possibilita análises específicas para a região, contribuindo para decisões locais de saúde pública.

---

## Extração e Transformação

### Visão Geral do Projeto

O projeto foi desenvolvido com foco na criação de uma pipeline de dados automatizada, utilizando tecnologias modernas para extrair, transformar e carregar informações. O processo foi dividido nas seguintes etapas:

1. **Extração**:
   - Os dados foram coletados diretamente do arquivo CSV disponibilizado pelo Ministério da Saúde, utilizando a biblioteca `request` e `os` em Python.
   - A filtragem dos dados para Pernambuco foi realizada durante a extração, utilizando a coluna `SG_UF_NOT` (sigla do estado de notificação).

2. **Transformação**:
   - Os dados brutos foram processados e limpos utilizando `pandas` e SQL.
   - Etapas de transformação incluíram:
     - Remoção de valores nulos ou inconsistentes.
     - Seleção de colunas relevantes para análise (e.g.,SG_UF_NOT, ID_MUNICIP, CO_MUN_NOT, ESTRANG, CS_SEXO,  
DT_NASC, NU_IDADE_N, CS_GESTANT, CS_RACA, FATOR_RISC, VACINA_COV, CLASSI_FIN, EVOLUCAO).
     - Junção de dados demográficos para criar uma visão unificada.

3. **Banco de Dados Utilizado**:
   - **PostgreSQL**: Escolhido por sua robustez, suporte a consultas complexas e facilidade de integração com ferramentas de análise.
   - O banco de dados foi configurado em um contêiner Docker para garantir portabilidade e replicação do ambiente.

4. **Carregamento**:
   - Os dados transformados foram armazenados em tabelas otimizadas no PostgreSQL, prontas para consultas e geração de relatórios atraveś do `setup.sql` e `docker` no ponto de incialização presente docker compose `./data:/docker-entrypoint-initdb.d`.

---
