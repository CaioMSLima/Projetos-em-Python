
# Um código que diz caso algum produto estiver com a quantidade de estoque abaixo do estoque mínimo

estoque_minimo_alimentos = 50
estoque_minimo_bebidas = 75
estoque_minimo_limpeza = 30

produto = input('Preecha com o nome do produto ')
quantidade = input('Preecha com a quantidade do produto ')
categoria = input('Preecha com a categoria do produto em letra minúsculas e no plural ')

if produto and quantidade and categoria:
    if categoria == 'bebidas':
        if int(quantidade) < estoque_minimo_bebidas:
            print('Solicita {} à equipe de compra, temos apenas {} unidades no estoque'.format(
                produto, quantidade))
    elif categoria == 'alimentos':
        if int(quantidade) < estoque_minimo_alimentos:
            print('Solicita {} à equipe de compra, temos apenas {} unidades no estoque'.format(
                produto, quantidade))
    else:
        if int(quantidade) < estoque_minimo_limpeza:
            print('Solicita {} à equipe de compra, temos apenas {} unidades no estoque'.format(
                produto, quantidade))
else:
    print('Preencha todas as informações')
