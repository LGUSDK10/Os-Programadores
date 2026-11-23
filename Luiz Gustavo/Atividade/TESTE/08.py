def prever_vendas(vendas_iniciais: float, periodo: int, taxa: float) -> float:
    """
    Calcula a previsão de vendas utilizando o regime de juros compostos.

    Args:
        vendas_iniciais: float
            O valor base ou atual das vendas antes da projeção. Deve ser um número não negativo.
        periodo: int
            O horizonte de tempo da projeção em meses. Deve ser um número inteiro não negativo.
        taxa: float
            A taxa de crescimento periódica (mensal). Deve ser um valor estritamente positivo 
            (ex: 0.05 para representar 5% de crescimento ao mês).

    Returns:
        float
            O valor projetado das vendas ao final do período, arredondado para 2 casas decimais.

    Lógica de Cálculo e Validação:
    1. Validação da Taxa: Verifica se a taxa é maior que zero. Caso contrário, levanta um ValueError,
       pois uma taxa nula ou negativa impediria o crescimento composto esperado.
    2. Validação dos Dados de Entrada: Garante que o valor inicial e o período não sejam negativos.
    3. Fórmula de Juros Compostos aplicada às vendas:
       V_final = V_inicial . (1 + taxa)^periodo
       Onde o montante cresce exponencialmente a cada mês com base no período acumulado.
    """
    if taxa <= 0:
        raise ValueError("A taxa de crescimento deve ser um valor positivo (> 0).")
        
    if vendas_iniciais < 0:
        raise ValueError("O valor de vendas iniciais não pode ser negativo.")
        
    if periodo < 0:
        raise ValueError("O período em meses não pode ser negativo.")
        
    previsao = vendas_iniciais * ((1 + taxa) ** periodo)
    
    return round(previsao, 2)

a = float(input("Digite o valor inicial das vendas: "))
periodo = int(input("Digite o período em meses: "))
taxa = float(input("Digite a taxa de crescimento mensal (ex: 0.05 para 5%): "))

print(f"Previsão de vendas ao final do período: {prever_vendas(a, periodo, taxa)}")