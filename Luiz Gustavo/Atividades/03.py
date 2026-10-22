def validar_senha(senha):
    if len(senha) < 8:
        return False
    tem_numero = False
    for c in senha:
        if c.isdigit():
            tem_numero = True
            break
    return tem_numero

a = input("Digite uma senha: ")
validar_senha(a)

if validar_senha(a):
    print("Senha válida")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")