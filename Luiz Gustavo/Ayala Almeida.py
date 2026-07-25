while True:
    print("=== Sistema de Cadastro de Alunos ===")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Pesquisar aluno pelo nome")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        turma = input("Turma: ")
        arquivo = open("alunos.txt", "a")
        arquivo.write(nome + ";" + idade + ";" + turma + "\n")
        arquivo.close()
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        try:
            arquivo = open("alunos.txt", "r")
            for linha in arquivo:
                dados = linha.strip().split(";")
                print("Nome:", dados[0])
                print("Idade:", dados[1])
                print("Turma:", dados[2])
                print()
            arquivo.close()

        except FileNotFoundError:
            print("Arquivo não encontrado.")
    elif opcao == "3":
        nome_procurado = input("Digite o nome do aluno: ")
        encontrado = False

        try:
            arquivo = open("alunos.txt", "r")
            for linha in arquivo:
                dados = linha.strip().split(";")
                if dados[0].lower() == nome_procurado.lower():
                    print("Nome:", dados[0])
                    print("Idade:", dados[1])
                    print("Turma:", dados[2])
                    encontrado = True
                    break
            arquivo.close()

            if encontrado == False:
                print("Aluno não encontrado.")
        except FileNotFoundError:
            print("Aluno não encontrado.")
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")