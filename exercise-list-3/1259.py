# beecrowd | 1259
'''
Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

Primeiro os Pares
Depois os Ímpares
Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

Entrada
A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

Saída
Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo abaixo.
'''
n = int(input())
listaPar = list()
listaImpar = list()
for _ in range(n):
    l = int(input())
    isPar = l % 2
    if isPar == 0:
        listaPar.append(l)
    else:
        listaImpar.append(l)

resultado = sorted(listaPar) + sorted(listaImpar, reverse=True)

for r in resultado:
    print(r)