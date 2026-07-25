multiplos4=open("múltiplos_de_4.txt","w")
pares=open("pares.txt")
for l in pares.readlines():
 if int(l) % 4 == 0:
    multiplos4.write(l)
pares.close()
multiplos4.close()