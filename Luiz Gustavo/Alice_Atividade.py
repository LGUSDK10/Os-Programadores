with open("Texto.txt", "r") as f: 
	conteudo = f.read() 
	conteudo = conteudo.replace("NEYMAR", "") 
	conteudo = conteudo.replace("NEYMAR.", "") 
with open("Texto_Atualizado.txt", "w") as f2: 
	f2.write(conteudo)