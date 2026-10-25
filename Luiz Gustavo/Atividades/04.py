
def processar_lista(lista):
    """
    Recebe uma lista de números e calcula seus resultados.

    Args:
        lista (list): Lista de números.

    Returns:
        Média, maior valor, menor valor e soma. Se a lista estiver vazia, retorna (0, 0, 0, 0).
        
    Exemplo:
        processar_lista([2, 4, 6])
        Retorna (4.0, 6, 2, 12).
    """
    if len(lista) > 0:
        media = sum(lista) / len(lista)
        maior_valor = max(lista)
        menor_valor = min(lista)
        soma = sum(lista)
    else:
        media = 0
        maior_valor = 0
        menor_valor = 0
        soma = 0

    return media, maior_valor, menor_valor, soma


a = []
resultado = processar_lista(a)

print("Média:", resultado[0])
print("Maior valor:", resultado[1])
print("Menor valor:", resultado[2])
print("Soma:", resultado[3])
