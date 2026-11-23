import random

def simular_jogada(tipo, lados):
    """
    Simula uma jogada de dado.

    Args:
        tipo (str): Tipo do dado (D4, D6, D8, D10, D12 ou D20).
        lados (int): Quantidade de lados.

    Returns:
        int: Número sorteado entre 1 e lados.
        None: Se os valores forem inválidos.
    """

    def gerar_numero():
        return random.randint(1, lados)

    if tipo != "D" + str(lados) or lados < 2:
        return None

    return gerar_numero()


print(simular_jogada("D6", 6))
