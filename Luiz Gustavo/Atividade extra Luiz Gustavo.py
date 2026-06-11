grupoA = []
grupoB = []

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

for i in tabela:
    print(i)