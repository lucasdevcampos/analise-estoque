from src.analise import calcular_valor_total, classificar_status, aplicar_curva_abc
import pandas as pd
import pathlib
import sys

COLUNAS_OBRIGATORIAS = ['Produto','Quantidade','Preco_Unitario']

def main():
    caminho_arquivo = pathlib.Path('data/raw/estoque_exemplo.xlsx')
    try:
        df = pd.read_excel(caminho_arquivo)
    except FileNotFoundError:
        print(f"\nArquivo não encontrado: {caminho_arquivo.resolve()}")
        sys.exit(1)
    except Exception as e:
        print(f"\nErro ao ler o Excel: {type(e).__name__}: {e}")
        sys.exit(1)

    # VALIDAÇÃO DADOS
    faltando = [c for c in COLUNAS_OBRIGATORIAS if c not in df.columns]
    if faltando:
        print('\n' + '=' * 78)
        print('  ERRO: a planilha não tem as colunas obrigatórias.')
        print(f'\n  Faltando:   {faltando}')
        print(f'  Encontradas: {list(df.columns)}')
        print(f'\n  Obrigatórias: {COLUNAS_OBRIGATORIAS}')
        print(f'  Arquivo:   {caminho_arquivo.resolve()}')
        print('=' * 78)
        sys.exit(1)

    nulos = df[COLUNAS_OBRIGATORIAS].isna().any().any()
    if nulos:
        print(f'\nERRO: Existem valores ausentes para análise!')
        sys.exit(1)

    # ANÁLISE DADOS
    try:
        df = calcular_valor_total(df)
        df = classificar_status(df)
        df = aplicar_curva_abc(df)
    except KeyError as e:
        print(f"\n-> Erro inesperado (bug interno): coluna {e} não encontrada após validação.")
        sys.exit(1)

    # DESCARTE DE COLUNA ANALÍTICA
    df_final = df.drop(columns=['pct_acumulado'], errors='ignore')

    # MOSTRA UM PREVIEW DOS DADOS COM FUNÇÕES APLICADAS
    print('=' * 78)
    print('🔍PREVIEW DA ANÁLISE:')
    print(df_final.head(10))

    # EXPORTAÇÃO DE RESULTADOS
    local_exportado = pathlib.Path('outputs/relatorios/Planilha_Analisada.xlsx')
    local_exportado.parent.mkdir(parents=True, exist_ok=True)

    try:
        df_final.to_excel(local_exportado, index=False)
    except PermissionError:
        print(f"  Sem permissão para salvar: {local_exportado}")
        print("  Feche o arquivo no Excel e tente novamente.")
        sys.exit(1)
    except Exception as e:
        print(f"\nErro ao salvar: {type(e).__name__}: {e}")
        sys.exit(1)

    # MOSTRA INFORMAÇÕES DO ARQUIVO SALVO
    print('=' * 78)
    print(f'\n📌--> Dados analisados de: {caminho_arquivo.stem}')
    print(f'📌--> Análise completa EXCEL salvo em: {local_exportado}')

    # RODAPÉ AUTORAL
    print('\nDesenvolvedor: Lucas Campos')
    print('https://github.com/lucasdevcampos')

if __name__ == '__main__':
    main()