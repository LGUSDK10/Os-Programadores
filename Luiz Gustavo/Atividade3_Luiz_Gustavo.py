with open ("neymar.txt", "r", encoding = 'utf-8') as arquivo:
    lista = []
    linhas = arquivo.readlines()
    for i in linhas:
        dados = i.split(' ')
                