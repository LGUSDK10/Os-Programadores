while True:
    print("=== MENU ===")
    print("1- Cadastrar livros")
    print("2- Listar todos os livros")
    print("3- Listar livros disponíveis")
    print("4- Emprestar livro")
    print("5- Devolver livro")
    print("6- Sair")
    r = int(input("Escolha uma opção: "))

    if r == 1:
        print("=== CADASTRO DE LIVRO ===")
        titulo = input("Insira o título do livro: ")
        autor = input("Insira o nome do autor: ")

        with open("livros.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(f"{titulo};{autor};Disponível\n")
        print("Livro cadastrado com sucesso!")

    elif r == 2:
        with open("livros.txt", "r", encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            qtd = 0

            for linha in linhas:
                qtd += 1
            if qtd == 0:
                print("Nenhum Livro encontrado.")
            else:
                for linha in linhas:
                    dados = linha.split(";")
                    print("Título:", dados[0])
                    print("Autor:", dados[1])
                    print("Status:", dados[2])

    elif r == 3:
        with open("livros.txt", "r", encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            qtd = 0

            for linha in linhas:
                dados = linha.split(";")
                if dados[2].strip() == "Disponível":
                    qtd += 1
                    print("Título:", dados[0])
                    print("Autor:", dados[1])
                    print("Status:", dados[2])
            if qtd == 0:
                print("Nenhum livro disponível.")
    elif r == 4:
        nome = input("Digite o nome do livro: ")
        with open("livros.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        qtd = 0

        with open("livros.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                dados = linha.split(";")
                if dados[0] == nome:
                    qtd += 1
                    if dados[2].strip() == "Disponível":
                        arquivo.write(dados[0] + ";" + dados[1] + ";Emprestado\n")
                        print("Livro emprestado!")
                    else:
                        arquivo.write(linha)
                        print("Esse livro já está emprestado.")
                else:
                    arquivo.write(linha)
        if qtd == 0:
            print("Livro não encontrado.")

    if r == 5:
        nome = input("Digite o nome do livro: ")
        with open("livros.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        qtd = 0

        with open("livros.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                dados = linha.split(";")

                if dados[0] == nome:
                    qtd += 1

                    if dados[2].strip() == "Emprestado":
                        arquivo.write(dados[0] + ";" + dados[1] + ";Disponível\n")
                        print("Livro devolvido!")
                    else:
                        arquivo.write(linha)
                        print("Esse livro já está disponível.")
                else:
                    arquivo.write(linha)

        if qtd == 0:
            print("Livro não encontrado.")

    elif r == 6:
        print("Encerrando o programa...")
        break