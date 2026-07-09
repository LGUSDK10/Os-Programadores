while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno pelo nome")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        idade = input("Idade: ")
        turma = input("Turma: ")
        with open("alunos.txt", "a") as arquivo:
            arquivo.write(f"{nome};{idade};{turma}\n")
        print("Aluno cadastrado!")

    elif opcao == 2:
        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.split(";")
                print("Nome:", dados[0])
                print("Idade:", dados[1])
                print("Turma:", dados[2])

    elif opcao == 3:
        nome = input("Digite o nome do aluno: ")
        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            encontrado = False
            for linha in linhas:
                dados = linha.split(";")
                if dados[0] == nome:
                    print("Nome:", dados[0])
                    print("Idade:", dados[1])
                    print("Turma:", dados[2])
                    encontrado = True
            if encontrado == False:
                print("Aluno não encontrado.")
    elif opcao == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")