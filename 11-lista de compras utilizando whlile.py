# Criar um sistema de vendas ,O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.

vendas = []

while True:
    produto = input('Qual o produto?')
    if not produto:
        break
    qtde = int(input('Qual a quantidade?'))
    vendas.append([produto, qtde])

print(vendas)
