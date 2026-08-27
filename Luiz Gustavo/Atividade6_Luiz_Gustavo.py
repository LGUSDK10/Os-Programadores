alunos = [
    {"Nome": "Enzo", "Notas": 6.7},
    {"Nome": "Antônio", "Notas": 5.0},
    {"Nome": "Gustavo", "Notas": 10.0},
    {"Nome": "Bernardo", "Notas": 9.7},
    {"Nome": "Luiz Carlos", "Notas": 4.6}
]

cont = 0
a = 0
for i in alunos:
    a+=i["Notas"]
    if i["Notas"] >= 6:
        i["Situação"] = "Aprovado"
    else:
       i["Situação"] = "Reprovado"
    cont+= 1
media = a/cont

for i in alunos:
    print("O Aluno", i["Nome"], "ficou com a nota", i["Notas"],"a situação final foi:", i["Situação"])

melhor = max(alunos, key=lambda aluno: aluno["Notas"])

print("\nA média da turma foi:", media)
print("O aluno com a maior nota foi:", melhor["Nome"], "com a nota:", melhor["Notas"])