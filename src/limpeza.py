"""Funções de limpeza e padronização dos participantes do ENEM 2025."""

import pandas as pd


TIPOS_ESPERADOS = {
    "NU_INSCRICAO": "string",
    "TP_ENSINO": "Int8",
    "CO_MUNICIPIO_PROVA": "string",
    "CO_UF_PROVA": "string",
    "Q005": "int",
}

COLUNAS_TEXTO = [
    "NU_INSCRICAO",
    "CO_MUNICIPIO_PROVA",
    "CO_UF_PROVA",
    "NO_MUNICIPIO_PROVA",
]


def limpar_participantes(dados: pd.DataFrame) -> pd.DataFrame:
    """Aplica as regras de limpeza que foram definidas e testadas no notebook para a base de participantes.
        Entrada: Dataframe com os dados brutos;
        Saída: Dataframe com os tipos corrigidos e colunas textuais padronizadas."""

    dados_limpos = dados.astype(TIPOS_ESPERADOS)

    for coluna in COLUNAS_TEXTO:
        dados_limpos[coluna] = dados_limpos[coluna].str.strip()

    return dados_limpos