
# Exemplo de Alinhamento
email = 'lira@gmail.com'
print('Meu e-mail não é {:^50}, show?'.format(email))

# Exemplo de Edição de Sinal
custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))

# Exemplo de Separador de Milhar
custo = 5000
faturamento = 2700
lucro = faturamento - custo
print('Faturamento foi {:+,} e lucro foi {:+,}'.format(faturamento, lucro))

# Formato com casas Decimais fixas
custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:.2f} e lucro foi {:.1f}'.format(faturamento, lucro))

# Formato Percentual
custo = 500
faturamento = 1300
lucro = faturamento - custo
margem = lucro / faturamento
print('Margem de lucro foi de {:.2%}'.format(margem))

# Formato Moeda -> Combinação de Formatos
custo = 5000
faturamento = 27000
lucro = faturamento - custo
print('Faturamento foi R${:,.2f} e lucro foi R${:,.2f}'.format(
    faturamento, lucro))

# transformando no formato brasileiro
lucro_texto = 'R${:_.2f}'.format(lucro)
print(lucro_texto.replace('.', ',').replace('_', '.'))

# Função round() para arredondar números, caso seja necessário
imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print('Imposto sobre o preço é de {}'.format(valor_imposto))
