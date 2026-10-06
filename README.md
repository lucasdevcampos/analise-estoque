# Análise ABC de Estoque

Script em Python que lê uma planilha `.xlsx` de estoque, calcula valor total
por produto, classifica status por quantidade mínima, aplica a Curva ABC
(Pareto) e exporta uma nova planilha com os resultados.

## Como funciona

- Lê `data/raw/estoque_exemplo.xlsx`
- `calcular_valot_total(df)` — cria a coluna `Valor_Total` = `Quantidade × Preco_Unitario`
- `classificar_status(df, minimo=10)` — cria `Status` = `Crítico` se `Quantidade < minimo`, senão `OK`
- `aplicar_curva_abc(df)` — ordena por `Valor_Total`, calcula `pct_acumulado` e classifica `curva` em `A` (até 80%), `B` (80–95%) e `C` (95–100%)
- Remove `pct_acumulado` e exporta para `outputs/relatorios/Planilha_Analisada.xlsx`

## Entrada esperada

Planilha `.xlsx` com as colunas `Quantidade` e `Preco_Unitario`.

## Saída

Planilha com as colunas originais + `Valor_Total`, `Status` e `curva`.

## Autor

Lucas Campos — [@lucasdevcampos](https://github.com/lucasdevcampos)

## Licença

MIT
