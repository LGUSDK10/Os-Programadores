estoque = {}

def adicionar_produto():
    """
    Adiciona um produto ao estoque após verificar seu nome e quantidade.

    Returns:
        None: Atualiza o estoque ou exibe uma mensagem de erro.
    """
    produto = input("Digite o nome do produto: ").strip()
    try:
        if produto == "":
            raise ValueError("O nome do produto não pode estar vazio.")
        elif produto in estoque:
            raise ValueError("Esse produto já existe no estoque.")

        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        estoque[produto] = quantidade
        print("Produto adicionado com sucesso!")
    except ValueError as erro:
        print(f"Erro: {erro}")

def remover_produto():
    """
    Remove um produto existente do estoque.

    Returns:
        None: Atualiza o estoque ou exibe uma mensagem de erro.
    """
    produto = input("Digite o nome do produto que deseja remover: ").strip()
    try:
        if produto not in estoque:
            raise KeyError("Produto não encontrado no estoque.")
        del estoque[produto]
        print("Produto removido com sucesso!")
    except KeyError as erro:
        print(f"Erro: {erro}")

def ver_estoque():
    """
    Exibe todos os produtos e suas respectivas quantidades no estoque.

    Returns:
        None: Exibe os produtos cadastrados ou informa que o estoque está vazio.
    """
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("\n--- ESTOQUE ---")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

def menu():
    """
    Exibe o menu principal e permite gerenciar as operações do estoque.

    Returns:
        None: Executa as operações escolhidas pelo usuário até o encerramento.
    """
    while True:
        print("\n===== SIMULADOR DE VENDAS =====")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Ver estoque")
        print("0 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                adicionar_produto()
            elif opcao == 2:
                remover_produto()
            elif opcao == 3:
                ver_estoque()
            elif opcao == 0:
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")

menu()