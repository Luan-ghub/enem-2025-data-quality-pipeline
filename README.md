# ENEM 2025 Data Quality Pipeline

--- 

## Objetivo

Construir um pipeline reproduzível de inspeção, limpeza, padronização e validação, utilizando o arquivo "PARTICIPANTES_2025.csv", referente ao ENEM DE 2025 como exemplo.

## Fonte oficial

- Instituição: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
- Edição: Enem 2025
- Página: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

## Restrições importantes

- Os arquivos originais permanecem fora deste repositório e não devem ser alterados.

- `NU_INSCRICAO`, da base de participantes, e `NU_SEQUENCIAL`, da base de resultados, são identificadores distintos apontados pela documentação oficial

## Estrutura

```text
enem-data/
├── data/ processed/
├── notebooks/
├── src/
├── tests/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Processo

Etapa 1 - Importação da fonte de dados, inspeção dos dados brutos, elaboração de análises e planejamento de limpeza

Etapa 2 - Limpeza, padronização dos dados e tipos de variáveis e salvamento das bases em Parquet, prontas para Elaboração de features ou análise exploratória seguinte

## Pipeline do Projeto


1. **Obtenção dos dados:** download dos microdados e consulta à documentação oficial do Inep.

2. **Configuração do ambiente:** instalação das dependências e definição do caminho local dos arquivos.

3. **Importação:** carregamento da base e configuração das bibliotecas utilizadas.

4. **Inspeção:**: avaliação da estrutura, tipos de dados, valores ausentes, duplicidades, domínios e consistência entre variáveis.

5. **Diagnóstico:**: registro dos problemas encontrados e definição dos critérios de tratamento.

6. **Plano de Limpeza:**: organização das transformações necessárias antes de alterar a base.

7. **Limpeza e padronização:**: aplicação das conversões de tipos, padronizações textuais e preservação das ausências justificadas.

8. **Validação:**: comparação da estrutura, dos valores ausentes, da unicidade e dos domínios antes e depois do tratamento.

9. **Exportação:**: armazenamento da base processada em Parquet
    

## Conclusões

### Principais Resultados  - Inspeção
- As inscrições não apresentaram valores ausentes ou duplicados.
- As variáveis categóricas avaliadas respeitaram os domínios do dicionário oficial.
- As 27 unidades federativas apresentaram correspondência válida entre códigos e siglas.
- Não foram encontradas respostas inválidas nos questionários
- TP_ENSINO foi a única coluna com valores tecnicamente ausentes, totalizando 64,04% da base, podendo ser consequência de uma pergunta anterior. Como não podem ser reconstruídos com segurança, foram preservados.

### Principais Resultados  - Limpeza
- Conversão de NU_INSCRICAO, CO_MUNICIPIO_PROVA e CO_UF_PROVA para texto;
- Conversão de TP_ENSINO para o tipo inteiro anulável Int8;
- Remoção de espaços externos nas colunas textuais selecionadas;
- Preservação dos valores ausentes e das categorias oficiais;
- exportação da base final em Parquet com compressão Snappy.
- Validações feitas ao final do processo e teste executável da função de limpeza salvo em "tests"

### Arquivos principais

1. notebooks/01_inspecao_dados_brutos.ipynb: inspeção e definição do plano de limpeza;

2. notebooks/02_limpeza_padronizacao.ipynb: transformações, validação e exportação;

3. src/limpeza.py: função reutilizável de limpeza;

4. tests/test_limpeza.py: teste automatizado da função;

5. data/processed/participantes_2025_limpo.parquet: saída local não versionada.

## Reprodução

1. Clone este repositório

2. Baixe os Microdados do Enem 2025 na página oficial do Inep e extraia o arquivo em uma pasta local.

3. Crie e ative um ambiente virtual. Em seguida, instale as dependências localizadas no `requirements.txt`

4. Crie o arquivo .env a partir do .env.example e informe o diretório em que os microdados foram extraídos: ENEM_RAW_DIR="C:/caminho/para/microdados_enem_2025"

5. Execute os notebooks nesta ordem:
notebooks/01_inspecao_dados_brutos.ipynb
notebooks/02_limpeza_padronizacao.ipynb

6. Após gerar a base processada, execute a validação em pytest
