def loop():
    """
    Solicita números inteiros repetidamente até que o usuário digite uma letra.

    Returns:
        None: Exibe os números informados ou uma mensagem de encerramento.
    """
    while True:
        try:
            numero = int(input("Digite um número (ou digite qualquer letra para encerrar): "))
            print(f"Você digitou: {numero}")
        except ValueError:
            print("Saindo do loop. Obrigado!")
            break

loop()