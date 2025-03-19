# BEE 1047
'''
Tempo de Jogo com Minutos

Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

h1, m1, h2, m2 = map(int, input().split())
auxA = h1 * 60 + m1
auxB = h2 * 60 + m2
if auxA >= auxB:
    auxC = (24 * 60 - auxA) + auxB
    print(f"O JOGO DUROU {auxC // 60} HORA(S) E {auxC % 60} MINUTO(S)")
elif auxA < auxB:
    auxC = auxB - auxA
    print(f"O JOGO DUROU {auxC // 60} HORA(S) E {auxC % 60} MINUTO(S)")
else:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")