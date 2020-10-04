import PySimpleGUI as sg
import Menus.utilidades_menus as utilidades_menus
import Utilitarios.forca_bruta_cesar as forca_bruta_cesar
import Utilitarios.adivinhador_cesar as adivinhador_cesar
import Cifras.bases_numericas as bases_numericas
import dicionarios


def retorna_layout_padrao_advinhador(titulo, lista_opcoes):
    dic_textos = dicionarios.retorna_menu_utilitario()
    return [[sg.Text(dic_textos[titulo])],
            [sg.Text(dic_textos[f'Mensagem {titulo}'])],
            [sg.Text(dic_textos['Opções'])],
            utilidades_menus.retorna_layout_opçoes_em_radio(lista_opcoes),
            [sg.Text(dic_textos['Mensagem encriptada']), sg.Input(key='mensagem')],
            [sg.Output(key='output', size=(75,25))],
            utilidades_menus.retorna_layout_botoes_utilitarios_padrao(dic_textos)]

def retorna_layout_calculadora_bases_numericas():
    dic_textos = dicionarios.retorna_menu_utilitario()
    lista_opcoes = ['Binário', 'Octal', 'Decimal', 'Hexadecimal']
    return [[sg.Text(dic_textos['Conversor bases numéricas'])],
            [sg.Text(dic_textos['Mensagem conversor bases numéricas'])],
            [sg.Text(dic_textos['Converter de'])],
            utilidades_menus.retorna_layout_opçoes_em_radio(lista_opcoes),
            [sg.Text(dic_textos['Para'])],
            utilidades_menus.retorna_layout_opçoes_em_radio(lista_opcoes, conexao='radio2'),
            [sg.Text(dic_textos['Numero']), sg.Input(key='mensagem')],
            [sg.Output(key='output', size=(75,25))],
            utilidades_menus.retorna_layout_botoes_utilitarios_padrao(dic_textos)]

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
        'Apenas letras':forca_bruta_cesar.imprimir_apenas_letras,
        'Vários caracteres':forca_bruta_cesar.imprimir_varios_caracteres
    }
    layout_forca_bruta_cesar = retorna_layout_padrao_advinhador(titulo, dic_funcoes_forca_bruta.keys())
    
    executar_menu_utilitarios('Força bruta César', dic_funcoes_forca_bruta, tela_anterior, layout_forca_bruta_cesar)


def menu_adivinhador_cesar(tela_anterior):
    titulo = 'Adivinhador César'
    dic_funcoes_adivhador_cesar = {
        'Apenas letras':adivinhador_cesar.imprimir_melhor_mensagem_adivinhada_apenas_letras,
        'Vários caracteres':adivinhador_cesar.imprimir_melhor_mensagem_adivinhada_varios_caracteres
    }
    layout_adivinhador_cesar = retorna_layout_padrao_advinhador(titulo, dic_funcoes_adivhador_cesar.keys())

    executar_menu_utilitarios('Adivinhador César', dic_funcoes_adivhador_cesar, tela_anterior, layout_adivinhador_cesar)

def menu_conversor_bases_numericas(tela_anterior):
    titulo = 'Conversor bases numéricas'
    dict_funcoes = {
        'Binário': bases_numericas.verificar_num_bin,
        'Octal': bases_numericas.verificar_num_octal,
        'Decimal': bases_numericas.verificar_num_decimal,
        'Hexadecimal': bases_numericas.verificar_num_hexadecimal,
        'Binário-Octal': bases_numericas.converter_binario_para_octal,
        'Binário-Decimal': bases_numericas.converter_binario_para_decimal,
        'Binário-Hexadecimal': bases_numericas.converter_binario_para_hexadecimal,
        'Octal-Binário': bases_numericas.converter_octal_para_binario,
        'Octal-Decimal': bases_numericas.converter_octal_para_decimal,
        'Octal-Hexadecimal': bases_numericas.converter_octal_para_hexadecimal,
        'Decimal-Binário': bases_numericas.converter_decimal_para_binario,
        'Decimal-Octal': bases_numericas.converter_decimal_para_octal,
        'Decimal-Hexadecimal': bases_numericas.converter_decimal_para_hexadecimal,
        'Hexadecimal-Binário': bases_numericas.converter_hexadecimal_para_binario,
        'Hexadecimal-Octal': bases_numericas.converter_hexadecimal_para_octal,
        'Hexadecimal-Decimal': bases_numericas.converter_hexadecimal_para_decimal
    }
    layout_conversor = retorna_layout_calculadora_bases_numericas()
    tela_conversor = sg.Window(titulo, layout_conversor)
    while True:
        evento, valores = tela_conversor.read()
        if evento in ('retornar', None):
            utilidades_menus.voltar_para_tela_anterior(tela_anterior, tela_conversor)
            break
        utilidades_menus.verificar_eventos_gerais(titulo, evento, tela_conversor)

        if evento == 'executar':
            numero_digitado = valores['mensagem']
            primeira_base = ''
            numero_convertido = ''
            segunda_base = ''
            for base_numerica, selecionado in valores.items():
                if selecionado:
                    if not primeira_base:  # Verificando se o numero digito pelo usuario bate com a primeira base numerica selecionada
                        primeira_base = base_numerica
                        if not dict_funcoes[primeira_base](numero_digitado) and dict_funcoes[primeira_base](numero_digitado) != 0:  # Usuario digitou numero errado, mostrar mensagem de erro.
                            numero_convertido = dicionarios.retorna_erro_numero_invalido()
                            break
                    else:
                        segunda_base = base_numerica[:-1]
                        if primeira_base != segunda_base:
                            numero_convertido = str(dict_funcoes[f'{primeira_base}-{segunda_base}'](numero_digitado))
                        else:
                            numero_convertido = bases_numericas.tirar_zeros_a_esquerda(numero_digitado)
                        break
            print(dicionarios.retorna_mensagem_com_bordas(numero_convertido, 127))
