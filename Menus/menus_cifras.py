import PySimpleGUI as sg
import sqlite3
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.subst_simples as subst_simples
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.bases_numericas as bases_numericas
import Cifras.base_64 as base_64
import Menus.utilidades_menus as utilidades_menus
import dicionarios
import banco_de_dados


def retorna_layout_padrao_tradução(titulo, opcoes):
    dic_textos = dicionarios.retorna_menus_cifras()
    layout = [[sg.Text(f"{dic_textos[f'{titulo} (tradução)']:^110}")],
             [sg.Text(dic_textos['Opções'])],
              utilidades_menus.retorna_layout_opçoes_em_radio(opcoes),
             [sg.Text(dic_textos['Mensagem encriptada']), sg.InputText(key='mensagem')],
             [sg.Text(dic_textos['Chave']), sg.InputText(key='chave')],
             [sg.Text(dic_textos['Mensagem traduzida'])],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button(dic_textos['Traduzir'], key='traduzir'), sg.Button(dic_textos['Traduzir com chave padrão'], key="utilizar_chave_padrao"),
              sg.Button(dic_textos['Abrir guia cifra'], key='link'), sg.Button(dic_textos['Limpar tela'], key='limpar'),
              sg.Button(dic_textos['Retornar'], key='retornar')]]
    return layout


def retorna_layout_padrao_encriptação(titulo, opcoes):
    dic_textos = dicionarios.retorna_menus_cifras()
    layout = [[sg.Text(f"{dic_textos[f'{titulo} (encriptação)']:^110}")],
             [sg.Text(dic_textos['Opções'])],
              utilidades_menus.retorna_layout_opçoes_em_radio(opcoes),
             [sg.Text(dic_textos['Mensagem']), sg.InputText(key='mensagem')],
             [sg.Text(dic_textos['Chave']), sg.InputText(key='chave')],
             [sg.Text(dic_textos['Mensagem encriptada'])],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button(dic_textos['Encriptar'], key='encriptar'), sg.Button(dic_textos['Encriptar com chave padrão'], key="utilizar_chave_padrao"),
              sg.Button(dic_textos['Abrir guia cifra'], key='link'), sg.Button(dic_textos['Limpar tela'], key='limpar'),
              sg.Button(dic_textos['Retornar'], key='retornar')]]
    return layout


def retorna_layout_subst_simples(titulo, opcoes, modo='encriptacao'):
    # Trocará o nome do que era "chave" para "letras mensagem encriptada" e adicionará outro local para digitar chamado "letras mensagem comum".
    lista_textos = dicionarios.retorna_lista_subst_simples()
    if modo == 'encriptacao':
        layout_subst_simples = retorna_layout_padrao_encriptação(titulo, opcoes)
    else:
        layout_subst_simples = retorna_layout_padrao_tradução(titulo, opcoes)
    del layout_subst_simples[4]  # Retirar o input "chave"
    layout_subst_simples.insert(4, [sg.Text(lista_textos[0]), sg.Input('abcdefghijklmnopqrstuvwxyz', key='chave_1')])
    layout_subst_simples.insert(5, [sg.Text(lista_textos[1]), sg.Input(key='chave_2')])
    return layout_subst_simples


def retorna_layout_bases_numericas(titulo, opcoes, modo='encriptacao'):
    # O layout das bases numéricas é o layout padrão sem input "chave" e sem botão "chave padrão"
    if modo == 'encriptacao':
        layout_bases_numericas = retorna_layout_padrao_encriptação(titulo, opcoes)
    else:
        layout_bases_numericas = retorna_layout_padrao_tradução(titulo, opcoes)
    del layout_bases_numericas[4]  # Retirar o input "chave"
    del layout_bases_numericas[6][1]  # Retirar botão "chave padrão"
    return layout_bases_numericas


