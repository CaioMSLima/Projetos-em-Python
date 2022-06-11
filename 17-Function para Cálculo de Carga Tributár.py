# Function para Cálculo de Carga Tributária

preco = 1500
custo = 400
lucro = 800


def carga_tributaria(valor, paguei, ganhei):
    tributo = valor - paguei - ganhei
    porc_tributo = tributo / valor
    return porc_tributo


print('a minha carga tributária é de {:.1%} da minha venda'.format(
    carga_tributaria(preco, custo, lucro)))
