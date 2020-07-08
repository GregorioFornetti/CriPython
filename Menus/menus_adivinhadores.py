import PySimpleGUI as sg
import Menus
import Adivinhadores.forca_bruta_cesar as forca_bruta_cesar
import Adivinhadores.adivinhador_cesar as adivinhador_cesar


def criar_layout_padrao_advinhador(titulo, nome_adivinhador):
    return [[sg.Text(titulo)],
            [sg.Text('Opções')],
            Menus.retorna_layout_opçoes(nome_adivinhador),
            [sg.Text('Mensagem encriptada:'), sg.Input(key='mensagem')],
            [sg.Output(key='output', size=(75,25))],
            [sg.Button('Executar', key='executar'), sg.Button('Abrir guia', key='link'),
             sg.Button('Limpar tela', key='limpar'), sg.Button('Retornar', key='retornar')]]


def menu_forca_bruta_cesar(tela_anterior):
    mensagem_inicial = '''
    Escolha uma opção e escreva uma mensagem encriptada pela cifra de César.
    Testaremos todas as chaves possíveis!
    OBS: dependendo do texto colocado, esse processo pode ser demorado
    '''
    layout_forca_bruta_cesar = criar_layout_padrao_advinhador(mensagem_inicial, 'Força bruta César')
    tela_forca_bruta_cesar = sg.Window('Cripythongrafia: força bruta César', layout_forca_bruta_cesar)
    while True:
        evento, valores = tela_forca_bruta_cesar.read()
        if evento in ('retornar', None):
            Menus.voltar_para_tela_anterior(tela_anterior, tela_forca_bruta_cesar)
            break
        Menus.verificar_eventos_gerais('Cifra de César', evento, tela_forca_bruta_cesar)
        if evento == 'executar':
            if valores['apenas letras']:
                forca_bruta_cesar.apenas_letras(valores['mensagem'])
            else:
                forca_bruta_cesar.varios_caracteres(valores['mensagem'])


def menu_adivinhador_cesar(tela_anterior):
    mensagem_inicial = '''
    Escolha uma opção de e escreva uma mensagem encriptada pela cifra de César.
    Tentaremos adivinhar qual é a mensagem traduzida !
    OBS: dependendo do texto, esse processo pode levar bastante tempo !
    '''
    layout_adivinha_cesar = criar_layout_padrao_advinhador(mensagem_inicial, 'Adivinhador César')
    tela_adivinha_cesar = sg.Window('Adivinhador César', layout_adivinha_cesar)
    while True:
        evento, valores = tela_adivinha_cesar.read()
        if evento in ('retornar', None):
            Menus.voltar_para_tela_anterior(tela_anterior, tela_adivinha_cesar)
            break
        Menus.verificar_eventos_gerais('Cifra de César', evento, tela_adivinha_cesar)
        if evento == 'executar':
            adivinhador_cesar.adivinhar_cesar(valores['mensagem'])
