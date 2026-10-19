import pandas as pd
import pytest
from src.analise import calcular_valor_total, classificar_status, aplicar_curva_abc


def test_calcular_valor_total():
    """Valor_Total deve ser Quantidade * Preco_Unitario."""
    df = pd.DataFrame({
        'Produto': ['A', 'B'],
        'Quantidade': [10, 5],
        'Preco_Unitario': [2.0, 10.0],
    })
    resultado = calcular_valor_total(df)
    assert list(resultado['Valor_Total']) == [20.0, 50.0]


def test_calcular_valor_total_nao_muta_original():
    """A função não deve alterar o DataFrame de entrada."""
    df = pd.DataFrame({
        'Produto': ['A'],
        'Quantidade': [10],
        'Preco_Unitario': [2.0],
    })
    calcular_valor_total(df)
    assert 'Valor_Total' not in df.columns


def test_classificar_status_padrao():
    """Quantidade < 10 deve virar 'Crítico', senão 'OK'."""
    df = pd.DataFrame({
        'Produto': ['A', 'B'],
        'Quantidade': [5, 20],
        'Preco_Unitario': [1.0, 1.0],
    })
    resultado = classificar_status(df)
    assert list(resultado['Status']) == ['Crítico', 'OK']


def test_classificar_status_minimo_customizado():
    """O parâmetro minimo deve ser respeitado."""
    df = pd.DataFrame({
        'Produto': ['A', 'B'],
        'Quantidade': [5, 8],
        'Preco_Unitario': [1.0, 1.0],
    })
    resultado = classificar_status(df, minimo=10)
    assert list(resultado['Status']) == ['Crítico', 'Crítico']

    resultado2 = classificar_status(df, minimo=5)
    assert list(resultado2['Status']) == ['OK', 'OK']


def test_aplicar_curva_abc_classifica_corretamente():
    """Valores 80/10/5/5 devem gerar A, B, B, C."""
    df = pd.DataFrame({
        'Produto': ['A', 'B', 'C', 'D'],
        'Valor_Total': [80.0, 10.0, 5.0, 5.0],
    })
    resultado = aplicar_curva_abc(df)
    assert list(resultado['curva']) == ['A', 'B', 'B', 'C']


def test_aplicar_curva_abc_ordena_decrescente():
    """A função deve ordenar por Valor_Total decrescente."""
    df = pd.DataFrame({
        'Produto': ['C', 'A', 'B'],
        'Valor_Total': [1.0, 100.0, 10.0],
    })
    resultado = aplicar_curva_abc(df)
    assert list(resultado['Produto']) == ['A', 'B', 'C']


def test_aplicar_curva_abc_nao_muta_original():
    """A função não deve alterar o DataFrame de entrada."""
    df = pd.DataFrame({
        'Produto': ['A', 'B'],
        'Valor_Total': [10.0, 5.0],
    })
    aplicar_curva_abc(df)
    assert 'curva' not in df.columns
    assert 'pct_acumulado' not in df.columns