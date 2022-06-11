# List Comprehension

preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']


def calcular_imposto(preco, imposto):
    return preco * imposto


impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
print(impostos)
