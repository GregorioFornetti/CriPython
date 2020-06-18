import Cifras.cifra_de_cesar
import Cifras.subst_simples
import Cifras.cifra_de_vigenere


def executa_cifra(dic_criptografia, modo_traducao):
    '''
    Essa função lerá algumas informações fornecidas pelo usuário e irá executar alguma cifra
    baseada nelas.
    parametro dict_criptografia: contém algumas informações como qual cifra foi escolhida pelo
    usuário e qual foi a mensagem e chave digitada por ele.
    parametro modo_tradução: bool que irá definir se vai ser uma tradução ou uma encriptação.
    '''
    cript_escolhida = dic_criptografia['cifra']
    mensagem = dic_criptografia['mensagem']
    chave = dic_criptografia['chave']
    if cript_escolhida == 'Cifra de César':
        if dic_criptografia['Cifra de César(apenas letras)']:
            return Cifras.cifra_de_cesar.apenas_letras(chave, mensagem, modo_traducao=modo_traducao)
        else:
            return Cifras.cifra_de_cesar.varios_caracteres(chave, mensagem, modo_traducao=modo_traducao)
    if cript_escolhida == 'Substituição simples':
        # Usuário escolheu encriptar/traduzir pela substituiçao simples.
        return Cifras.subst_simples.apenas_letras(chave, mensagem, modo_traducao=modo_traducao)
    if cript_escolhida == 'Cifra de Vigenère':
        if dic_criptografia['Cifra de Vigenère(apenas letras)']:
            return Cifras.cifra_de_vigenere.apenas_letras(chave, mensagem, modo_traducao=modo_traducao)
        else:
            return Cifras.cifra_de_vigenere.varias_letras(chave, mensagem, modo_traducao=modo_traducao)
    return 'Por favor, selecione uma cifra !'
