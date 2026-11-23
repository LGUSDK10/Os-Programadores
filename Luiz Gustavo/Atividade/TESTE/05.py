def calcular_calorias(peso, altura, idade, genero="masculino", atividade=1.2):
    """
    Calcula a recomendação diária de calorias.

    Args:
        peso (float): Peso em kg.
        altura (float): Altura em cm.
        idade (int): Idade em anos.
        genero (str): "masculino" ou "feminino". Padrão: masculino.
        atividade (float): Fator de atividade física. Padrão: 1.2.

    Returns:
        float: Quantidade diária recomendada de calorias.

    Fórmula de Mifflin-St Jeor:
        Masculino: (10*peso) + (6.25*altura) - (5*idade) + 5
        Feminino: (10*peso) + (6.25*altura) - (5*idade) - 161

    O resultado é multiplicado pelo fator de atividade.
    """
    if genero == "masculino":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

    return tmb * atividade


calorias = calcular_calorias(60, 170, 17)
print("Calorias diárias:", round(calorias, 2))
