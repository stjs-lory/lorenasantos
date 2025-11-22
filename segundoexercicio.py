tuplaAlunos = (("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9), ("Paulo", 5), ("Maria", 8), ("Paulo", 8))
alunosDict = dict()
alunosMedia = dict()
for nome, nota in tuplaAlunos:
    if nome in alunosDict:
        alunosDict[nome].append(nota)
    else:
        alunosDict[nome] = [nota]

for nome, notas in alunosDict.items():
        alunosMedia[nome] = (sum(notas)/len(notas))

alunosOrdenados = dict(sorted(alunosMedia.items(), key=lambda item: item[1]))

print(f' Alunos em ordem crescente de média: {alunosOrdenados}')



