for i in range(3):
    print(f"{grupoA[0][0]} X {grupoA[i+1][0]}")
    golsA = int(input(f"Digite o número de gols marcados por {grupoA[0][0]}: "))
    golsB = int(input(f"Digite o número de gols marcados por {grupoA[i+1][0]}: "))
    print(f"{grupoA[0][0]} {golsA} X {golsB} {grupoA[i+1][0]}")