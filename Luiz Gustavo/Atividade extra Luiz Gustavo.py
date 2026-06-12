grupoA = []
grupoB = []
semi = []

for i in range(4):
    selecao = input("Digite o nome da seleção do grupo A: ")
    grupoA.append([selecao, 0, 0, 0, 0, 0, 0, 0, 0])
print()


for i in range(4):
    selecao = input("Digite o nome da seleção do grupo B: ")
    grupoB.append([selecao, 0, 0, 0, 0, 0, 0, 0, 0])
print()

tabela = [
    ["Seleção", "Pontos", "Jogos", "Vitórias", "Empates", "Derrotas", "Gols marcados", "Gols sofridos", "Saldo de gols"],
    ["Grupo A:"],
    [grupoA[0]],
    [grupoA[1]],
    [grupoA[2]],
    [grupoA[3]],
    ["Grupo B:"],
    [grupoB[0]],
    [grupoB[1]],
    [grupoB[2]],
    [grupoB[3]]
]

print("========================================")
print("Confronto do Grupo A:")

for i in range(3):
    print(f"{grupoA[0][0]} X {grupoA[i+1][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoA[0][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoA[i+1][0]}: "))
    print(f"{grupoA[0][0]} {golsA} X {golsB} {grupoA[i+1][0]}")
    if golsA > golsB:
        grupoA[0][1] += 3
        grupoA[0][2] += 1
        grupoA[0][3] += 1
        grupoA[0][6] += golsA
        grupoA[0][7] += golsB
        grupoA[0][8] += golsA - golsB
        grupoA[i+1][2] += 1
        grupoA[i+1][5] += 1
        grupoA[i+1][6] += golsB
        grupoA[i+1][7] += golsA
        grupoA[i+1][8] += golsB - golsA
    elif golsA < golsB:
        grupoA[i+1][1] += 3
        grupoA[i+1][2] += 1
        grupoA[i+1][3] += 1
        grupoA[i+1][6] += golsB
        grupoA[i+1][7] += golsA
        grupoA[i+1][8] += golsB - golsA
        grupoA[0][2] += 1
        grupoA[0][5] += 1
        grupoA[0][6] += golsA
        grupoA[0][7] += golsB
        grupoA[0][8] += golsA - golsB
    else:
        grupoA[0][1] += 1
        grupoA[0][2] += 1
        grupoA[0][6] += golsA
        grupoA[0][7] += golsB
        grupoA[0][8] += golsA - golsB

        grupoA[i+1][1] += 1
        grupoA[i+1][2] += 1
        grupoA[i+1][6] += golsB
        grupoA[i+1][7] += golsA
        grupoA[i+1][8] += golsB - golsA
print()

for i in range(2):
    print(f"{grupoA[1][0]} X {grupoA[i+2][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoA[1][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoA[i+2][0]}: "))
    print(f"{grupoA[1][0]} {golsA} X {golsB} {grupoA[i+2][0]}")

    if golsA > golsB:
        grupoA[1][1] += 3
        grupoA[1][2] += 1
        grupoA[1][3] += 1
        grupoA[1][6] += golsA
        grupoA[1][7] += golsB
        grupoA[1][8] += golsA - golsB
        grupoA[i+2][2] += 1
        grupoA[i+2][5] += 1
        grupoA[i+2][6] += golsB
        grupoA[i+2][7] += golsA
        grupoA[i+2][8] += golsB - golsA
    elif golsA < golsB:
        grupoA[i+2][1] += 3
        grupoA[i+2][2] += 1
        grupoA[i+2][3] += 1
        grupoA[i+2][6] += golsB
        grupoA[i+2][7] += golsA
        grupoA[i+2][8] += golsB - golsA
        grupoA[1][2] += 1
        grupoA[1][5] += 1
        grupoA[1][6] += golsA
        grupoA[1][7] += golsB
        grupoA[1][8] += golsA - golsB
    else:
        grupoA[1][1] += 1
        grupoA[1][2] += 1
        grupoA[1][6] += golsA
        grupoA[1][7] += golsB
        grupoA[1][8] += golsA - golsB

        grupoA[i+2][1] += 1
        grupoA[i+2][2] += 1
        grupoA[i+2][6] += golsB
        grupoA[i+2][7] += golsA
        grupoA[i+2][8] += golsB - golsA
print()

