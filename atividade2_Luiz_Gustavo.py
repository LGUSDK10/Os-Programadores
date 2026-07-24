with open("numeros.txt", "r") as arquivo:
    linhas = []
    for i in arquivo:
        linhas.append(int(i))
        linhas.sort()

with open("numeros_organizados.txt", "w") as f:
    for item in linhas:
        f.write(str(item) + '\n')