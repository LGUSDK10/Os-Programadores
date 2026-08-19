with open("alunos_notas.txt", "r", encoding="utf-8") as arquivo:
    notas = arquivo.readlines()
matriz = []

for i in notas:
    aluno = i.split()
    matriz.append(aluno)
notas = []
nome = []

for i in matriz:
    nome.append(i[0])
    notas.append(float(i[1]))

qtd = len(notas)
maior = max(notas)
menor = min(notas)
nome_maior = nome[notas.index(maior)]
nome_menor = nome[notas.index(menor)]
nomes_ordenados = nome.copy()
nomes_ordenados.sort()

with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO DE NOTAS\n")
    arquivo.write(f"Quantidade de alunos: {qtd}\n")
    arquivo.write("Notas da turma:\n")

    for aluno in nomes_ordenados:
        posicao = nome.index(aluno)
        arquivo.write(f"{aluno} {notas[posicao]}\n")

    arquivo.write(f"A maior nota é de {nome_maior} ({maior})\n")
    arquivo.write(f"A menor nota é {nome_menor} ({menor})\n")