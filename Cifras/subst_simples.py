import valores


def executar_modo_varios_caracteres(chave_1, chave_2, mensagem):  # Função que traduz/encripta através da "substituição simples".
    chave = adaptar_chave_modo_varios_caracteres(chave_1, chave_2)
    if chave:
        return criar_mensagem_com_caracteres_trocados(chave, mensagem)
    else:
        return 'Chave inválida !'


def executar_modo_apenas_letras(chave_1, chave_2, mensagem):
    chave = adaptar_chave_modo_apenas_letras(chave_1, chave_2)
    if chave:
        return criar_mensagem_com_caracteres_trocados(chave, mensagem)
    else:
        return 'Chave inválida !'


def adaptar_chave_modo_varios_caracteres(chave_1, chave_2):  # Adaptará as chaves fornecidas para um dicionário.
    if verifica_caracteres_duplicados([chave_1, chave_2]) and len(chave_1) == len(chave_2):
        return cria_chave_dicionario(chave_1, chave_2)
    return False


def adaptar_chave_modo_apenas_letras(chave_1, chave_2):
    if verifica_caracteres_duplicados([chave_1, chave_2]) and len(chave_1) == len(chave_2) and chave_1.isalpha() and chave_2.isalpha():
        chave_dic = cria_chave_dicionario(chave_1.lower(), chave_2.lower())
        chave_dic.update(cria_chave_dicionario(chave_1.upper(), chave_2.upper()))
        return chave_dic
    return False        


def verifica_caracteres_duplicados(lista_chaves):  
    # Recebe como parâmetro uma lista de chaves, e retorna verdadeiro se nenhuma das chaves contém caracteres repetidos.
    for chave in lista_chaves:
        chave = chave.lower()
        for char in chave:
            if chave.count(char) >= 2:
                return False
    return True


def criar_mensagem_com_caracteres_trocados(chave_dic, mensagem):
    nova_mensagem = ''
    for letra in mensagem:
        try:
            nova_mensagem += chave_dic[letra]
        except:
            nova_mensagem += letra
    return nova_mensagem


def cria_chave_dicionario(chave_1, chave_2):
    dicionario_chave = dict()
    for index in range(len(chave_1)):
        dicionario_chave[chave_1[index]] = chave_2[index]
    return dicionario_chave


