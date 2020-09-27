'''
Esse arquivo terá todos os textos necessários para os titulos/textos dos menus. Além disso,
terá as versões do programa em outros idiomas.
'''
criptografias_disponiveis = {'Cifra de César': ['Apenas letras', 'Vários caracteres'],
                             'Substituição simples': ['Apenas letras (letras mensagem comum)      ', 'Apenas letras (letras mensagem encriptada)     ',
                                                      'Vários caracteres (letras mensagem comum)', 'Vários caracteres (letras mensagem encriptada)'], 
                             'Cifra de Vigenère': ['Apenas letras', 'Vários caracteres']}
dic_criptografias_eng = {'Cifra de César': ['Letters only', 'Several characters'],
                         'Substituição simples': ['Letters only (plaintext letters)      ', 'Letters only (ciphertext letters)     ',
                                                  'Several characters (plaintext letters)', 'Several characters (ciphertext letters)'], 
                         'Cifra de Vigenère': ['Letters only', 'Several characters']}
import banco_de_dados
idioma = banco_de_dados.idioma_configurado


def retorna_menu_opcoes():
    if idioma == 'Portugues':
        return {'titulo': 'Crypythongraphy: Opções',
                'opcao temas': 'Temas:',
                'opcao idiomas': 'Idiomas:',
                'cifras': 'Cifras:',
                'modos': criptografias_disponiveis,
                'chaves padroes': 'Chaves padrões cifras',
                'retornar': 'Retornar',
                'aplicar': 'Aplicar',
                'ajuda': 'Ajuda'}
    else:
        return {'titulo': 'Crypythongraphy: Options',
                'opcao temas': 'Themes:',
                'opcao idiomas': 'Languages:',
                'cifras': 'Ciphers:',
                'modos': dic_criptografias_eng ,
                'chaves padroes': 'Default keys',
                'retornar': 'Return',
                'aplicar': 'Apply',
                'ajuda': 'Help'}


def retorna_mensagem_temas(tema):
    if idioma == 'Portugues':
        return retorna_mensagem_com_bordas(f'Novo tema: "{tema}" definido com sucesso !', 127) + '\n'
    else:
        return retorna_mensagem_com_bordas(f'New theme: "{tema}" successfully applied !', 127) + '\n'


def retorna_mensagem_idioma(novo_idioma):
    if idioma == 'Portugues':
        return retorna_mensagem_com_bordas(f'Novo idioma: "{novo_idioma}" definido com sucesso !', 127) + '\n'
    else:
        return retorna_mensagem_com_bordas(f'New language: "{novo_idioma}" successfully applied !', 127) + '\n'


def retorna_mensagem_menu_opcoes(erro=False):  # Texto mostrado ao mudar alguma config. Deve mudar o idioma dessas mensagem também...
    if idioma == 'Portugues':
        mensagem = retorna_mensagem_com_bordas('Chave padrão "{}" salva com sucesso !', 127) + '\n'
        if erro:
            mensagem = retorna_mensagem_com_bordas('Erro: não foi possível salvar a chave padrão: {}.\nA chave digitada não é válida !\nPara verificar as chaves possiveis, clique em "ajuda".', 127) + '\n'
        return {'Cifra de César-Apenas letras': mensagem.format('Cifra de César-Apenas letras'),
                'Cifra de César-Vários caracteres': mensagem.format('Cifra de César-Vários caracteres'),
                'Substituição simples-Apenas letras (letras mensagem comum)': mensagem.format('Substituição simples-Apenas letras (letras mensagem comum)'),
                'Substituição simples-Apenas letras (letras mensagem encriptada)':mensagem.format('Substituição simples-Apenas letras (letras mensagem encriptada)'),
                'Substituição simples-Vários caracteres (letras mensagem comum)':mensagem.format('Substituição simples-Vários caracteres (letras mensagem comum)'),
                'Substituição simples-Vários caracteres (letras mensagem encriptada)': mensagem.format('Substituição simples-Vários caracteres (letras mensagem encriptada)'),
                'Cifra de Vigenère-Apenas letras': mensagem.format('Cifra de Vigenère-Apenas letras'),
                'Cifra de Vigenère-Vários caracteres':mensagem.format('Cifra de Vigenère-Vários caracteres')}
    else:
        mensagem = retorna_mensagem_com_bordas('Default key "{}" successfully saved !', 127) + '\n'
        if erro:
            mensagem = retorna_mensagem_com_bordas('Error: it was not possible to save the key: {}.\nThe key is not valid !', 127) + '\n'
        return {'Cifra de César-Apenas letras': mensagem.format('Caesar Cipher-Letters only'),
                'Cifra de César-Vários caracteres': mensagem.format('Caesar Cipher-Several characters'),
                'Substituição simples-Apenas letras (letras mensagem comum)': mensagem.format('Substituição simples-Letters only (plaintext)'),
                'Substituição simples-Apenas letras (letras mensagem encriptada)':mensagem.format('Substituição simples-Letters only (ciphertext)'),
                'Substituição simples-Vários caracteres (letras mensagem comum)':mensagem.format('Substituição simples-Several characters (plaintext)'),
                'Substituição simples-Vários caracteres (letras mensagem encriptada)': mensagem.format('Substituição simples-Several characters (ciphertext)'),
                'Cifra de Vigenère-Apenas letras': mensagem.format('Vigenère Cipher-Letters only'),
                'Cifra de Vigenère-Vários caracteres':mensagem.format('Vigenère Cipher-Several characters')}


