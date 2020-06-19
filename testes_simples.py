import subst_simples
import cesar
import vigenere
import Cifras.executar


def testar():  # Função que chamará todos os testes de cifras disponiveis.
    print('Iniciando os testes automatizados...')
    print('Aqui serão feitos alguns testes simples...')
    todos_erros = testa_cesar_apenas_letras()
    todos_erros += testa_cesar_varios_caracteres()
    todos_erros += testa_subst_simples_apenas_letras()
    todos_erros += testa_vigenere_apenas_letras()
    todos_erros += testa_vigenere_varios_caracteres()
    if todos_erros == 0:
        separacoes('Nenhum erro encontrado !')
    else:
        separacoes('Total de erros encontrados foi:' + str(todos_erros))


def testa_cesar_apenas_letras():  # Função que testa a cifra de césar.
    separacoes('Cifra de César(apenas letras)')
    dicionario_testes = {'cifra': 'Cifra de César', 'Cifra de César(apenas letras)': True,
                         'Cifra de César(varios caracteres)':False}
    erros = 0
    # Primeiro teste:
    dicionario_testes['chave'] = '1'
    dicionario_testes['mensagem'] = 'abcdefghijklmnopqrstuvwxyz'
    dicionario_testes['mensagem esperada'] = 'bcdefghijklmnopqrstuvwxyza'
    erros += verificar_e_imprimir_testes(dicionario_testes, 1)
    # Segundo teste:
    dicionario_testes['chave'] = '5'
    dicionario_testes['mensagem'] = 'abcdefghijklmnopqrstuvwxyz'
    dicionario_testes['mensagem esperada'] = 'fghijklmnopqrstuvwxyzabcde'
    erros += verificar_e_imprimir_testes(dicionario_testes, 2)
    # Terceiro teste:
    dicionario_testes['chave'] = '7'
    dicionario_testes['mensagem'] = 'Bom dia, Boa tarde, Boa noite!'
    dicionario_testes['mensagem esperada'] = 'Ivt kph, Ivh ahykl, Ivh uvpal!'
    erros += verificar_e_imprimir_testes(dicionario_testes, 3)
    # Quarto teste:
    dicionario_testes['chave'] = '7'
    dicionario_testes['mensagem'] = 'Ivt kph, Ivh ahykl, Ivh uvpal!'
    dicionario_testes['mensagem esperada'] = 'Bom dia, Boa tarde, Boa noite!'
    erros += verificar_e_imprimir_testes(dicionario_testes, 4, modo_traduc=True)
    return erros


def testa_cesar_varios_caracteres():
    separacoes('Cifra de César(vários caracteres)')
    dicionario_testes = {'cifra': 'Cifra de César', 'Cifra de César(apenas letras)': False,
                         'Cifra de César(varios caracteres)':True}
    erros = 0
    # Primeiro teste:
    dicionario_testes['chave'] = '123'
    dicionario_testes['mensagem'] = 'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'
    dicionario_testes['mensagem esperada'] = 'ìĉž½¾½ðĂďž½ĎĒĂ½đďČĀþ½ĉĂđďþĐ½ĀČĊ½þĀĂċđČĐ½đþĊÿƆĊ½Ü½â½ĂĐčþƄČĐ½Ü½óþĊČĐ½đĂĐđþď½þĄČďþ½¾'
    erros += verificar_e_imprimir_testes(dicionario_testes, 1)
    # Segundo teste:
    dicionario_testes['chave'] = '123'
    dicionario_testes['mensagem'] = 'ìĉž½¾½ðĂďž½ĎĒĂ½đďČĀþ½ĉĂđďþĐ½ĀČĊ½þĀĂċđČĐ½đþĊÿƆĊ½Ü½â½ĂĐčþƄČĐ½Ü½óþĊČĐ½đĂĐđþď½þĄČďþ½¾'
    dicionario_testes['mensagem esperada'] = 'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'
    erros += verificar_e_imprimir_testes(dicionario_testes, 2, modo_traduc=True)
    # Terceiro teste:
    dicionario_testes['chave'] = '321'
    dicionario_testes['mensagem'] = 'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'
    dicionario_testes['mensagem esperada'] = 'ƯǈǊǄǏƃƄƃƳǄǕǈǆǈƃǔǘǈƃǈǖǗɄƃǗǘǇǒƃǉǘǑǆǌǒǑǄǑǇǒƃǆǒǕǕǈǗǄǐǈǑǗǈƏƃǙǄǐǒǖƃǙǈǕƃǆǒǐǒƃǒƃǗǈǛǗǒƃǉǌǆǄƃǐǒǙǈǑǇǒƃǐǄǌǖƃǄǌǑǇǄƃƄƄƄ'
    erros += verificar_e_imprimir_testes(dicionario_testes, 3)
    # Quarto teste:
    dicionario_testes['chave'] = '321'
    dicionario_testes['mensagem'] = 'ƯǈǊǄǏƃƄƃƳǄǕǈǆǈƃǔǘǈƃǈǖǗɄƃǗǘǇǒƃǉǘǑǆǌǒǑǄǑǇǒƃǆǒǕǕǈǗǄǐǈǑǗǈƏƃǙǄǐǒǖƃǙǈǕƃǆǒǐǒƃǒƃǗǈǛǗǒƃǉǌǆǄƃǐǒǙǈǑǇǒƃǐǄǌǖƃǄǌǑǇǄƃƄƄƄ'
    dicionario_testes['mensagem esperada'] = 'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'
    erros += verificar_e_imprimir_testes(dicionario_testes, 4, modo_traduc=True)
    return erros
    


