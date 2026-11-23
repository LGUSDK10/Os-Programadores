def converter_temperatura(valor, origem, destino):
    """
    Converte uma temperatura entre Celsius, Fahrenheit e Kelvin.

    Args:
        valor (float): Temperatura que será convertida.
        origem (str): Unidade de temperatura original (C, F ou K).
        destino (str): Unidade de temperatura desejada (C, F ou K).

    Returns:
        float: Temperatura convertida para a unidade de destino.

    Raises:
        ValueError: Se a unidade de origem ou destino for inválida.
    """
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida.")
  
    if destino == "C":
        resultado = celsius
    elif destino == "F":
        resultado = (celsius * 9 / 5) + 32
    elif destino == "K":
        resultado = celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida.")
    return resultado

def menu():
    """
    Exibe o menu do conversor e solicita os dados para realizar a conversão.

    Returns:
        None: Exibe o resultado da conversão ou uma mensagem de erro.
    """
    print("===== CONVERSOR DE TEMPERATURAS =====")
    print("C - Celsius")
    print("F - Fahrenheit")
    print("K - Kelvin")
    try:
        valor = float(input("\nDigite a temperatura: "))
        origem = input("Unidade original (C/F/K): ").strip().upper()
        destino = input("Unidade de destino (C/F/K): ").strip().upper()

        if origem not in ["C", "F", "K"]:
            raise ValueError("Unidade original inválida!")
        if destino not in ["C", "F", "K"]:
            raise ValueError("Unidade de destino inválida!")
        resultado = converter_temperatura(valor, origem, destino)
        print(f"\nResultado: {resultado:.2f} °{destino}")
    except ValueError as erro:
        print(f"\nErro: {erro}")
    except OverflowError:
        print("\nErro: Valor muito grande para conversão.")

menu()