# Function para cálculo do Percentual e da Lista de Vendedores

from pickle import APPEND

meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Ramon': 7870,
}

bateram_meta = []

def atingiram_meta(lista, meta):
    qtd_funciorios = len(lista)
    for vendedor, venda in lista.items():
        if venda > meta:
            bateram_meta.append(vendedor)
            porc_meta = len(bateram_meta) / qtd_funciorios
    return bateram_meta, '{:.1%}'.format(porc_meta)

print(atingiram_meta(vendas, meta))
