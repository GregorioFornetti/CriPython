import subst_simples
import cesar
import vigenere


def testar():  # Função que chamará todos os testes de cifras disponiveis.
    print('Iniciando os testes automatizados...')
    print('Aqui serão feitos alguns testes simples...')
    todos_erros = testa_cesar()
    todos_erros += testa_cesar_varios_caracteres()
    todos_erros += testa_subst_simples()
    todos_erros += testa_vigenere()
    todos_erros += testa_vigenere_varios_caracteres()
    if todos_erros == 0:
        separacoes('Nenhum erro encontrado !')
    else:
        separacoes('Total de erros encontrados foi:' + str(todos_erros))


def testa_cesar():  # Função que testa a cifra de césar.
    erros = 0
    separacoes('Cifra de César(apenas letras)')
    print('Teste 1:')
    erros += imprimir_testes('1',
                             'abcdefghijklmnopqrstuvwxyz',
                             'bcdefghijklmnopqrstuvwxyza',
                              cesar.cifra_de_cesar('1', 'abcdefghijklmnopqrstuvwxyz'))
    print('Teste 2:')
    erros += imprimir_testes('5',
                             'abcdefghijklmnopqrstuvwxyz',
                             'fghijklmnopqrstuvwxyzabcde',
                              cesar.cifra_de_cesar('5', 'abcdefghijklmnopqrstuvwxyz'))
    print('Teste 3:')
    erros += imprimir_testes('7',
                             'Bom dia, Boa tarde, Boa noite!',
                             'Ivt kph, Ivh ahykl, Ivh uvpal!',
                             cesar.cifra_de_cesar('7', 'Bom dia, Boa tarde, Boa noite!'))
    print('Teste 4:')
    erros += imprimir_testes('7 (tradução)',
                             'Ivt kph, Ivh ahykl, Ivh uvpal!',
                             'Bom dia, Boa tarde, Boa noite!',
                             cesar.cifra_de_cesar('7', 'Ivt kph, Ivh ahykl, Ivh uvpal!', modo_traducao=True))
    return erros


def testa_cesar_varios_caracteres():
    erros = 0
    separacoes('Cifra de César(vários caracteres)')
    print('Teste 1:')
    erros += imprimir_testes('123',
                             'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !',
                             'ìĉž½¾½ðĂďž½ĎĒĂ½đďČĀþ½ĉĂđďþĐ½ĀČĊ½þĀĂċđČĐ½đþĊÿƆĊ½Ü½â½ĂĐčþƄČĐ½Ü½óþĊČĐ½đĂĐđþď½þĄČďþ½¾',
                             cesar.cesar_todos_caracteres('123', 'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'))
    print('Teste 2:')
    erros += imprimir_testes('123 (tradução)',
                             'ìĉž½¾½ðĂďž½ĎĒĂ½đďČĀþ½ĉĂđďþĐ½ĀČĊ½þĀĂċđČĐ½đþĊÿƆĊ½Ü½â½ĂĐčþƄČĐ½Ü½óþĊČĐ½đĂĐđþď½þĄČďþ½¾',
                             'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !',
                             cesar.cesar_todos_caracteres('123', 'ìĉž½¾½ðĂďž½ĎĒĂ½đďČĀþ½ĉĂđďþĐ½ĀČĊ½þĀĂċđČĐ½đþĊÿƆĊ½Ü½â½ĂĐčþƄČĐ½Ü½óþĊČĐ½đĂĐđþď½þĄČďþ½¾', modo_traducao=True))
    print('Teste 3:')
    erros += imprimir_testes('321',
                             'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!',
                             'ƯǈǊǄǏƃƄƃƳǄǕǈǆǈƃǔǘǈƃǈǖǗɄƃǗǘǇǒƃǉǘǑǆǌǒǑǄǑǇǒƃǆǒǕǕǈǗǄǐǈǑǗǈƏƃǙǄǐǒǖƃǙǈǕƃǆǒǐǒƃǒƃǗǈǛǗǒƃǉǌǆǄƃǐǒǙǈǑǇǒƃǐǄǌǖƃǄǌǑǇǄƃƄƄƄ',
                             cesar.cesar_todos_caracteres('321', 'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'))
    print('Teste 4:')
    erros += imprimir_testes('321 (tradução)',
                             'ƯǈǊǄǏƃƄƃƳǄǕǈǆǈƃǔǘǈƃǈǖǗɄƃǗǘǇǒƃǉǘǑǆǌǒǑǄǑǇǒƃǆǒǕǕǈǗǄǐǈǑǗǈƏƃǙǄǐǒǖƃǙǈǕƃǆǒǐǒƃǒƃǗǈǛǗǒƃǉǌǆǄƃǐǒǙǈǑǇǒƃǐǄǌǖƃǄǌǑǇǄƃƄƄƄ',
                             'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!',
                             cesar.cesar_todos_caracteres('321', 'ƯǈǊǄǏƃƄƃƳǄǕǈǆǈƃǔǘǈƃǈǖǗɄƃǗǘǇǒƃǉǘǑǆǌǒǑǄǑǇǒƃǆǒǕǕǈǗǄǐǈǑǗǈƏƃǙǄǐǒǖƃǙǈǕƃǆǒǐǒƃǒƃǗǈǛǗǒƃǉǌǆǄƃǐǒǙǈǑǇǒƃǐǄǌǖƃǄǌǑǇǄƃƄƄƄ', modo_traducao=True))
    return erros
    


