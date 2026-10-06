from src.analise import calcular_valot_total, classificar_status, aplicar_curva_abc
import pandas as pd
import pathlib

def main():
    caminho_arquivo = pathlib.Path('data/raw/estoque_exemplo.xlsx')
    df = pd.read_excel(caminho_arquivo)
    df = calcular_valot_total(df)
    df = classificar_status(df)
    df = aplicar_curva_abc(df)

    sem_coluna = df.drop(columns=['pct_acumulado'])

    print('=' * 78)

    print('🔍PREVIEW DA ANÁLISE:')
    print(sem_coluna.head(10))

    local_exportado = pathlib.Path('outputs/relatorios/Planilha_Analisada.xlsx')
    sem_coluna.to_excel(local_exportado, index=False)

    print('=' * 78)

    print(f'\n📌--> Dados analisados de: {caminho_arquivo.stem}')
    print(f'📌--> Análise completa EXCEL salvo em: {local_exportado}')

    print('\nDesenvolvedor: Lucas Campos')
    print('https://github.com/lucasdevcampos')

if __name__ == '__main__':
    main()