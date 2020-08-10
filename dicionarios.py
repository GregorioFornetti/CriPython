'''
Esse arquivo terá todos os textos necessários para os titulos dos menus. Além disso,
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


def retorna_menu_opcoes(idioma):
    if idioma == 'Portugues':
        return {'titulo': 'Crypythongraphy: Opções',
                'opcao temas': 'Temas:',
                'opcao idiomas': 'Idiomas:',
                'cifras': 'Cifras:',
                'modos': criptografias_disponiveis,
                'chaves padroes': 'Chaves padrões cifras',
                'retornar': 'Retornar',
                'aplicar': 'Aplicar'}
    else:
        return {'titulo': 'Crypythongraphy: Options',
                'opcao temas': 'Themes:',
                'opcao idiomas': 'Languages:',
                'cifras': 'Ciphers:',
                'modos': dic_criptografias_eng ,
                'chaves padroes': 'Default keys',
                'retornar': 'Return',
                'aplicar': 'Apply'}


def retorna_mensagem_menu_opcoes(idioma, erro=False):  # Texto mostrado ao mudar alguma config. Deve mudar o idioma dessas mensagem também...
    if idioma == 'Portugues':
        mensagem = 'Chave padrão "{}" salva com sucesso !\n\n'
        if erro:
            mensagem = 'Erro: não foi possível salvar a chave padrão: {}.\nA chave digitada não é válida !\nPara verificar as chaves possiveis, clique em "ajuda".\n\n'
        return {'Cifra de César-Apenas letras': mensagem.format('Cifra de César-Apenas letras'),
                'Cifra de César-Vários caracteres': mensagem.format('Cifra de César-Vários caracteres'),
                'Substituição simples-Apenas letras (letras mensagem comum)': mensagem.format('Substituição simples-Apenas letras (letras mensagem comum)'),
                'Substituição simples-Apenas letras (letras mensagem encriptada)':mensagem.format('Substituição simples-Apenas letras (letras mensagem encriptada)'),
                'Substituição simples-Vários caracteres (letras mensagem comum)':mensagem.format('Substituição simples-Vários caracteres (letras mensagem comum)'),
                'Substituição simples-Vários caracteres (letras mensagem encriptada)': mensagem.format('Substituição simples-Vários caracteres (letras mensagem encriptada)'),
                'Cifra de Vigenère-Apenas letras': mensagem.format('Cifra de Vigenère-Apenas letras'),
                'Cifra de Vigenère-Vários caracteres':mensagem.format('Cifra de Vigenère-Vários caracteres')}
    else:
        mensagem = 'Default key "{}" successfully saved !\n\n'
        if erro:
            mensagem = 'Error: it was not possible to save the key: {}.\nThe key is not valid !\n\n'
        return {'Cifra de César-Apenas letras': mensagem.format('Caesar Cipher-Letters only'),
                'Cifra de César-Vários caracteres': mensagem.format('Caesar Cipher-Several characters'),
                'Substituição simples-Apenas letras (letras mensagem comum)': mensagem.format('Substituição simples-Letters only (plaintext)'),
                'Substituição simples-Apenas letras (letras mensagem encriptada)':mensagem.format('Substituição simples-Letters only (ciphertext)'),
                'Substituição simples-Vários caracteres (letras mensagem comum)':mensagem.format('Substituição simples-Several characters (plaintext)'),
                'Substituição simples-Vários caracteres (letras mensagem encriptada)': mensagem.format('Substituição simples-Several characters (ciphertext)'),
                'Cifra de Vigenère-Apenas letras': mensagem.format('Vigenère Cipher-Letters only'),
                'Cifra de Vigenère-Vários caracteres':mensagem.format('Vigenère Cipher-Several characters')}


def retorna_menu_principal(idioma):
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


def retorna_lista_cifras(idioma):
    if idioma == 'Portugues':
        return ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
    else:
        return ['Caesar Cipher', 'Substitution cipher', 'Vigenère Cipher']


def retorna_lista_utilitarios(idioma):
    if idioma == 'Portugues':
        return ['Força bruta César', 'Adivinhador César']
    else:
        return ['Brute force Caesar', 'Caesar guess']


def retorna_menu_encript_traduc_utilitarios(idioma):
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


def retorna_menus_cifras(idioma):
    if idioma == 'Portugues':
        return {'Cifra de César (encriptação)': 'Cifra de César (encriptação)',
                'Cifra de César (tradução)': 'Cifra de César (tradução)',
                'Substituição simples (encriptação)': 'Substituição simples (encriptação)',
                'Substituição simples (tradução)': 'Substituição simples (tradução)',
                'Cifra de Vigenère (encriptação)': 'Cifra de Vigenère (encriptação)',
                'Cifra de Vigenère (tradução)': 'Cifra de Vigenère (tradução)',
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


def retorna_opcoes_cifras(idioma):
    if idioma == 'Portugues':
        return {'Apenas letras': 'Apenas letras',
                'Vários caracteres': 'Vários caracteres'}
    else:
        return {'Apenas letras': 'Only letters',
                'Vários caracteres': 'Several characters'}


def retorna_lista_subst_simples(idioma):
    if idioma == 'Portugues':
        return ['Letras mensagem comum:    ', 'Letras mensagem encriptada:']
    else:
        return ['Plaintext letters:  ', 'Ciphertext letters:']


def retorna_menu_utilitario(idioma):
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
