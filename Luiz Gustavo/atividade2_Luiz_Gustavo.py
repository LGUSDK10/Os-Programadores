with open ("numeros.txt", "r") as arquivo:
    org = []
    for i in arquivo:
        org.append(int(i))
        org.sort()

with open ("numeros_organizados.txt", "w") as a:
    for i in org:
        a.write(str(i) + '\n')