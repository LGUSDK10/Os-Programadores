import json
alunos = []
escolha = 0

while escolha != 3:
    print("\n=== Cadastro de Alunos ===")
    print("1- Cadastrar Aluno")
    print("2- Exibir Alunos")
    print("3- Sair")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        aluno = {"Nome": nome, "Notas": nota}
        alunos.append(aluno)
    elif escolha == 2:
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for i in alunos:
                print("O Aluno", i["Nome"], "ficou com a nota", i["Notas"])
    elif escolha == 3:
        print("Saindo do programa...")
        with open("alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False)
    else:
        print("Opção inválida. Tente novamente.")