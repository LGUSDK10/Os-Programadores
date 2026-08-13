with open ("notas.txt", "r") as arquivo:
    notas = []
    for i in arquivo:
        notas.append(float(i))
print(notas)

notas_novas = []

#with open ("notas_organizadas.txt", "w") as a:
    #for i in notas:
        #a.write(str(i) + '\n')