def retorna_layout_base_64(titulo,  modo='encriptacao'):
    # O layout das base_64 é igual o da bases_numéricas sem as opções.
    if modo == 'encriptacao':
        layout_base_64 = retorna_layout_bases_numericas(titulo, [])
    else:
        layout_base_64 = retorna_layout_bases_numericas(titulo, [], modo='traducao')
    del layout_base_64[1]  # Tirar o titulo de "Opções"
    del layout_base_64[1]  # Tirar o radio das opções...
    # Colocar radio invisivel de opção "Base 64", pois a função "executar_menu_cifra" verificará a opção selecionada.
    layout_base_64.append([sg.Radio(titulo, 'radio', key=titulo, default=True, visible=False)])
    return layout_base_64

def executar_menu_cifra(titulo_cifra, tela_anterior, dicionario_funcoes_cifras, layout_cifra):
    # Criará a janela do menu da cifra e verificará os eventos ocorridos nela (ex: botões clicados, tela foi fechada, inputs,...)
    tela_cifra = sg.Window(titulo_cifra, layout_cifra)
    while True:
        evento, valores = tela_cifra.read()
        if evento in ('retornar', None):
            utilidades_menus.voltar_para_tela_anterior(tela_anterior, tela_cifra)
            break
        utilidades_menus.verificar_eventos_gerais(titulo_cifra, evento, tela_cifra)
        if evento == 'encriptar' or evento == 'traduzir' or evento == "utilizar_chave_padrao":
            for opção, criptografar in dicionario_funcoes_cifras.items():
                if valores[opção]:  # Verificar a opção escolhida pelo usuário e executar a função referente a ela (armazenada no dicionário).
                    if evento == "utilizar_chave_padrao":
                        lista_chaves = banco_de_dados.retorna_chaves_padroes(titulo_cifra, opção)
                        if not lista_chaves:
                            print(dicionarios.retorna_mensagem_com_bordas(dicionarios.retorna_erro_chave_padrao(), 127))
                            break
                    else:
                        lista_chaves = []
                        for nome_item, chave in valores.items():  # Loop para procurar as chaves utilizadas (já que alguns modos utilizam mais que 1)
                            if 'chave' in nome_item:
                                lista_chaves.append(chave)
                    if lista_chaves:  # Caso seja encontrado alguma chave, a cifra atual precisa de uma chave para funcionar.
                        print(dicionarios.retorna_mensagem_com_bordas(criptografar(lista_chaves, valores['mensagem']), 127))
                    else:  # Caso nenhuma chave tenha sido encontrada, a cifra atual não necessita de chave.
                        print(dicionarios.retorna_mensagem_com_bordas(criptografar(valores['mensagem']), 127))


def menu_cifra_de_cesar_encriptação(tela_anterior):
    titulo_da_cifra = 'Cifra de César'
    dicionario_funções_cesar_encript = {'Apenas letras': cifra_de_cesar.encriptar_modo_apenas_letras,
                                        'Vários caracteres': cifra_de_cesar.encriptar_modo_varios_caracteres}
    layout_cifra_de_cesar_encript = retorna_layout_padrao_encriptação(titulo_da_cifra, dicionario_funções_cesar_encript.keys())
    
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_cesar_encript, layout_cifra_de_cesar_encript)


def menu_cifra_de_cesar_tradução(tela_anterior):
    titulo_da_cifra = 'Cifra de César'
    dicionario_funções_cesar_traduc = {'Apenas letras':cifra_de_cesar.traduzir_modo_apenas_letras,
                                       'Vários caracteres':cifra_de_cesar.traduzir_modo_varios_caracteres}
    layout_cifra_de_cesar_traduc = retorna_layout_padrao_tradução(titulo_da_cifra, dicionario_funções_cesar_traduc.keys())
    
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_cesar_traduc, layout_cifra_de_cesar_traduc)


def menu_subst_simples_encriptação(tela_anterior):
    titulo_da_cifra = 'Substituição simples'
    dicionario_funções_subst_encript = {'Apenas letras':subst_simples.encriptar_modo_apenas_letras,
                                        'Vários caracteres':subst_simples.encriptar_modo_varios_caracteres}
    layout_subst_simples_encript = retorna_layout_subst_simples(titulo_da_cifra, dicionario_funções_subst_encript.keys())
    
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_subst_encript, layout_subst_simples_encript)


