import pandas as pd

from src.limpeza import limpar_participantes


def test_limpar_participantes():
    dados = pd.DataFrame(
        {
            "NU_INSCRICAO": [
                " 210066506229 ",
                "210066506230",
            ],
            "TP_ENSINO": [1.0, None],
            "CO_MUNICIPIO_PROVA": [
                " 2927408",
                "2611606 ",
            ],
            "CO_UF_PROVA": [
                " 29",
                "26 ",
            ],
            "NO_MUNICIPIO_PROVA": [
                " Salvador ",
                "Recife ",
            ],
            "Q005": [3, 4],
        }
    )

    resultado = limpar_participantes(dados)

    # Estrutura preservada
    assert resultado.shape == dados.shape

    # Tipos convertidos
    assert str(resultado["NU_INSCRICAO"].dtype) == "string"
    assert str(resultado["TP_ENSINO"].dtype) == "Int8"
    assert str(resultado["CO_MUNICIPIO_PROVA"].dtype) == "string"
    assert str(resultado["CO_UF_PROVA"].dtype) == "string"

    # Espaços externos removidos
    assert resultado["NU_INSCRICAO"].tolist() == [
        "210066506229",
        "210066506230",
    ]
    assert resultado["CO_MUNICIPIO_PROVA"].tolist() == [
        "2927408",
        "2611606",
    ]
    assert resultado["CO_UF_PROVA"].tolist() == ["29", "26"]
    assert resultado["NO_MUNICIPIO_PROVA"].tolist() == [
        "Salvador",
        "Recife",
    ]

    # Valor ausente preservado
    assert resultado["TP_ENSINO"].isna().sum() == 1