def testa_subst_simples():  # Função que testa a cifra de substituição simples.
    erros = 0
    separacoes('Substituição simples')
    print('Teste 1:')
    erros += imprimir_testes('fhizdlmnavgewptubxjrqocsky',
                             'Tudo bem com voce ?',
                             'Rqzt hdw itw otid ?',
                              subst_simples.subst_simples('fhizdlmnavgewptubxjrqocsky', 'Tudo bem com voce ?'))
    print('Teste 2:')
    erros += imprimir_testes('fhizdlmnavgewptubxjrqocsky (tradução)',
                             'Rqzt hdw itw otid ?',
                             'Tudo bem com voce ?',
                              subst_simples.subst_simples('fhizdlmnavgewptubxjrqocsky', 'Rqzt hdw itw otid ?', modo_traducao=True))
    print('Teste 3:')
    erros += imprimir_testes('neruzjxpgfabcowvdqyihtslmk',
                             'Por favor, me responda !',
                             'Vwq jntwq, cz qzyvwoun !',
                              subst_simples.subst_simples('neruzjxpgfabcowvdqyihtslmk', 'Por favor, me responda !'))
    print('Teste 4:')
    erros += imprimir_testes('neruzjxpgfabcowvdqyihtslmk (tradução)',
                             'Vwq jntwq, cz qzyvwoun !',
                             'Por favor, me responda !',
                             subst_simples.subst_simples('neruzjxpgfabcowvdqyihtslmk', 'Vwq jntwq, cz qzyvwoun !', modo_traducao=True))

    return erros


def testa_vigenere():  # Função que testa a cifra de Vigenère.
    erros = 0
    separacoes('Cifra de Vigenère')
    print('Teste 1:')
    erros += imprimir_testes('ataque',
                             'Vamos invadir a base deles amanhã !',
                             'Vtmem mnoatcv a uaiy heeei uqaghã !',
                             vigenere.vigenere('ataque', 'Vamos invadir a base deles amanhã !'))
    print('Teste 2:')
    erros += imprimir_testes('ataque (tradução)',
                             'Vtmem mnoatcv a uaiy heeei uqaghã !',
                             'Vamos invadir a base deles amanhã !',
                             vigenere.vigenere('ataque', 'Vtmem mnoatcv a uaiy heeei uqaghã !', modo_traducao=True))
    print('Teste 3:')
    erros += imprimir_testes('covid',
                             'Cuidado para não se contaminar !',
                             'Eidldfc kiuc bãj ah ecibdowiiu !',
                             vigenere.vigenere('covid', 'Cuidado para não se contaminar !'))
    print('Teste 4:')
    erros += imprimir_testes('covid (tradução)',
                             'Eidldfc kiuc bãj ah ecibdowiiu !',
                             'Cuidado para não se contaminar !',
                             vigenere.vigenere('covid', 'Eidldfc kiuc bãj ah ecibdowiiu !', modo_traducao=True))
    return erros


def testa_vigenere_varios_caracteres():
    erros = 0
    separacoes('Cifra de Vigenère (vários caracteres)')
    print('Teste 1:')
    erros += imprimir_testes('testando',
                             'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?',
                             'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï',
                             vigenere.vigenere_varias_letras('testando', 'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'))
    print('Teste 2:')
    erros += imprimir_testes('testando (tradução)',
                             'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï',
                             'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?',
                             vigenere.vigenere_varias_letras('testando', 'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï', modo_traducao=True))
    print('Teste 3:')
    erros += imprimir_testes('cháves diférentes!',
                             'Vamos testar agora com uma chave diferente, com espaços e acentos.',
                             'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ',
                             vigenere.vigenere_varias_letras('cháves diférentes!', 'Vamos testar agora com uma chave diferente, com espaços e acentos.'))
    print('Teste 4:')
    erros += imprimir_testes('cháves diférentes! (tradução)',
                             'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ',
                             'Vamos testar agora com uma chave diferente, com espaços e acentos.',
                             vigenere.vigenere_varias_letras('cháves diférentes!', 'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ', modo_traducao=True))
    return erros


def separacoes(cifra):  # Cria uma separação no output gerado.
    print()
    print('----' * 15)
    print('{:^45}'.format(cifra))
    print('----' * 15)
    print()


def imprimir_testes(chave, mensagem, mensagem_esperada, mensagem_recebida):  # Impressões automaticas e testes.
    '''
    Função que recebe como parâmetros a chave que será usada para o teste, a mensagem que será encriptada/traduzida, a mensagem esperada
    que o programa deve retornar, e a mensagem recebida pelo próprio programa. Se a mensagem esperada for igual a mensagem recebida,
    quer dizer que o programa passou no teste.
    '''
    print(f'chave = {chave}')
    print(f'Mensagem = {mensagem}')
    print(f'Mensagem esperada: {mensagem_esperada}')
    print(f'Mensagem recebida: {mensagem_recebida}')
    if mensagem_esperada == mensagem_recebida:
        print('Passou!')
        return 0
    else:
        print('Não passou!')
        return 1


print(ord('˪'))
print(ord('c'))
print(ord('V'))
print(ord(','))
print(ord('d'))
print(chr(ord(',') + ord('d') + 34))
print(chr((ord('c') + ord('V') + 34)))