def retorna_menu_principal():
    if idioma == 'Portugues':
        return {'titulo': 'Cripythongraphy: Tela principal',
                'opcao 1': '1- Criar mensagem criptografada',
                'opcao 2': '2- Traduzir mensagem criptografada',
                'opcao 3': '3- Utilitários',
                'opcao 4': '4- Opções',
                'opcao 5': '5- Ajuda',
                'opcao 6': '6- Finalizar programa'}
    else:
        return {'titulo': 'Cripythongraphy: Main screen',
                'opcao 1': '1- Create ciphertext',
                'opcao 2': '2- Translate ciphertext',
                'opcao 3': '3- Utilities',
                'opcao 4': '4- Options',
                'opcao 5': '5- Help',
                'opcao 6': '6- Close program'}


def retorna_lista_cifras(coletar_port=False):  # As vezes vai ser necessário coletar essa lista em port independente do idioma configurado.
    if idioma == 'Portugues' or coletar_port:
        return ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère', 'Bases numéricas', 'Base 64']
    else:
        return ['Caesar Cipher', 'Substitution cipher', 'Vigenère Cipher', 'Numeral systems', 'Base 64']


def retorna_lista_cifras_com_chaves():
    if idioma == 'Portugues':
        return ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
    else:
        return ['Caesar Cipher', 'Substitution cipher', 'Vigenère Cipher']


def retorna_lista_utilitarios(coletar_port=False):
    if idioma == 'Portugues' or coletar_port:
        return ['Força bruta César', 'Adivinhador César']
    else:
        return ['Brute force Caesar', 'Caesar guess']


def retorna_menu_encript_traduc_utilitarios():
    if idioma == 'Portugues':
        return {'Cripythongraphy: Encriptação': 'Cripythongraphy: Encriptação',
                'Cripythongraphy: Tradução': 'Cripythongraphy: Tradução',
                'Cripythongraphy: Utilitários': 'Cripythongraphy: Utilitários',
                'Retornar': 'Retornar'}
    else:
        return {'Cripythongraphy: Encriptação': 'Cripythongraphy: Encrypt',
                'Cripythongraphy: Tradução': 'Cripythongraphy: Translation',
                'Cripythongraphy: Utilitários': 'Cripythongraphy: Utilities',
                'Retornar': 'Return'}