def testa_subst_simples_apenas_letras():  # Função que testa a cifra de substituição simples.
    separacoes('Substituição simples(apenas letras)')
    dicionario_testes = {'cifra':'Substituição simples', 'Substituição simples(apenas letras)': True}
    erros = 0
    # Primeiro teste:
    dicionario_testes['chave'] = 'fhizdlmnavgewptubxjrqocsky'
    dicionario_testes['mensagem'] = 'Tudo bem com voce ?'
    dicionario_testes['mensagem esperada'] = 'Rqzt hdw itw otid ?'
    erros += verificar_e_imprimir_testes(dicionario_testes, 1)
    # Segundo teste:
    dicionario_testes['chave'] = 'fhizdlmnavgewptubxjrqocsky'
    dicionario_testes['mensagem'] = 'Rqzt hdw itw otid ?'
    dicionario_testes['mensagem esperada'] = 'Tudo bem com voce ?'
    erros += verificar_e_imprimir_testes(dicionario_testes, 2, modo_traduc=True)
    # Terceiro teste:
    dicionario_testes['chave'] = 'neruzjxpgfabcowvdqyihtslmk'
    dicionario_testes['mensagem'] = 'Por favor, me responda !'
    dicionario_testes['mensagem esperada'] = 'Vwq jntwq, cz qzyvwoun !'
    erros += verificar_e_imprimir_testes(dicionario_testes, 3)
    # Quarto teste:
    dicionario_testes['chave'] = 'neruzjxpgfabcowvdqyihtslmk'
    dicionario_testes['mensagem'] = 'Vwq jntwq, cz qzyvwoun !'
    dicionario_testes['mensagem esperada'] = 'Por favor, me responda !' 
    erros += verificar_e_imprimir_testes(dicionario_testes, 4, modo_traduc=True)
    return erros


