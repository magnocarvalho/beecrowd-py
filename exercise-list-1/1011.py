# BEE 1011
# Esfera
'''
Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). 
A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), 
pois algumas linguagens (dentre elas o C++), 
assumem que o resultado da divisão entre dois inteiros é outro inteiro.

Entrada
O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.
'''

a = input()
pi = 3.14159
volume = (4/3) * pi * float(a)**3
print("VOLUME = {:.3f}".format(volume))