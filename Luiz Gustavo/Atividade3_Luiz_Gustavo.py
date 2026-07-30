with open("texto.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
texto = texto.replace("NEYMAR ", "")
texto = texto.replace(" NEYMAR", "")

with open("texto_corrigido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)