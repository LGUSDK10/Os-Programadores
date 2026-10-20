def desconto_percentual (porcentagem, preco):
    c = (porcentagem * preco) / 100
    return preco - c
def imposto_percentual (porcentagem, preco):
    d = (porcentagem * preco) / 100
    return preco + d
    








preco = float(input("Digite o preço original do produto: "))
b = float(input("Digite o percentual de desconto: "))
print(desconto_percentual(b, preco))