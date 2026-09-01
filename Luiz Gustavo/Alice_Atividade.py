arquivo = open("notas.txt", "r") 
notas = [] 

for linha in arquivo: 
	notas.append(float(linha.strip().replace(",", "."))) 
arquivo.close() 

quantidade = len(notas) 
maior = max(notas) 
menor = min(notas)

notas_ordenadas = notas.copy() 
notas_ordenadas.sort(reverse=True) 

relatorio = open("relatorio.txt", "w") 
relatorio.write("RELATÓRIO DE NOTAS\n\n") 
relatorio.write("Quantidade de alunos: " + str(quantidade) + "\n\n") 
relatorio.write("Notas da turma:\n") 

for nota in notas_ordenadas: 
	relatorio.write(str(nota) + "\n") 
relatorio.write("\nA maior nota é " + str(maior) + "\n") 
relatorio.write("A menor nota é " + str(menor) + "\n") 
relatorio.close() 