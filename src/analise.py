import pandas as pd
import numpy as np

def calcular_valot_total(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Valor_Total'] = df['Quantidade'] * df['Preco_Unitario']
    return df

def classificar_status(df: pd.DataFrame, minimo: int = 10) -> pd.DataFrame:
    df = df.copy()
    df['Status'] = np.where(df['Quantidade'] < minimo, "Crítico", "OK")
    return df

def aplicar_curva_abc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().sort_values("Valor_Total", ascending=False)
    df['pct_acumulado'] = df['Valor_Total'].cumsum() / df['Valor_Total'].sum()
    df['curva'] = pd.cut(
        df['pct_acumulado'],
        bins=[0, 0.8, 0.95, 1],
        labels=['A', 'B', 'C'],
        include_lowest=True
    )
    return df