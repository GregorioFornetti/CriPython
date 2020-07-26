import PySimpleGUI as sg
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.subst_simples as subst_simples
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Menus.utilidades_menus as utilidades_menus


def retorna_layout_padrao_tradução(titulo):
    layout = [[sg.Text(f"{f'Cripythongrafia: {titulo} (tradução)':^110}")],
             [sg.Text('Opções:')],
             utilidades_menus.retorna_layout_opçoes(titulo),
             [sg.Text('Mensagem encriptada:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem traduzida:')],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button('Traduzir', key='traduzir'), sg.Button('Abrir guia da cifra', key='link'),
              sg.Button('Limpar tela', key='limpar') ,sg.Button('Retornar', key='retornar')]]
    return layout


def retorna_layout_padrao_encriptação(titulo):
    layout = [[sg.Text(f"{f'Cripythongrafia: {titulo} (encriptação)':^110}")],
             [sg.Text('Opções:')],
             utilidades_menus.retorna_layout_opçoes(titulo),
             [sg.Text('Mensagem:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem encriptada:')],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button('Encriptar', key='encriptar'), sg.Button('Abrir guia da cifra', key='link'),
              sg.Button('Limpar tela', key='limpar'), sg.Button('Retornar', key='retornar')]]
    return layout


def retorna_layout_subst_simples(titulo, modo='encriptação'):
    # Trocará o nome do que era "chave" para "letras mensagem encriptada" e adicionará outro local para digitar chamado "letras mensagem comum".
    layout_subst_simples = retorna_layout_padrao_encriptação(titulo)
    if modo == 'tradução':
        layout_subst_simples = retorna_layout_padrao_tradução(titulo)
    del layout_subst_simples[4]
    layout_subst_simples.insert(4, [sg.Text('Letras mensagem comum:    '), sg.Input('abcdefghijklmnopqrstuvwxyz', key='chave_1')])
    layout_subst_simples.insert(5, [sg.Text('Letras mensagem encriptada:'), sg.Input(key='chave_2')])
    return layout_subst_simples


def executar_menu_cifra(titulo, tela_anterior, dicionario_funcoes_cifras, layout_cifra):
    # Criará a janela do menu da cifra e verificará os eventos ocorridos nela (ex: botões clicados, tela foi fechada, inputs,...)
    tela_cifra = sg.Window(titulo, layout_cifra)
    while True:
        evento, valores = tela_cifra.read()
        if evento in ('retornar', None):
            utilidades_menus.voltar_para_tela_anterior(tela_anterior, tela_cifra)
            break
        utilidades_menus.verificar_eventos_gerais('Cifra de César', evento, tela_cifra)
        if evento == 'encriptar' or evento == 'traduzir':
            for opção, criptografar in dicionario_funcoes_cifras.items():
                if valores[opção]:  # Verificar a opção escolhida pelo usuário e executar a função referente a ela (armazenada no dicionário).
                    lista_chaves = []
                    for nome_item, chave in valores.items():  # Loop para procurar as chaves utilizadas (já que alguns modos utilizam mais que 1)
                        if 'chave' in nome_item:
                            lista_chaves.append(chave)
                    print(criptografar(lista_chaves, valores['mensagem']))


def menu_cifra_de_cesar_encriptação(tela_anterior):
    layout_cifra_de_cesar_encript = retorna_layout_padrao_encriptação('Cifra de César')
    dicionario_funções_cesar_encript = {'Apenas letras': cifra_de_cesar.encriptar_modo_apenas_letras,
                                        'Vários caracteres': cifra_de_cesar.encriptar_modo_varios_caracteres}
    
    executar_menu_cifra('Cifra de César (encriptação)', tela_anterior, dicionario_funções_cesar_encript, layout_cifra_de_cesar_encript)


def menu_cifra_de_cesar_tradução(tela_anterior):
    layout_cifra_de_cesar_traduc = retorna_layout_padrao_tradução('Cifra de César')
    dicionario_funções_cesar_traduc = {'Apenas letras':cifra_de_cesar.traduzir_modo_apenas_letras,
                                       'Vários caracteres':cifra_de_cesar.traduzir_modo_varios_caracteres}
    
    executar_menu_cifra('Cifra de César (tradução)', tela_anterior, dicionario_funções_cesar_traduc, layout_cifra_de_cesar_traduc)


def menu_subst_simples_encriptação(tela_anterior):
    layout_subst_simples_encript = retorna_layout_subst_simples('Substituição simples')
    dicionario_funções_subst_encript = {'Apenas letras':subst_simples.encriptar_modo_apenas_letras,
                                        'Vários caracteres':subst_simples.encriptar_modo_varios_caracteres}
    
    executar_menu_cifra('Substituição simples (encriptação)', tela_anterior, dicionario_funções_subst_encript, layout_subst_simples_encript)


def menu_subst_simples_tradução(tela_anterior):
    layout_subst_simples_traduc = retorna_layout_subst_simples('Substituição simples', modo='tradução')
    dicionario_funções_subst_traduc = {'Apenas letras':subst_simples.traduzir_modo_apenas_letras,
                                       'Vários caracteres':subst_simples.traduzir_modo_varios_caracteres}
    
    executar_menu_cifra('Substituição simples (tradução)', tela_anterior, dicionario_funções_subst_traduc, layout_subst_simples_traduc)


def menu_cifra_de_vigenere_encriptação(tela_anterior):
    layout_cifra_de_vigenere_encript = retorna_layout_padrao_encriptação('Cifra de Vigenère')
    dicionario_funções_vigenere_encript = {'Apenas letras':cifra_de_vigenere.encriptar_modo_apenas_letras,
                                           'Vários caracteres':cifra_de_vigenere.encriptar_modo_varios_caracteres}
    
    executar_menu_cifra('Cifra de Vigenère (encriptação)', tela_anterior, dicionario_funções_vigenere_encript, layout_cifra_de_vigenere_encript)


def menu_cifra_de_vigenere_tradução(tela_anterior):
    layout_cifra_de_vigenere_traduc = retorna_layout_padrao_tradução('Cifra de Vigenère')
    dicionario_funções_vigenere_traduc = {'Apenas letras':cifra_de_vigenere.traduzir_modo_apenas_letras,
                                          'Vários caracteres':cifra_de_vigenere.traduzir_modo_varios_caracteres}
    
    executar_menu_cifra('Cifra de Vigenère (tradução)', tela_anterior,
                                                        dicionario_funções_vigenere_traduc, layout_cifra_de_vigenere_traduc)
