with open ("notas.txt", "r") as arquivo:
    notas = []
    for i in arquivo:
        notas.append(float(i))

qtd = len(notas)
maior = max(notas)
menor = min(notas)

lista_copy = notas.copy()

lista_ord = sorted(lista_copy, reverse=True)

with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO DE NOTAS\n\n")
    
    arquivo.write(f"Quantidade de alunos: {qtd}\n\n")
    
    arquivo.write("Notas da turma:\n")
    for nota in lista_ord:
        arquivo.write(f"{nota}\n")
    
    arquivo.write(f"\nA maior nota é {maior}\n")
    arquivo.write(f"A menor nota é {menor}\n")