def retorna_menus_cifras():
    if idioma == 'Portugues':
        return {'Cifra de César (encriptação)': 'Cifra de César (encriptação)',
                'Cifra de César (tradução)': 'Cifra de César (tradução)',
                'Substituição simples (encriptação)': 'Substituição simples (encriptação)',
                'Substituição simples (tradução)': 'Substituição simples (tradução)',
                'Cifra de Vigenère (encriptação)': 'Cifra de Vigenère (encriptação)',
                'Cifra de Vigenère (tradução)': 'Cifra de Vigenère (tradução)',
                'Bases numéricas (encriptação)': 'Bases numéricas (encriptação)',
                'Bases numéricas (tradução)': 'Bases numéricas (tradução)',
                'Base 64 (encriptação)': 'Base 64 (encriptação)',
                'Base 64 (tradução)': 'Base 64 (tradução)',
                'Opções': 'Opções:',
                'Chave': 'Chave:',
                'Mensagem encriptada': 'Mensagem encriptada:',
                'Mensagem traduzida': 'Mensagem traduzida:',
                'Mensagem': 'Mensagem:',
                'Encriptar': 'Encriptar',
                'Encriptar com chave padrão': 'Encriptar com chave padrão',
                'Traduzir': 'Traduzir',
                'Traduzir com chave padrão': 'Traduzir com chave padrão',
                'Abrir guia cifra': 'Abrir guia cifra',
                'Limpar tela': 'Limpar tela',
                'Retornar': 'Retornar'}
    else:
        return {'Cifra de César (encriptação)': 'Caesar Cipher (encrypt)',
                'Cifra de César (tradução)': 'Caesar Cipher (translation)',
                'Substituição simples (encriptação)': 'Substitution cipher (encrypt)',
                'Substituição simples (tradução)': 'Substitution cipher (translation)',
                'Cifra de Vigenère (encriptação)': 'Vigenère Cipher (encrypt)',
                'Cifra de Vigenère (tradução)': 'Vigenère Cipher (translation)',
                'Bases numéricas (encriptação)': 'Numeral systems (encrypt)',
                'Bases numéricas (tradução)': 'Numeral systems (translation)',
                'Base 64 (encriptação)': 'Base 64 (encrypt)',
                'Base 64 (tradução)': 'Base 64 (translation)',
                'Opções': 'Options:',
                'Chave': 'Key:',
                'Mensagem encriptada': 'Ciphertext:',
                'Mensagem traduzida': 'Plaintext:',
                'Mensagem': 'Text:',
                'Encriptar': 'Encrypt',
                'Encriptar com chave padrão': 'Encrypt with default key',
                'Traduzir': 'Translate',
                'Traduzir com chave padrão': 'Translate with default key',
                'Abrir guia cifra': 'Open wiki',
                'Limpar tela': 'Clean output',
                'Retornar': 'Return'}


def retorna_opcoes_cifras():
    if idioma == 'Portugues':
        return {'Apenas letras': 'Apenas letras',
                'Vários caracteres': 'Vários caracteres',
                'Binário': 'Binário',
                'Octal': 'Octal',
                'Decimal': 'Decimal',
                'Hexadecimal': 'Hexadecimal'}
    else:
        return {'Apenas letras': 'Only letters',
                'Vários caracteres': 'Several characters',
                'Binário': 'Binary',
                'Octal': 'Octal',
                'Decimal': 'Decimal',
                'Hexadecimal': 'Hexadecimal'}


def retorna_lista_subst_simples():
    if idioma == 'Portugues':
        return ['Letras mensagem comum:    ', 'Letras mensagem encriptada:']
    else:
        return ['Plaintext letters:  ', 'Ciphertext letters:']


def retorna_menu_utilitario():
    if idioma == 'Portugues':
        return {'Força bruta César': 'Força bruta César',
                'Adivinhador César': 'Adivinhador César',
                'Mensagem Força bruta César':'''
                Escolha uma opção e escreva uma mensagem encriptada pela cifra de César.
                O programa testará todas as chaves possíveis!
                OBS: dependendo do texto colocado, esse processo pode ser demorado''',

                'Mensagem Adivinhador César':'''
                Escolha uma opção e escreva uma mensagem encriptada pela cifra de César.
                O programa tentará adivinhar qual é a mensagem traduzida !
                OBS: dependendo do texto, esse processo pode levar bastante tempo !''',

                'Opções': 'Opções:',
                'Mensagem encriptada': 'Mensagem encriptada:',
                'Executar': 'Executar',
                'Abrir wiki': 'Abrir wiki',
                'Limpar tela': 'Limpar tela',
                'Retornar': 'Retornar'}
    else:
        return {'Força bruta César': 'Brute force Caesar',
                'Adivinhador César': 'Caesar guess',
                'Mensagem Força bruta César':'''
                Choose an option and write a text encrypted by the Caesar Cipher.
                The program will test all the possible keys !
                Depending on the text, this process can be slow''',

                'Mensagem Adivinhador César':'''
                Choose an option and write a text encrypted by the Caesar Cipher.
                The program will try to translate the text without the key !
                Depending on the text, this process can be slow''',
                
                'Opções': 'Options:',
                'Mensagem encriptada': 'Ciphertext:',
                'Executar': 'Execute',
                'Abrir wiki': 'Open wiki',
                'Limpar tela': 'Clean screen',
                'Retornar': 'Return'}