def testa_vigenere_apenas_letras():  # Função que testa a cifra de Vigenère.
    separacoes('Cifra de Vigenère(apenas letras)')
    dicionario_testes = {'cifra':'Cifra de Vigenère', 'Cifra de Vigenère(apenas letras)':True,
                         'Cifra de Vigenère (vários caracteres)':False}
    erros = 0
    # Primeiro teste:
    dicionario_testes['chave'] = 'ataque'
    dicionario_testes['mensagem'] = 'Vamos invadir a base deles amanhã !'
    dicionario_testes['mensagem esperada'] = 'Vtmem mnoatcv a uaiy heeei uqaghã !'
    erros += verificar_e_imprimir_testes(dicionario_testes, 1)
    # Segundo teste:
    dicionario_testes['chave'] = 'ataque'
    dicionario_testes['mensagem'] = 'Vtmem mnoatcv a uaiy heeei uqaghã !'
    dicionario_testes['mensagem esperada'] = 'Vamos invadir a base deles amanhã !'
    erros += verificar_e_imprimir_testes(dicionario_testes, 2, modo_traduc=True)
    # Terceiro teste:
    dicionario_testes['chave'] = 'covid'
    dicionario_testes['mensagem'] = 'Cuidado para não se contaminar !'
    dicionario_testes['mensagem esperada'] = 'Eidldfc kiuc bãj ah ecibdowiiu !'
    erros += verificar_e_imprimir_testes(dicionario_testes, 3)
    # Quarto teste:
    dicionario_testes['chave'] = 'covid'
    dicionario_testes['mensagem'] = 'Eidldfc kiuc bãj ah ecibdowiiu !'
    dicionario_testes['mensagem esperada'] = 'Cuidado para não se contaminar !'
    erros += verificar_e_imprimir_testes(dicionario_testes, 4, modo_traduc=True)
    return erros


def testa_vigenere_varios_caracteres():
    separacoes('Cifra de Vigenère (vários caracteres)')
    dicionario_testes = {'cifra':'Cifra de Vigenère', 'Cifra de Vigenère(apenas letras)':False,
                         'Cifra de Vigenère (vários caracteres)':True}
    erros = 0
    # Primeiro teste:
    dicionario_testes['chave'] = 'testando'
    dicionario_testes['mensagem'] = 'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'
    dicionario_testes['mensagem esperada'] = 'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï'
    erros += verificar_e_imprimir_testes(dicionario_testes, 1)
    # Segundo teste:
    dicionario_testes['chave'] = 'testando'
    dicionario_testes['mensagem'] = 'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï'
    dicionario_testes['mensagem esperada'] = 'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'
    erros += verificar_e_imprimir_testes(dicionario_testes, 2, modo_traduc=True)
    # Terceiro teste:
    dicionario_testes['chave'] = 'cháves diférentes!'
    dicionario_testes['mensagem'] = 'Vamos testar agora com uma chave diferente, com espaços e acentos.'
    dicionario_testes['mensagem esperada'] = 'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ'
    erros += verificar_e_imprimir_testes(dicionario_testes, 3)
    # Quarto teste:
    dicionario_testes['chave'] = 'cháves diférentes!'
    dicionario_testes['mensagem'] = 'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ'
    dicionario_testes['mensagem esperada'] = 'Vamos testar agora com uma chave diferente, com espaços e acentos.'
    erros += verificar_e_imprimir_testes(dicionario_testes, 4, modo_traduc=True)
    return erros


def separacoes(cifra):  # Cria uma separação no output gerado.
    print()
    print('----' * 15)
    print('{:^45}'.format(cifra))
    print('----' * 15)
    print()


def verificar_e_imprimir_testes(dic_testes, n_teste, modo_traduc=False):  # Impressões automaticas e testes.
    '''
    Função que verificará e imprimirá os testes feitos pelo programa.
    Param. dic_testes: é um dicionário que contém a chave e a mensagem que devem ser testadas (indexes: chave, mensagem),
    e também apresenta o resultado esperado a ser recebido pelo programa(index: mensagem esperada)
    Param. n_teste: é o número do teste realizado.
    '''
    print(f'Teste {n_teste}:')
    if modo_traduc:
        print('Modo tradução')
    else:
        print('Modo encriptação')
    print(f'chave utilizada = {dic_testes["chave"]}')
    print(f'Mensagem utilizada = {dic_testes["mensagem"]}')
    print(f'Mensagem esperada: {dic_testes["mensagem esperada"]}')
    dic_testes['mensagem computada'] = Cifras.executar.executa_cifra(dic_testes, modo_traducao=modo_traduc)  # Coletar mensagem computada.
    print(f'Mensagem computada: {dic_testes["mensagem computada"]}')
    if dic_testes["mensagem esperada"] == dic_testes["mensagem computada"]:
        # O algoritmo do programa foi bem sucedido e acertou o valor esperado.
        print('Passou!\n')
        return 0
    else:
        # Ocorreu algum erro e o algoritmo não acertou o valor esperado.
        print('Não passou!\n')
        return 1
