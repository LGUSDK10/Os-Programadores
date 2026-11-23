def raiz_quadrada(n):
    """
    Calcula a raiz quadrada de um número, tratando valores negativos.

    Args:
        n (float): Número utilizado no cálculo da raiz quadrada.

    Returns:
        None: Exibe o resultado ou uma mensagem de erro.
    """
    try:
        if n < 0:
            raise ValueError("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
        resultado = n ** 0.5
        print(f"A raiz quadrada de {n} é: {resultado}")
    except ValueError as e:
        print(e)

n = float(input("Digite um número para calcular a raiz quadrada: "))
raiz_quadrada(n)