def retorna_frequencia_letras(idioma_teste=''):
    dic_freq_port = {'a':14.63, 'e':12.57, 'o':10.73, 's':7.81, 'r':6.53, 'i':6.18, 'n':5.05, 'd':4.99,
                     'm':4.74, 'u':4.63, 't':4.34, 'c':3.88, 'l':2.78, 'p':2.52, 'v':1.67, 'g':1.3,
                     'h':1.28, 'q':1.20, 'b':1.04, 'f':1.02, 'z':0.47, 'j':0.4, 'x':0.21, 'k':0.02,
                     'y':0.01, 'w':0.01}
    dic_freq_eng = {'a':8.16, 'b':1.49, 'c':2.78, 'd':4.25, 'e':12.72, 'f':2.22, 'g':2.01, 'h': 6.09,
                    'i':6.96, 'j':0.15, 'k':0.77, 'l':4.02, 'm':2.40, 'n':6.74, 'o':7.50, 'p':1.92,
                    'q':0.09, 'r':5.98, 's':6.32, 't':9.05, 'u':2.75, 'v':0.97, 'w':2.36, 'x':0.15,
                    'y':1.97, 'z':0.07}

    if idioma_teste:
        if idioma_teste == 'Portugues':
            return dic_freq_port
        else:
            return dic_freq_eng
    else:
        if idioma == 'Portugues':
            return dic_freq_port
        else:
            return dic_freq_eng


def retorna_erro_mensagem():
    if idioma == 'Portugues':
        return 'Erro: Mensagem inválida !'
    else:
        return 'Error: Invalid message !'


def retorna_erro_chave():
    if idioma == 'Portugues':
        return 'Erro: Chave inválida !\nPara verificar as chaves válidas, clique em "abrir guia cifra"\ne procure o tópico "chaves válidas" da sua opção de cifra'
    else:
        return 'Error: Invalid key !\nTo verify the available keys, click on "open wiki"\nand search for the topic "chaves válidas" of your cipher option'


def retorna_erro_chave_padrao():
    if idioma == 'Portugues':
        return "Você ainda não definiu uma chave padrão para essa cifra !\nVá para o menu principal e depois em opções e defina uma !"
    else:
        return "You havent defined a default key for this cipher yet !\nGo to the options menu and define one !"


def retorna_mensagens_forca_bruta_cesar(chave, mensagem_traduzida):
    if idioma == 'Portugues':
        return  retorna_mensagem_com_bordas(f'''
Testando chave: {chave}
Mensagem traduzida: {mensagem_traduzida}
''', 127)
    else:
        return  retorna_mensagem_com_bordas(f'''
Testing key: {chave}
Translated message: {mensagem_traduzida}
''', 127)

def retorna_mensagens_adivinhador_cesar(melhor_mensagem, chave_mensagem):
    if idioma == 'Portugues':
        return  retorna_mensagem_com_bordas(f'''
Após alguns cálculos, a mensagem traduzida com maior probabilidade de ser correta é: {melhor_mensagem}\n
E a chave utilizada para essa tradução foi: {chave_mensagem}                                      
''', 127)
    else:
        return retorna_mensagem_com_bordas(f'''
After some calculations, the translated message with the best probability of being correct is: {melhor_mensagem}\n
And the utilized key was: {chave_mensagem}
''', 127)

def retorna_mensagem_com_bordas(mensagem, tamanho):
    return '#' + '-' * tamanho + '#\n' + mensagem + '\n#' + '-' * tamanho + '#\n'

def atualizar_idioma(idioma_configurado):
    global idioma
    idioma = idioma_configurado