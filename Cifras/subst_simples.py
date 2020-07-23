
def encriptar_modo_apenas_letras(lista_chaves, mensagem):
    chave = adaptar_chave_modo_apenas_letras(lista_chaves[0], lista_chaves[1])
    return mensagem_nova(chave, mensagem)


def encriptar_modo_varios_caracteres(lista_chaves, mensagem):
    chave = adaptar_chave_modo_varios_caracteres(lista_chaves[0], lista_chaves[1])
    return mensagem_nova(chave, mensagem)


def traduzir_modo_apenas_letras(lista_chaves, mensagem):
    '''
    Para fazer a tradução, basta apenas trocar a ordem das chaves. Isso fará com que as letras 
    da mensagem encriptada sejam trocadas pelas letras mensagem comum.
    '''
    chave = adaptar_chave_modo_apenas_letras(lista_chaves[1], lista_chaves[0])
    return mensagem_nova(chave, mensagem)


def traduzir_modo_varios_caracteres(lista_chaves, mensagem):
    chave = adaptar_chave_modo_varios_caracteres(lista_chaves[1], lista_chaves[0])
    return mensagem_nova(chave, mensagem)


def mensagem_nova(chave, mensagem):
    if not mensagem:
        return 'Mensagem inválida !'
    if chave:
        return criar_mensagem_com_caracteres_trocados(chave, mensagem)
    else:
        return 'Chave inválida !'

def adaptar_chave_modo_varios_caracteres(chave_1, chave_2):  # Criará um dicionário relacionando a chave_1 com a chave_2
    if chave_1 and chave_2 and verifica_caracteres_duplicados(chave_1, chave_2) and len(chave_1) == len(chave_2):
        return cria_chaves_dicionarios(chave_1, chave_2)
    return False


def adaptar_chave_modo_apenas_letras(chave_1, chave_2):  # Criar conversões para caixa baixa e alta.
    if verifica_caracteres_duplicados(chave_1.lower(), chave_2.lower()) and len(chave_1) == len(chave_2) and chave_1.isalpha() and chave_2.isalpha():
        chave_dics = cria_chaves_dicionarios(chave_1.lower(), chave_2.lower())
        chave_dics.update(cria_chaves_dicionarios(chave_1.upper(), chave_2.upper()))
        return chave_dics
    return False


def verifica_caracteres_duplicados(chave_1, chave_2):  
    # Recebe como parâmetro uma lista de chaves, e retorna verdadeiro se nenhuma das chaves contém caracteres repetidos.
    chave_composta = chave_1 + chave_2
    for letra in chave_composta:
        if chave_composta.count(letra) >= 2:
            return False
    return True


def criar_mensagem_com_caracteres_trocados(chave_dics, mensagem):
    nova_mensagem = ''
    for letra in mensagem:
        try:
            nova_mensagem += chave_dics[letra]
        except:
            nova_mensagem += letra
    return nova_mensagem


def cria_chaves_dicionarios(chave_1, chave_2):
    '''
    OBS: É preciso criar duas chaves, pois ocorrerá erros quando um caractere trocado pela chave_2 não é trocado pela chave_1
    Ex com o erro:  chave_1 = a | chave_2 = b | mensagem = ab | mensagem_encriptada = bb | mensagem_traduzida = a
    Ex erro resolvido: chave_1 = a | chave_2 = b | mensagem = ab | mensagem_encriptada = ba | mensagem_traduzida = ab
    Com duas chaves, é possível realizar o processo inverso de procura caso seja necessário.
    '''
    dicionario_chave = dict()
    for index in range(len(chave_1)):
        dicionario_chave[chave_1[index]] = chave_2[index]
        dicionario_chave[chave_2[index]] = chave_1[index]
    return dicionario_chave
