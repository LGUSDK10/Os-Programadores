def converter_para_inteiro():
    """
    Solicita um número ao usuário e tenta convertê-lo para inteiro.

    Returns:
        None: Exibe o número convertido ou uma mensagem de erro.
    """
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"O número convertido é: {numero}")
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros válidos.")

converter_para_inteiro()