for i in range(1):
    print(f"{grupoA[2][0]} X {grupoA[i+3][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoA[2][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoA[i+3][0]}: "))
    print(f"{grupoA[2][0]} {golsA} X {golsB} {grupoA[i+3][0]}")

    if golsA > golsB:
        grupoA[2][1] += 3
        grupoA[2][2] += 1
        grupoA[2][3] += 1
        grupoA[2][6] += golsA
        grupoA[2][7] += golsB
        grupoA[2][8] += golsA - golsB
        grupoA[i+3][2] += 1
        grupoA[i+3][5] += 1
        grupoA[i+3][6] += golsB
        grupoA[i+3][7] += golsA
        grupoA[i+3][8] += golsB - golsA
    elif golsA < golsB:
        grupoA[i+3][1] += 3
        grupoA[i+3][2] += 1
        grupoA[i+3][3] += 1
        grupoA[i+3][6] += golsB
        grupoA[i+3][7] += golsA
        grupoA[i+3][8] += golsB - golsA
        grupoA[2][2] += 1
        grupoA[2][5] += 1
        grupoA[2][6] += golsA
        grupoA[2][7] += golsB
        grupoA[2][8] += golsA - golsB
    else:
        grupoA[2][1] += 1
        grupoA[2][2] += 1
        grupoA[2][6] += golsA
        grupoA[2][7] += golsB
        grupoA[2][8] += golsA - golsB

        grupoA[i+3][1] += 1
        grupoA[i+3][2] += 1
        grupoA[i+3][6] += golsB
        grupoA[i+3][7] += golsA
        grupoA[i+3][8] += golsB - golsA
print()

print("========================================")
print("Confronto do Grupo B:")

for i in range(3):
    print(f"{grupoB[0][0]} X {grupoB[i+1][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoB[0][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoB[i+1][0]}: "))
    print(f"{grupoB[0][0]} {golsA} X {golsB} {grupoB[i+1][0]}")
    if golsA > golsB:
        grupoB[0][1] += 3
        grupoB[0][2] += 1
        grupoB[0][3] += 1
        grupoB[0][6] += golsA
        grupoB[0][7] += golsB
        grupoB[0][8] += golsA - golsB
        grupoB[i+1][2] += 1
        grupoB[i+1][5] += 1
        grupoB[i+1][6] += golsB
        grupoB[i+1][7] += golsA
        grupoB[i+1][8] += golsB - golsA
    elif golsA < golsB:
        grupoB[i+1][1] += 3
        grupoB[i+1][2] += 1
        grupoB[i+1][3] += 1
        grupoB[i+1][6] += golsB
        grupoB[i+1][7] += golsA
        grupoB[i+1][8] += golsB - golsA
        grupoB[0][2] += 1
        grupoB[0][5] += 1
        grupoB[0][6] += golsA
        grupoB[0][7] += golsB
        grupoB[0][8] += golsA - golsB
    else:
        grupoB[0][1] += 1
        grupoB[0][2] += 1
        grupoB[0][6] += golsA
        grupoB[0][7] += golsB
        grupoB[0][8] += golsA - golsB

        grupoB[i+1][1] += 1
        grupoB[i+1][2] += 1
        grupoB[i+1][6] += golsB
        grupoB[i+1][7] += golsA
        grupoB[i+1][8] += golsB - golsA
print()

for i in range(2):
    print(f"{grupoB[1][0]} X {grupoB[i+2][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoB[1][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoB[i+2][0]}: "))
    print(f"{grupoB[1][0]} {golsA} X {golsB} {grupoB[i+2][0]}")

    if golsA > golsB:
        grupoB[1][1] += 3
        grupoB[1][2] += 1
        grupoB[1][3] += 1
        grupoB[1][6] += golsA
        grupoB[1][7] += golsB
        grupoB[1][8] += golsA - golsB
        grupoB[i+2][2] += 1
        grupoB[i+2][5] += 1
        grupoB[i+2][6] += golsB
        grupoB[i+2][7] += golsA
        grupoB[i+2][8] += golsB - golsA
    elif golsA < golsB:
        grupoB[i+2][1] += 3
        grupoB[i+2][2] += 1
        grupoB[i+2][3] += 1
        grupoB[i+2][6] += golsB
        grupoB[i+2][7] += golsA
        grupoB[i+2][8] += golsB - golsA
        grupoB[1][2] += 1
        grupoB[1][5] += 1
        grupoB[1][6] += golsA
        grupoB[1][7] += golsB
        grupoB[1][8] += golsA - golsB
    else:
        grupoB[1][1] += 1
        grupoB[1][2] += 1
        grupoB[1][6] += golsA
        grupoB[1][7] += golsB
        grupoB[1][8] += golsA - golsB

        grupoB[i+2][1] += 1
        grupoB[i+2][2] += 1
        grupoB[i+2][6] += golsB
        grupoB[i+2][7] += golsA
        grupoB[i+2][8] += golsB - golsA
print()

