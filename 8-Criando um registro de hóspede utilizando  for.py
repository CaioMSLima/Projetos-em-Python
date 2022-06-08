# criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas

qtde_pessoas = int(input('Quantas pessoas terão no quarto?'))
quarto = []

for i in range(qtde_pessoas):
    nome = input('Qual o nome?')
    cpf = input('Qual o cpf?')
    hospede = [nome, 'cpf:{}'.format(cpf)]
    quarto.append(hospede)

print(quarto)
