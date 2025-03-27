# beecrowd | 2136

l = int(-1)
amigo = ""
alunos = list()
while True:
    line = input()
    if line == 'FIM':
        break
    
    n, b = map(str, line.split(" "))
    alunos.append(n)
    if (l < 0) or l < len(n):
        if b == 'YES':
            amigo = n
lista = set(alunos)
listaOrdenada = sorted(lista)
for a in listaOrdenada:
    print(a)

print("Amigo do Habay:")
print(amigo)