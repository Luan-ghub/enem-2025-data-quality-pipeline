# ENEM 2025 Data Quality Pipeline

Projeto de portfólio para construir um processo reproduzível de inspeção, limpeza e padronização dos Microdados do Enem 2025.

## Objetivo

Transformar os arquivos públicos do Inep em produtos de dados padronizados, documentados e validados, preservando os arquivos originais e respeitando as restrições documentais da edição.

## Fonte oficial

- Instituição: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
- Edição: Enem 2025
- Página: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

## Restrições importantes

- Os arquivos originais permanecem fora deste repositório e não devem ser alterados.
- `NU_INSCRICAO`, da base de participantes, e `NU_SEQUENCIAL`, da base de resultados, são identificadores distintos.
- As bases de participantes e resultados não podem ser relacionadas em nível individual.
- Arquivos de dados gerados localmente não serão versionados no Git.

## Estrutura

```text
enem-data/
├── data/
│   ├── modified/
│   └── processed/
├── docs/
├── notebooks/
├── reports/
├── src/
├── tests/
├── .gitignore
└── README.md
```

## Situação atual

Etapa 1 - inspeção da fonte e definição do contrato de dados.
    inspeção concluída;
    principais resultados;
    próxima etapa: limpeza e padronização.

Etapa 2 - Limpeza e padronização dos dados.
