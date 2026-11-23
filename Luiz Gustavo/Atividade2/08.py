def interagir_com_arquivo():
    """
    Solicita o nome de um arquivo e tenta abrir e exibir seu conteúdo.

    Returns:
        None: Exibe o conteúdo do arquivo ou uma mensagem de erro.
    """
    try:
        nome_arquivo = input("Digite o nome do arquivo que deseja abrir (lembre-se de incluir a extensão, por exemplo, 'arquivo.txt'): ")
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

interagir_com_arquivo()