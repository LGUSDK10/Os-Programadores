GrupoA = [] 
GrupoB = [] 
 
for i in range(4): 
    nome = input("Digite uma seleção do Grupo A: ") 
    GrupoA.append([nome, 0, 3, 0, 0, 0, 0, 0, 0]) 
 
for i in range(4): 
    nome = input("Digite uma seleção do Grupo B: ") 
    GrupoB.append([nome, 0, 3, 0, 0, 0, 0, 0, 0]) 
 
# Grupo A 
time1 = 0 
time2 = 1 
 
for ii in range(6): 
    print("Insira o resultado do jogo:", GrupoA[time1][0], "X", GrupoA[time2][0]) 
 
    empate = input("Foi um empate? S ou N: ") 
 
    if empate.upper() == "N": 
        print("Quem venceu? Digite 1 para:", GrupoA[time1][0], "ou 2 para:", GrupoA[time2][0]) 
        resultado = int(input("Insira 1 ou 2: ")) 
 
        if resultado == 1: 
            GrupoA[time1][1] += 3 
            GrupoA[time1][3] += 1 
            GrupoA[time2][5] += 1 
        else: 
            GrupoA[time2][1] += 3 
            GrupoA[time2][3] += 1 
            GrupoA[time1][5] += 1 
 
    else: 
        GrupoA[time1][1] += 1 
        GrupoA[time2][1] += 1 
        GrupoA[time1][4] += 1 
        GrupoA[time2][4] += 1 
 
    print(GrupoA[time1][0]) 
    qnt1 = int(input("Fez quantos gols? ")) 
 
    print(GrupoA[time2][0]) 
    qnt2 = int(input("Fez quantos gols? ")) 
 
    GrupoA[time1][6] += qnt1 
    GrupoA[time2][6] += qnt2 
 
    GrupoA[time2][7] += qnt1 
    GrupoA[time1][7] += qnt2 
 
    GrupoA[time1][8] = GrupoA[time1][6] - GrupoA[time1][7] 
    GrupoA[time2][8] = GrupoA[time2][6] - GrupoA[time2][7] 
 
    if time1 == 0 and time2 == 1: 
        time1 = 2 
        time2 = 3 
    elif time1 == 2 and time2 == 3: 
        time1 = 0 
        time2 = 2 
    elif time1 == 0 and time2 == 2: 
        time1 = 3 
        time2 = 1 
    elif time1 == 3 and time2 == 1: 
        time1 = 0 
        time2 = 3 
    elif time1 == 0 and time2 == 3: 
        time1 = 2 
        time2 = 1 
 
# Grupo B 
time1 = 0 
time2 = 1 
 
for ii in range(6): 
    print("Insira o resultado do jogo:", GrupoB[time1][0], "X", GrupoB[time2][0]) 
 
    empate = input("Foi um empate? S ou N: ") 
 
    if empate.upper() == "N": 
        print("Quem venceu? Digite 1 para:", GrupoB[time1][0], "ou 2 para:", GrupoB[time2][0]) 
        resultado = int(input("Insira 1 ou 2: ")) 
 
        if resultado == 1: 
            GrupoB[time1][1] += 3 
            GrupoB[time1][3] += 1 
            GrupoB[time2][5] += 1 
        else: 
            GrupoB[time2][1] += 3 
            GrupoB[time2][3] += 1 
            GrupoB[time1][5] += 1 
 
    else: 
        GrupoB[time1][1] += 1 
        GrupoB[time2][1] += 1 
        GrupoB[time1][4] += 1 
        GrupoB[time2][4] += 1 
 
    print(GrupoB[time1][0]) 
    qnt1 = int(input("Fez quantos gols? ")) 
 
    print(GrupoB[time2][0]) 
    qnt2 = int(input("Fez quantos gols? ")) 
 
    GrupoB[time1][6] += qnt1 
    GrupoB[time2][6] += qnt2 
 
    GrupoB[time2][7] += qnt1 
    GrupoB[time1][7] += qnt2 
 
    GrupoB[time1][8] = GrupoB[time1][6] - GrupoB[time1][7] 
    GrupoB[time2][8] = GrupoB[time2][6] - GrupoB[time2][7] 
 
    if time1 == 0 and time2 == 1: 
        time1 = 2 
        time2 = 3 
    elif time1 == 2 and time2 == 3: 
        time1 = 0 
        time2 = 2 
    elif time1 == 0 and time2 == 2: 
        time1 = 3 
        time2 = 1 
    elif time1 == 3 and time2 == 1: 
        time1 = 0 
        time2 = 3 
    elif time1 == 0 and time2 == 3: 
        time1 = 2 
        time2 = 1 
 
GrupoA.sort(key=lambda time: time[1], reverse=True) 
GrupoB.sort(key=lambda time: time[1], reverse=True) 
 
print("\nCLASSIFICAÇÃO GRUPO A") 
for linha in GrupoA: 
    print(linha) 
 
print("\nCLASSIFICAÇÃO GRUPO B") 
for linha in GrupoB: 
    print(linha) 
 
print("\nSEMIFINAL 1") 
print(GrupoA[0][0], "x", GrupoB[1][0]) 
 
gols1 = int(input("Quantos gols fez " + GrupoA[0][0] + ": ")) 
gols2 = int(input("Quantos gols fez " + GrupoB[1][0] + ": ")) 
 
if gols1 > gols2: 
    finalista1 = GrupoA[0][0] 
elif gols2 > gols1: 
    finalista1 = GrupoB[1][0] 
else: 
    penaltis = int(input("Empate! Digite 1 ou 2: ")) 
    if penaltis == 1: 
        finalista1 = GrupoA[0][0] 
    else: 
        finalista1 = GrupoB[1][0] 
 
print("\nSEMIFINAL 2") 
print(GrupoB[0][0], "x", GrupoA[1][0]) 
 
gols3 = int(input("Quantos gols fez " + GrupoB[0][0] + ": ")) 
gols4 = int(input("Quantos gols fez " + GrupoA[1][0] + ": ")) 
 
if gols3 > gols4: 
    finalista2 = GrupoB[0][0] 
elif gols4 > gols3: 
    finalista2 = GrupoA[1][0] 
else: 
    penaltis = int(input("Empate! Digite 1 ou 2: ")) 
    if penaltis == 1: 
        finalista2 = GrupoB[0][0] 
    else: 
        finalista2 = GrupoA[1][0] 
 
print("\nFINAL") 
print(finalista1, "x", finalista2) 
 
gols5 = int(input("Quantos gols fez " + finalista1 + ": ")) 
gols6 = int(input("Quantos gols fez " + finalista2 + ": ")) 
 
if gols5 > gols6: 
    campeao = finalista1 
elif gols6 > gols5: 
    campeao = finalista2 
else: 
    penaltis = int(input("Empate! Digite 1 ou 2: ")) 
    if penaltis == 1: 
        campeao = finalista1 
    else: 
        campeao = finalista2 
 
print("\nCAMPEÃO DA COPA") 
print(campeao) 