# beecrowd | 2136

amigo = ""
max_length = -1
alunos_yes = []
alunos_no = []

while True:
    line = input()
    if line == 'FIM':
        break
    
    n, b = map(str, line.split(" "))
    if b == 'YES':
        alunos_yes.append(n)
        # Atualizar o "Amigo do Habay" com base no critério
        if len(n) > max_length:
            max_length = len(n)
            amigo = n
    else:
        alunos_no.append(n)

# Ordenar as listas
alunos_yes = sorted(set(alunos_yes))
alunos_no = sorted(set(alunos_no))

# Imprimir a lista de inscritos
for a in alunos_yes:
    print(a)
for a in alunos_no:
    print(a)

# Imprimir o vencedor com uma linha em branco antes
print()
print("Amigo do Habay:")
print(amigo)