with open ("nomes.txt", "r") as arquivo:
    lista = []
    for i in arquivo:
        lista.append(i)
        lista.sort()
with open ("Nomes_organizados.txt", "w") as f:
    for i in lista:
        f.write(i)