for i in range(1):
    print(f"{grupoB[2][0]} X {grupoB[i+3][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoB[2][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoB[i+3][0]}: "))
    print(f"{grupoB[2][0]} {golsA} X {golsB} {grupoB[i+3][0]}")

    if golsA > golsB:
        grupoB[2][1] += 3
        grupoB[2][2] += 1
        grupoB[2][3] += 1
        grupoB[2][6] += golsA
        grupoB[2][7] += golsB
        grupoB[2][8] += golsA - golsB
        grupoB[i+3][2] += 1
        grupoB[i+3][5] += 1
        grupoB[i+3][6] += golsB
        grupoB[i+3][7] += golsA
        grupoB[i+3][8] += golsB - golsA
    elif golsA < golsB:
        grupoB[i+3][1] += 3
        grupoB[i+3][2] += 1
        grupoB[i+3][3] += 1
        grupoB[i+3][6] += golsB
        grupoB[i+3][7] += golsA
        grupoB[i+3][8] += golsB - golsA
        grupoB[2][2] += 1
        grupoB[2][5] += 1
        grupoB[2][6] += golsA
        grupoB[2][7] += golsB
        grupoB[2][8] += golsA - golsB
    else:
        grupoB[2][1] += 1
        grupoB[2][2] += 1
        grupoB[2][6] += golsA
        grupoB[2][7] += golsB
        grupoB[2][8] += golsA - golsB

        grupoB[i+3][1] += 1
        grupoB[i+3][2] += 1
        grupoB[i+3][6] += golsB
        grupoB[i+3][7] += golsA
        grupoB[i+3][8] += golsB - golsA
print()



grupoA_ord = sorted(grupoA, key=lambda row: row[1], reverse=True)
grupoB_ord = sorted(grupoB, key=lambda row: row[1], reverse=True)

print("========================================")
print("Classificação do Grupo A:")
for i in grupoA_ord:
    print(i)
print()
print("Classificação do Grupo B:")
for i in grupoB_ord:
    print(i)
print()

print("========================================")
print("Confronto das Semifinais:")
print(f"{grupoA_ord[0][0]} X {grupoB_ord[1][0]}")
print(f"{grupoB_ord[0][0]} X {grupoA_ord[1][0]}")

print("Quer simular as Semifinais? (s/n)")
r = input()

if r == "s":
    print("Semi lado 1: ")
    print(f"{grupoA_ord[0][0]} X {grupoB_ord[1][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoA_ord[0][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoB_ord[1][0]}: "))
    print(f"{grupoA_ord[0][0]} {golsA} X {golsB} {grupoB_ord[1][0]}")
    if golsA > golsB:
        semi.append(grupoA_ord[0][0])
    elif golsA < golsB:
        semi.append(grupoB_ord[1][0])
    else:
        print("Empate? Vamos para os pênaltis!")
        r = input(f"Quem venceu nos pênaltis? ({grupoA_ord[0][0]}/{grupoB_ord[1][0]}): ")
        if r == grupoA_ord[0][0]:
            semi.append(grupoA_ord[0][0])
        else:
            semi.append(grupoB_ord[1][0])
    print()
    print("Semi lado 2: ")
    print(f"{grupoB_ord[0][0]} X {grupoA_ord[1][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoB_ord[0][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoA_ord[1][0]}: "))
    print(f"{grupoB_ord[0][0]} {golsA} X {golsB} {grupoA_ord[1][0]}")
    if golsA > golsB:
        semi.append(grupoB_ord[0][0])
    elif golsA < golsB:
        semi.append(grupoA_ord[1][0])
    else:
        print("Empate? Vamos para os pênaltis!")
        r = input(f"Quem venceu nos pênaltis? ({grupoB_ord[0][0]}/{grupoA_ord[1][0]}): ")
        if r == grupoB_ord[0][0]:
            semi.append(grupoB_ord[0][0])
        else:
            semi.append(grupoA_ord[1][0])
    print()

    print("========================================")
    print("Confronto da Final:")
    print(f"{semi[0]} X {semi[1]}")
    golsA = int(input(f"Digite o número de gols marcados por {semi[0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {semi[1]}: "))
    print(f"{semi[0]} {golsA} X {golsB} {semi[1]}")
    if golsA > golsB:
        print(f"O campeão é {semi[0]}!")
    elif golsA < golsB:
        print(f"O campeão é {semi[1]}!")
    else:
        print("Empate? Vamos para os pênaltis!")
        r = input(f"Quem venceu nos pênaltis? ({semi[0]}/{semi[1]}): ")
        if r == semi[0]:
            print(f"O campeão é {semi[0]}!")
        else:
            print(f"O campeão é {semi[1]}!")