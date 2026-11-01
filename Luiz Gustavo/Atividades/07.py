def converter_moeda(valor: float, moeda: str) -> float:
    """
    Converte um valor em Reais (BRL) para uma moeda estrangeira usando uma taxa fixa.

    Args:
        valor: float
            O valor em Reais (BRL) a ser convertido. Deve ser um número não negativo.
        moeda: str
            O código da moeda alvo (ex.: 'USD', 'EUR', 'GBP').
    
    Returns:
        float
            O valor convertido na moeda alvo.

    Moedas Suportadas e Taxas Fixas de Conversão (Exemplo):
        'USD' (Dólar Americano): Taxa de 5.00 BRL por USD
        'EUR' (Euro): Taxa de 5.50 BRL por EUR
        'GBP' (Libra Esterlina): Taxa de 7.00 BRL por GBP

    Lógica de Conversão e Validação:
        1. O código da moeda é convertido para letras maiúsculas para evitar erros de digitação.
        2. A função valida se o código informado está presente no dicionário de taxas suportadas.
       Caso contrário, levanta um erro do tipo ValueError.
        3. Valida se o valor em reais é positivo.
        4. O valor em reais é dividido pela taxa fixa correspondente para obter o montante na moeda estrangeira.
    """
    taxas = {
        'USD': 5.00,
        'EUR': 5.50,
        'GBP': 7.00
    }
    
    moeda_val = moeda.strip().upper()
    
    if moeda_val not in taxas:
        raise ValueError("Moeda não suportada. Use 'USD', 'EUR' ou 'GBP'.")
        
    if valor < 0:
        raise ValueError("O valor em reais não pode ser negativo.")
        
    valor_convertido = valor / taxas[moeda_val]
    return round(valor_convertido, 2)

valor = float(input("Digite o valor em reais (BRL): "))
moeda = input("Digite a moeda para conversão (USD, EUR, GBP): ")

convertido = converter_moeda(valor, moeda)
print(f"O valor convertido é: {convertido} {moeda.upper()}")