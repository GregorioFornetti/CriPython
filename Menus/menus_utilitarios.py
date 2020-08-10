import PySimpleGUI as sg
import Menus.utilidades_menus as utilidades_menus
import Adivinhadores.forca_bruta_cesar as forca_bruta_cesar
import Adivinhadores.adivinhador_cesar as adivinhador_cesar
import banco_de_dados
import dicionarios


def retorna_layout_padrao_advinhador(titulo, nome_adivinhador):
    dic_textos = dicionarios.retorna_menu_utilitario(banco_de_dados.retorna_idioma_configurado())
    return [[sg.Text(dic_textos[titulo])],
            [sg.Text(dic_textos[f'Mensagem {titulo}'])],
            [sg.Text(dic_textos['Opções'])],
            utilidades_menus.retorna_layout_opçoes_em_radio(nome_adivinhador),
            [sg.Text(dic_textos['Mensagem encriptada']), sg.Input(key='mensagem')],
            [sg.Output(key='output', size=(75,25))],
            [sg.Button(dic_textos['Executar'], key='executar'), sg.Button(dic_textos['Abrir wiki'], key='link'),
             sg.Button(dic_textos['Limpar tela'], key='limpar'), sg.Button(dic_textos['Retornar'], key='retornar')]]


def executar_menu_utilitarios(titulo, dicionario_funcoes, tela_anterior, layout_utilitario):
    tela_utilitario = sg.Window(titulo, layout_utilitario)
    while True:
        evento, valores = tela_utilitario.read()
        if evento in ('retornar', None):
            utilidades_menus.voltar_para_tela_anterior(tela_anterior, tela_utilitario)
            break
        utilidades_menus.verificar_eventos_gerais(titulo, evento, tela_utilitario)
        if evento == 'executar':
            for opcao, funcao in dicionario_funcoes.items():
                if valores[opcao]:
                    funcao(valores['mensagem'])


def menu_forca_bruta_cesar(tela_anterior):
    titulo = 'Força bruta César'
    dic_funcoes_forca_bruta = {
        'Apenas letras':forca_bruta_cesar.apenas_letras,
        'Vários caracteres':forca_bruta_cesar.varios_caracteres
    }
    layout_forca_bruta_cesar = retorna_layout_padrao_advinhador(titulo, dic_funcoes_forca_bruta.keys())
    
    executar_menu_utilitarios('Força bruta César', dic_funcoes_forca_bruta, tela_anterior, layout_forca_bruta_cesar)


def menu_adivinhador_cesar(tela_anterior):
    titulo = 'Adivinhador César'
    dic_funcoes_adivhador_cesar = {
        'Apenas letras':adivinhador_cesar.adivinhar_cesar_apenas_letras,
        'Vários caracteres':adivinhador_cesar.adivinhar_cesar_varios_caracteres
    }
    layout_adivinhador_cesar = retorna_layout_padrao_advinhador(titulo, dic_funcoes_adivhador_cesar.keys())

    executar_menu_utilitarios('Adivinhador César', dic_funcoes_adivhador_cesar, tela_anterior, layout_adivinhador_cesar)
