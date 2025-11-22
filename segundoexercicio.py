tuplaAlunos = (("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9), ("Paulo", 5), ("Maria", 8), ("Paulo", 8))
alunos_dict = dict()
alunos_media = dict()
for nome, nota in tuplaAlunos:
    if nome in alunos_dict:
        alunos_dict[nome].append(nota)
    else:
        alunos_dict[nome] = [nota]

for nome, notas in alunos_dict.items():
        alunos_media[nome] = (sum(notas)/len(notas))

alunos_ordenados = dict(sorted(alunos_media.items(), key=lambda item: item[1]))

print(f' Alunos em ordem crescente de média: {alunos_ordenados}')



