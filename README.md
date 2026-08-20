# ENEM 2025 Data Quality Pipeline

Projeto de portfólio para construir um processo reproduzível de inspeção, limpeza e padronização utilizando como exemplo os Microdados do Enem 2025.

## Objetivo

Construir um pipeline reproduzível de inspeção, limpeza, padronização e validação, utilizando o arquivo "PARTICIPANTES_2025.csv", referente ao ENEM DE 2025 como exemplo.

## Fonte oficial

- Instituição: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
- Edição: Enem 2025
- Página: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

## Restrições importantes

- Os arquivos originais permanecem fora deste repositório e não devem ser alterados.
- `NU_INSCRICAO`, da base de participantes, e `NU_SEQUENCIAL`, da base de resultados, são identificadores distintos, assim como pontuado na documentação oficial do disponível do INEP.

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

Etapa 1 - inspeção da fonte e definição do contrato de dados.
    inspeção concluída;
    principais resultados;
    próxima etapa: limpeza e padronização.

Etapa 2 - Limpeza e padronização dos dados.
    limpeza concluída
    padronização dos textos, tipos e variáveis numéricas executada
    base limpa salva em parquet 
    

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

1- notebooks/01_inspecao_dados_brutos.ipynb: inspeção e definição do plano de limpeza;

2- notebooks/02_limpeza_padronizacao.ipynb: transformações, validação e exportação;

3- src/limpeza.py: função reutilizável de limpeza;

4- tests/test_limpeza.py: teste automatizado da função;

5 - data/processed/participantes_2025_limpo.parquet: saída local não versionada.