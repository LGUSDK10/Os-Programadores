def enviar_notificacao(tipo: str, conteudo: str) -> str:
    """
    Formata dinamicamente uma mensagem de notificação para exibição no sistema.

    Args:
        tipo: str
            O tipo da notificação a ser exibida (ex.: 'curtida', 'comentario', 'seguidor', 'sistema').
        conteudo: str
            O texto contendo a informação ou mensagem principal da notificação.

    Returns:
        str
            Uma string contendo a notificação inteiramente formatada com prefixos baseados no tipo.

    Formatação da Saída:
        Para tipos reconhecidos: Retorna uma string no formato 
            "[TIPO DA NOTIFICAÇÃO]: Você recebeu uma notificação: [conteúdo]".
        Exemplo ('curtida', 'João curtiu sua foto'): 
            "Você recebeu uma notificação de CURTIDA: João curtiu sua foto"

    Lógica de Validação:
        1. Trata e padroniza as entradas de texto removendo espaços extras.
        2. Garante que nem o tipo nem o conteúdo estejam vazios antes de processar a mensagem.
    """
    if not tipo.strip() or not conteudo.strip():
        raise ValueError("O tipo e o conteúdo da notificação não podem ser vazios.")

    tipo_formatado = tipo.strip().lower()
    conteudo_limpo = conteudo.strip()

    formatos = {
        'curtida': f" Você recebeu uma notificação de CURTIDA: {conteudo_limpo}",
        'comentario': f" Você recebeu um NOVO COMENTÁRIO: {conteudo_limpo}",
        'seguidor': f" Você tem um NOVO SEGUIDOR: {conteudo_limpo}",
        'sistema': f" NOTIFICAÇÃO DO SISTEMA: {conteudo_limpo}"
    }

    if tipo_formatado in formatos:
        return formatos[tipo_formatado]
    else:
        return f" Você recebeu uma notificação de {tipo_formatado.upper()}: {conteudo_limpo}"

a = input("Digite o tipo de notificação (ex: curtida, comentario, seguidor, sistema): ")
b = input("Digite o conteúdo da notificação: ")
print(enviar_notificacao(a, b))