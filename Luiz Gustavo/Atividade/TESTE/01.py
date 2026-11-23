def calcular_juros_composto(capital_i: float, taxa: float, meses: int) -> float:
    """
    Calcula o montante final de um investimento utilizando juros compostos.

    Args:
      capital_i (float): O valor do capital inicial.
      taxa (float): A taxa de juros mensal em porcentagem (deve ser estritamente positiva, > 0).
      meses (int): O número de meses em que o capital renderá (deve ser um valor inteiro).

    Returns:
      float: O valor total acumulado (montante) após o período.

    Exceções:
      A taxa não pode ser negativa ou zero.
    """
    if taxa <= 0:
        raise ValueError("A taxa de juros deve ser estritamente positiva (> 0).")
    montante = capital_i * (1 + taxa / 100) ** meses
    return montante

a = float(input("Digite o valor do capital inicial: "))
b = float(input("Digite a taxa de juros mensal (em %): "))
c = int(input("Digite o número de meses: "))

resultado = calcular_juros_composto(a, b, c)

print(f"O montante final após {c} meses é: {resultado:.2f}")