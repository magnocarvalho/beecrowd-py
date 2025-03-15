# BEE 1020
# Idade em Dias
'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.
'''
a = int(input())
anos = a // 365
meses = (a % 365) // 30
dias = (a % 365) % 30
print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')