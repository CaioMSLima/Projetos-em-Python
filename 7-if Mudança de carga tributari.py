# Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela
# Ocorreu um aumento de 10% no preço do livro

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv',
            'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    i_livro = produtos.index('livro')
    total_antigo = produtos_ecommerce[i_livro][0] * \
        produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    novo_total = produtos_ecommerce[i_livro][0] * \
        produtos_ecommerce[i_livro][1]
    print('Vamos pagar de imposto a mais: R${:,}'.format(
        novo_total - total_antigo))
