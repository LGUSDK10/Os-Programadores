def ler_arquivo(nome_arquivo):
    """
    Lê o conteúdo de um arquivo. Caso ele não exista, cria um novo arquivo.

    Args:
        nome_arquivo (str): Nome ou caminho do arquivo que será acessado.

    Returns:
        None: Exibe o conteúdo do arquivo ou uma mensagem de criação.

    Raises:
        OSError: Caso ocorra um erro durante a criação do arquivo.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Este é um arquivo de teste.\n")
            print(f"Arquivo '{nome_arquivo}' criado com sucesso.")


nome_arquivo = "teste.txt"
ler_arquivo(nome_arquivo)