def menu_subst_simples_tradução(tela_anterior):
    titulo_da_cifra = 'Substituição simples'
    dicionario_funções_subst_traduc = {'Apenas letras':subst_simples.traduzir_modo_apenas_letras,
                                       'Vários caracteres':subst_simples.traduzir_modo_varios_caracteres}
    layout_subst_simples_traduc = retorna_layout_subst_simples(titulo_da_cifra, dicionario_funções_subst_traduc.keys(), modo='tradução')
    
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_subst_traduc, layout_subst_simples_traduc)


def menu_cifra_de_vigenere_encriptação(tela_anterior):
    titulo_da_cifra = 'Cifra de Vigenère'
    dicionario_funções_vigenere_encript = {'Apenas letras':cifra_de_vigenere.encriptar_modo_apenas_letras,
                                           'Vários caracteres':cifra_de_vigenere.encriptar_modo_varios_caracteres}
    layout_cifra_de_vigenere_encript = retorna_layout_padrao_encriptação(titulo_da_cifra, dicionario_funções_vigenere_encript.keys())
    
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_vigenere_encript, layout_cifra_de_vigenere_encript)


def menu_cifra_de_vigenere_tradução(tela_anterior):
    titulo_da_cifra = 'Cifra de Vigenère'
    dicionario_funções_vigenere_traduc = {'Apenas letras':cifra_de_vigenere.traduzir_modo_apenas_letras,
                                          'Vários caracteres':cifra_de_vigenere.traduzir_modo_varios_caracteres}
    layout_cifra_de_vigenere_traduc = retorna_layout_padrao_tradução(titulo_da_cifra, dicionario_funções_vigenere_traduc.keys())
    
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_vigenere_traduc, layout_cifra_de_vigenere_traduc)


def menu_bases_numericas_encriptação(tela_anterior):
    titulo_da_cifra = 'Bases numéricas'
    dicionario_funções_bases_num_encript = {'Binário': bases_numericas.transformar_texto_para_binario,
                                            'Octal': bases_numericas.transformar_texto_para_octal,
                                            'Decimal': bases_numericas.transformar_texto_para_decimal,
                                            'Hexadecimal': bases_numericas.transformar_texto_para_hexadecimal}   
    layout_bases_numericas_encript = retorna_layout_bases_numericas(titulo_da_cifra, dicionario_funções_bases_num_encript.keys()) 

    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_bases_num_encript, layout_bases_numericas_encript)

def menu_bases_numericas_tradução(tela_anterior):
    titulo_da_cifra = 'Bases numéricas'
    dicionario_funções_bases_num_traduc = {'Binário': bases_numericas.transformar_binario_para_texto,
                                           'Octal': bases_numericas.transformar_octal_para_texto,
                                           'Decimal': bases_numericas.transformar_decimal_para_texto,
                                           'Hexadecimal': bases_numericas.transformar_hexadecimal_para_texto}
    layout_bases_numericas_traduc = retorna_layout_bases_numericas(titulo_da_cifra, dicionario_funções_bases_num_traduc, modo='traducao')

    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_bases_num_traduc, layout_bases_numericas_traduc)


def menu_base_64_encriptação(tela_anterior):
    titulo_da_cifra = 'Base 64'
    dicionario_funções_base_64_encript = {titulo_da_cifra: base_64.codificar_base_64}
    layout_base_64 = retorna_layout_base_64(titulo_da_cifra)
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_base_64_encript, layout_base_64)


def menu_base_64_tradução(tela_anterior):
    titulo_da_cifra = 'Base 64'
    dicionario_funções_base_64_traduc = {titulo_da_cifra: base_64.traduzir_base_64}
    layout_base_64 = retorna_layout_base_64(titulo_da_cifra, modo='Traducao')
    executar_menu_cifra(titulo_da_cifra, tela_anterior, dicionario_funções_base_64_traduc, layout_base_64)
