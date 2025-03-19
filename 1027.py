# URI Online Judge
# beecrowd | 1027
# Onda Crítica
'''
A tarefa é simples. Através de alguns pontos críticos em 2D, você deve desenhar uma onda como uma curva. Seu objetivo é incluir tantos pontos quantos forem possível.

Haverá uma linha imaginária y = a, a qual chamaremos de eixo principal para a curva.
Todos os pontos na curva deverão ter diferentes coordenadas x. Suas coordenadas y devem ser na forma a-1 ou a+1.
Dois pontos consecutivos na curva devem ter diferença de 2 na coordenada y.

Entrada
Haverá no máximo, 222 casos de testes. Cada caso inicia com um inteiro N, que é o número de pontos no caso de teste. Nas próximas N linhas, haverá N pares de inteiros dando as coordenadas x e y de cada ponto. Não haverá mais do que 1000 pontos em cada caso de teste. Todas coordenadas são inteiros – eles devem ficar dentro de um inteiro de 2 bytes com sinal. Os dados devem ser lidos da entrada padrão.

Saída
Para cada caso de teste, imprima um número – o número máximo de pontos críticos que podem ser incluídos em uma curva desenhada a partir dos pontos dados.
'''

# Importing defaultdict from collections library for convenient dictionary management
from collections import defaultdict

# This function is used to compare two lists of x-coordinates, 
# representing points on different levels of the wave curve.
def compare_points(x1, x2):
    # If the first list has elements and the second one doesn't, return 1.
    if x1 and not x2:
        return 1
    # If the first list is empty, return 0.
    if not x1:
        return 0
    # If the first element of both lists are equal, recursively compare the remaining elements
    # with additional count of 1.
    if x1[0] == x2[0]:
        return 1 + compare_points(x2[1:], x1[1:])
    # If the first element of the first list is less than that of the second list,
    # continue recursively comparing, moving forward in the first list.
    if x1[0] < x2[0]:
        return 1 + compare_points(x2, x1[1:])
    # Otherwise, skip the first element of the second list and keep comparing.
    return compare_points(x1, x2[1:])

# Infinite loop to continuously accept test cases
while True:
    try:
        # Read the number of critical points for the current test case
        n = int(input())
    except EOFError:
        # Exit the loop on End Of File (EOF)
        break
    
    # Dictionary to group x-coordinates by their respective y-coordinates
    y_dict = defaultdict(list)
    # List to accumulate maximum curve points for each comparison
    curve_points = []
    
    # Loop through each point and classify x-coordinates by their y-coordinates
    for _ in range(n):
        x, y = map(int, input().split())
        y_dict[y].append(x)
    
    # For each y-coordinate, compare points at this level with those at the previous level (y-2)
    for y, x_above in y_dict.items():
        x_below = y_dict.get(y-2, [])
        # Add the best result of comparison between x-coordinates at y and y-2
        curve_points.append(compare_points(sorted(x_above), sorted(x_below)))
        # Also add the best result when reversing the roles of x_above and x_below
        curve_points.append(compare_points(sorted(x_below), sorted(x_above)))
    
    # Output the maximum number of included critical points for the current test case
    print(max(curve_points))




