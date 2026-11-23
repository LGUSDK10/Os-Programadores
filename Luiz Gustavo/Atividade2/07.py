import time

def conectar_servidor():
    """
    Simula uma conexão com um servidor, tratando possíveis erros.

    Returns:
        None: Exibe mensagens sobre o processo de conexão.
    """
    try:
        print("Tentando conectar ao servidor...")
        time.sleep(5)
        print("Conexão bem-sucedida!")
    except ConnectionError as e:
        print(f"Erro ao conectar: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

conectar_servidor()