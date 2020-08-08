'''
Esse arquivo terá todos os textos necessários para os titulos dos menus. Além disso,
terá as versões do programa em outros idiomas.
'''

criptografias_disponiveis = {'Cifra de César': ['Apenas letras', 'Vários caracteres'],
                             'Substituição simples': ['Apenas letras (letras mensagem comum)      ', 'Apenas letras (letras mensagem encriptada)     ',
                                                      'Vários caracteres (letras mensagem comum)', 'Vários caracteres (letras mensagem encriptada)'], 
                             'Cifra de Vigenère': ['Apenas letras', 'Vários caracteres']}

dic_criptografias_eng = {'Cifra de César': ['Letters only', 'Several characters'],
                         'Substituição simples': ['Letters only (commom message letters)      ', 'Letters only (cipher message letters)     ',
                                                  'Several characters (commom message letters)', 'Several characters (cipher message letters)'], 
                         'Cifra de Vigenère': ['Letters only', 'Several characters']}              

lista_cifras_port = ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
lista_cifras_ingles = ['Caesar Cipher', 'Substitution cipher', 'Vigenère Cipher']

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
