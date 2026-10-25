def validar_senha(senha):
    """
    Função para validar uma senha.
    
    Args:
        senha (str): A senha a ser validada.

    Returns:
        True se a senha for válida, False caso contrário.
    Regras de validação:
        A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.
    """



    if len(senha) < 8:
        return False
    tem_numero = False
    for c in senha:
        if c.isdigit():
            tem_numero = True
            break
    return tem_numero
while True:
    a = input("Digite uma senha: ")

    if validar_senha(a):
        print("Senha válida")
        break
    else:
        print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")