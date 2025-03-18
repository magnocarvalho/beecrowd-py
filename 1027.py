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

n = int(input())
points = []

for _ in range(n):
    # EOF (End Of File), para encerrar o loop
    try:
        x, y = map(int, input().split())
        points.append((x, y))
    except EOFError:
        break
max_count = 0

for point in points:
    a = point[1]
    track_start_a_minus_1 = {a - 1}
    track_start_a_plus_1 = {a + 1}
    
    for current_x, current_y in points:
        if current_y in track_start_a_minus_1:
            max_count = max(max_count, len(track_start_a_minus_1))
            track_start_a_minus_1.add(current_y + 2)
            track_start_a_minus_1.add(current_y - 2)
            
        if current_y in track_start_a_plus_1:
            max_count = max(max_count, len(track_start_a_plus_1))
            track_start_a_plus_1.add(current_y + 2)
            track_start_a_plus_1.add(current_y - 2)

print(max_count)


