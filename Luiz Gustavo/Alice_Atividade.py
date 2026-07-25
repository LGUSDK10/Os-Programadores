while True:
	print("\n===== BIBLIOTECA =====")
	print("1 - Cadastrar livro")
	print("2 - Listar todos os livros")
	print("3 - Listar livros disponíveis")
	print("4 - Emprestar livro")
	print("5 - Devolver livro")
	print("6 - Sair")
	opcao = input("Escolha uma opção: ")

	if opcao == "1":
		titulo = input("Título: ")
		autor = input("Autor: ")
		with open("livro.txt", "a", encoding="utf-8") as arquivo:
			arquivo.write(f"{titulo};{autor};Disponivel\n")
		print("Livro cadastrado!")

	elif opcao == "2":
		try:
			with open("livro.txt", "r", encoding="utf-8") as arquivo:
				for linha in arquivo.readlines():
					titulo, autor, status = linha.strip().split(";")
					print(f"Título: {titulo}")
					print(f"Autor: {autor}")
					print(f"Status: {status}")
					print()
		except FileNotFoundError:
			print("Arquivo não encontrado!")

	elif opcao == "3":
		try:
			with open("livro.txt", "r", encoding="utf-8") as arquivo:
				for linha in arquivo.readlines():
					titulo, autor, status = linha.strip().split(";")
					if status == "Disponivel":
						print(f"Título: {titulo}")
						print(f"Autor: {autor}")
						print(f"Status: {status}")
						print()
		except FileNotFoundError:
			print("Arquivo não encontrado!")

	elif opcao == "4":
		titulo = input("Título do livro: ")
		try:
			with open("livro.txt", "r", encoding="utf-8") as arquivo:
				livros = arquivo.readlines()
		except FileNotFoundError:
			print("Arquivo não encontrado!")
			continue

		encontrado = False
		with open("livro.txt", "w", encoding="utf-8") as arquivo:
			for linha in livros:
				t, a, s = linha.strip().split(";")
				if t == titulo:
					encontrado = True
					if s == "Disponivel":
						s = "Emprestado"
						print("Livro emprestado!")
					else:
						print("Livro já está emprestado!")
				arquivo.write(f"{t};{a};{s}\n")
		if not encontrado:
			print("Livro não encontrado!")

	elif opcao == "5":
		titulo = input("Título do livro: ")
		try:
			with open("livro.txt", "r", encoding="utf-8") as arquivo:
				livros = arquivo.readlines()
		except FileNotFoundError:
			print("Arquivo não encontrado!")
			continue

		with open("livro.txt", "w", encoding="utf-8") as arquivo:
			encontrado = False
			for linha in livros:
				t, a, s = linha.strip().split(";")
				if t == titulo and s == "Emprestado":
					s = "Disponivel"
					encontrado = True
					print("Livro devolvido!")
				arquivo.write(f"{t};{a};{s}\n")
		if not encontrado:
			print("Livro não encontrado ou não estava emprestado!")

	elif opcao == "6":
		print("Programa encerrado!")
		break

	else:
		print("Opção inválida!")
