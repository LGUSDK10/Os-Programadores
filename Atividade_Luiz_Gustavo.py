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

    if r == 2:
        with open("livros.txt", "r", encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            qtd = 0

            for linha in linhas:
                qtd += 1
            if qtd == 0:
                print("Nenhum Livro encontrado.")
            else:
                for linhas in linha:
                    dados = linha.split(";")
                    print("Título:", dados[0])
                    print("Autor:", dados[1])
                    print("Status:", dados[2])