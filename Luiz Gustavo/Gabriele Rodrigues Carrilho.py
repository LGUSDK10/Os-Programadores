arquivo = open("notas.txt", "r")

notas = []

for linha in arquivo:
    nota = float(linha.strip())
    notas.append(nota)

arquivo.close()

quantidade_alunos = len(notas)

maior_nota = max(notas)
menor_nota = min(notas)

notas_ordenadas = notas.copy()

notas_ordenadas.sort(reverse=True)

relatorio = open("relatorio.txt", "w")

relatorio.write("RELATÓRIO DE NOTAS\n\n")

relatorio.write(f"Quantidade de alunos: {quantidade_alunos}\n\n")

relatorio.write("Notas da turma:\n")

for nota in notas_ordenadas:
    relatorio.write(f"{nota}\n")

relatorio.write(f"\nA maior nota é {maior_nota}\n")
relatorio.write(f"A menor nota é {menor_nota}\n")

relatorio.close()

print("Relatório criado com sucesso!")