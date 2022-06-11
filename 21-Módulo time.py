# Módulo time

import time
# Marco Zero (chamado de EPOCH) = 1 de Janeiro de 1970 às 00:00:00
# Time() retorna quantos segundos se passaram desde a EPOCH

segundos_hoje = time.time()
print(segundos_hoje)

# ctime retorna a data em string o texto no formato UTC (um formato padrão de datas
data_hoje = time.ctime()
# ou entao data_hoje = time.ctime(time())
print(data_hoje)

# Isso já pode ser muito útil para medir o tempo que uma ação leva, caso seja do interesse:
tempo_inicial = time.time()
for i in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print('O programa levou {} segundos para rodar'.format(duracao))

# Fazer o código esperar alguns segundos (muito útil quando temos que esperar um programa ou uma página carregar)
# para esperar 5 segundos fazemos:
print('Começando')
time.sleep(5)
print('Rodou 5 segundos após')

# Pegar informações de dias, hora, segundo, minuto, tudo detalhado:
# gmtime()
# gmtime().parâmetro

data_atual = time.gmtime()
print(data_atual)

# É um objeto diferente, mas podemos pegar os parâmetros de ano, mês, dia, etc fazendo:
ano = data_atual.tm_year
mes = data_atual.tm_mon
dia = data_atual.tm_mday
hora = data_atual.tm_hour
dia_da_semana = data_atual.tm_wday

print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))
