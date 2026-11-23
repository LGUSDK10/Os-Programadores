def divisao_segura(num1, num2):
    """
    Realiza a divisão entre dois números, tratando possíveis erros.

    Args:
        num1 (float): Primeiro número da divisão.
        num2 (float): Segundo número da divisão.

    Returns:
        None: Apenas exibe o resultado ou uma mensagem de erro.
    """
    try:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
divisao_segura(num1, num2)