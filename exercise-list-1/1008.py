# BEE 1008
# Salário
'''
Escreva um programa que leia o número de um funcionário, 
seu número de horas trabalhadas, 
o valor que recebe por hora e calcula o salário desse funcionário. 
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, 
representando o número, 
quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, 
respectivamente.
'''
# Code
number = int(input())
hours = int(input())
hour_value = float(input())
salary = hours * hour_value
print("NUMBER = {}".format(number))
print("SALARY = U$ {:.2f}".format(salary))