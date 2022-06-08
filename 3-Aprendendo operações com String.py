faturamento = 2000
custo = 500
lucro = faturamento - custo

# Uso do str() e do concatenar com +
print('O faturamento da loja foi de: ' + str(faturamento) +
      ' O custo foi de ' + str(custo) + ' O lucro foi de ' + str(lucro))

# Uso do Format
print('O faturamento foi de: {0}. O custo foi de {1} e o Lucro foi de {2}. Lembrando, o faturamento foi de {0}'.format(
    faturamento, custo, lucro))

# Uso do %s e %d
print('O faturamento foi de: %d. O custo foi de %d e o Lucro foi de %d' %
      (faturamento, custo, lucro))

# Uso do in
print('@' in 'Cvbrerio@gmail.com')
print('@' in 'Cvbrerio.gmail.com')
