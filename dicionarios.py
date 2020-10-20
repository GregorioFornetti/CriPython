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
                'restaurar': 'Restaurar configurações',
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
                'restaurar': 'Reset settings',
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
        return ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère', 'Bases numéricas', 'UTF-8', 'Base 64']
    else:
        return ['Caesar Cipher', 'Substitution cipher', 'Vigenère Cipher', 'Numeral systems', 'UTF-8', 'Base 64']


def retorna_lista_cifras_com_chaves():
    if idioma == 'Portugues':
        return ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
    else:
        return ['Caesar Cipher', 'Substitution cipher', 'Vigenère Cipher']


def retorna_lista_utilitarios(coletar_port=False):
    if idioma == 'Portugues' or coletar_port:
        return ['Força bruta César', 'Adivinhador César', 'Conversor bases numéricas', 'Codificador de arquivos para base64',
                'Decodificador de base64 para arquivos']
    else:
        return ['Brute force Caesar', 'Caesar guess',  'Numeral systems conversor', 'File encoding to base64',
                'Base64 text decoding to file']


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
        return {'Cifra de César': 'Cifra de César',
                'Substituição simples': 'Substituição simples',
                'Cifra de Vigenère': 'Cifra de Vigenère',
                'Bases numéricas': 'Bases numéricas',
                'UTF-8': 'UTF-8',
                'Base 64': 'Base 64',
                'encriptação': '(encriptação)',
                'tradução': '(tradução)',
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
        return {'Cifra de César': 'Caesar Cipher',
                'Substituição simples': 'Substitution cipher',
                'Cifra de Vigenère': 'Vigenère Cipher',
                'Bases numéricas': 'Numeral systems',
                'UTF-8': 'UTF-8',
                'Base 64': 'Base 64',
                'encriptação': '(encrypt)',
                'tradução': '(translation)',
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
                'Conversor bases numéricas': 'Conversor bases numéricas',
                'Encoding base64': 'Codificador de arquivos para base64',
                'Decoding base64': 'Decodificador de base64 para arquivos',

                'Mensagem Força bruta César':'''
                Escolha uma opção e escreva uma mensagem encriptada pela cifra de César.
                O programa testará todas as chaves possíveis!
                OBS: dependendo do texto colocado, esse processo pode ser demorado''',

                'Mensagem Adivinhador César':'''
                Escolha uma opção e escreva uma mensagem encriptada pela cifra de César.
                O programa tentará adivinhar qual é a mensagem traduzida !
                OBS: dependendo do texto, esse processo pode levar bastante tempo !''',

                'Mensagem conversor bases numéricas':'''
                Diferente da cifra de "bases numéricas", aqui você fará as conversões de uma
                base númerica para outra (ao invés de converter o UNICODE de um texto para uma
                base numérica).''',

                'Mensagem Encoding base64': '''
                Clique em "selecionar arquivo" e escolha um arquivo para converter, depois clique em
                "Salvar como..." e escolha um nome e um local para salvar o arquivo com o código base
                64. OBS: é recomendado a utilização da extensão ".txt" para salvar o arquivo.''',

                'Mensagem Decoding base64':'''
                Clique em "selecionar arquivo" e escolha um arquivo com o código base 64 a ser convertido,
                escolha um local, nome e extensão do arquivo clicando em "salvar como". 
                Ao clicar em executar, o seu texto base64 será convertido
                para um arquivo. OBS: se você digitar um código base64 inválido ou escolher um formato
                inválido, isso resultará em um arquivo corrompido.
                ''',

                'Opções': 'Opções:',
                'Mensagem encriptada': 'Mensagem encriptada:',
                'Executar': 'Executar',
                'Converter de': 'Converter de',
                'Para': 'Para:',
                'Numero': 'Numero:',
                'Codigo base64': 'Texto base64:',
                'salvar como': 'Salvar como...',
                'pesquisar': 'Selecionar arquivo',
                'sem arquivo': 'Nenhum arquivo foi selecionado ainda !',
                'Abrir wiki': 'Abrir wiki',
                'Limpar tela': 'Limpar tela',
                'Retornar': 'Retornar'}
    else:
        return {'Força bruta César': 'Brute force Caesar',
                'Adivinhador César': 'Caesar guess',
                'Conversor bases numéricas': 'Numeral systems conversor',
                'Encoding base64': 'File encoding to base64',
                'Decoding base64': 'Base64 text decoding to file',

                'Mensagem Força bruta César': '''
                Choose an option and write a text encrypted by the Caesar Cipher.
                The program will test all the possible keys !
                Depending on the text, this process can be slow''',

                'Mensagem Adivinhador César':'''
                Choose an option and write a text encrypted by the Caesar Cipher.
                The program will try to translate the text without the key !
                Depending on the text, this process can be slow''',

                'Mensagem conversor bases numéricas':'''
                Unlike the "Numeral systems" cipher, here you will make the conversions
                of a numeral system to another instead of converting the text UNICODE values
                to another numeral system.''',

                'Mensagem Encoding base64': '''
                Click in "select file" and choose a file to convert and click in "Save as..."
                to choose a name and place to save the base64 encoded text. NOTE: it's recomended
                to use the ".txt" extension to save the file.''',

                'Mensagem Decoding base64': '''
                Click in "Select file" and choose a base64 text file and click in "Save as" 
                and choose a folder, name and extensionof the file. After clicking
                the "execute" button, the base64 text will be decoded to
                a file. NOTE: if you enter an invalid base64 code or choose a 
                invalid format, this will result in a corrupted file.''',
                
                'Opções': 'Options:',
                'Converter de': 'Convert from',
                'Para': 'To:',
                'Numero': 'Number:',
                'Codigo base64': 'Base64 text:',
                'pesquisar': 'Select file',
                'salvar como': 'Save as...',
                'pesquisar': 'Select file',
                'sem arquivo': 'No file have been selected yet!',
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

def retorna_erro_numero_invalido():
    if idioma == 'Portugues':
        return 'Número inválido'
    else:
        return 'Invalid number'

def retorna_erro_arquivo():
    if idioma == 'Portugues':
        return 'Arquivo não selecionado ou inválido !'
    else:
        return 'Not selected or invalid file !'

def retorna_mensagem_sucesso_salvar():
    if idioma == 'Portugues':
        return 'Arquivo salvo com sucesso!'
    else:
        return 'File succesfully saved!'

def retorna_mensagem_erro_salvar():
    if idioma == 'Portugues':
        return 'ERRO: Não foi possível salvar o arquivo!'
    else:
        return 'ERROR: the file could not be saved!'


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