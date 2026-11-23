def soma_valores():
    """
    Solicita dois números inteiros e realiza a soma, tratando erros de entrada.

    Returns:
        None: Exibe o resultado da soma ou mensagens de erro.
    """
    while True:
        try:
            valor1 = int(input("Digite um número: "))
        except ValueError:
            print("Erro: Digite um valor inteiro válido.")
        else:
            try:
                valor2 = int(input("Digite outro número: "))
                soma = valor1 + valor2
                print("Resultado da soma:", soma)
                break
            except (ValueError, TypeError):
                print("Erro: Não foi possível realizar a operação matemática.")

soma_valores()
