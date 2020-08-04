import PySimpleGUI as sg
import webbrowser
import Menus.menus_utilitarios as menus_utilitarios
import Menus.menus_cifras as menus_cifras
import Menus.utilidades_menus as utilidades_menu
import banco_de_dados

# Dicionário utilizado para a criação do layout opções e banco de dados.
opcoes_cifras = [cifra for cifra in banco_de_dados.dic_criptografias_disponiveis.keys()]  # Colocar as opcoes de cifras dentro de uma lista.
lista_utilitarios_disponiveis = ['Força bruta César', 'Adivinhador César']

def main():
    # Layout da interface principal do programa.
    banco_de_dados.criar_banco_de_dados_se_ainda_nao_existir()
    sg.theme(banco_de_dados.retornar_tema_configurado())
    tela_principal = sg.Window('Cripythongrafia: Tela principal', retorna_layout_principal())  # Aplicar layout anterior e criar a janela.)
    while True:  # Loop que verifica as interações do usuários com o menu principal.
        evento, valores = tela_principal.read()
        if evento in ('6', None):
            # Fechar o programa
            tela_principal.close()
            break
        if evento == '1':
            # Iniciar interface "encriptar".
            tela_principal.Hide()
            menu_encriptar(tela_principal)
        if evento == '2':
            # Iniciar a interface "traduzir".
            tela_principal.Hide()
            menu_traducao(tela_principal)
        if evento == '3':
            # Inicar interface "utilitários"
            tela_principal.Hide()
            menu_utilitarios(tela_principal)
        if evento == '4':
            # Iniciar interface "opções"
            tela_principal.Close()
            menu_opcoes()
            tela_principal = sg.Window('Cripythongrafia: Tela principal', retorna_layout_principal())
        if evento == '5':
            # Abrir wiki ajuda
            webbrowser.open(utilidades_menu.dic_links['Wiki'])


def retorna_layout_principal():
    layout_principal =  [[sg.Text('       Cripythongrafia: Tela principal')],
                        [sg.Button('1- Criar mensagem criptografada', key='1')],
                        [sg.Button('2- Traduzir mensagem criptografada', key='2')],
                        [sg.Button('3- Utilitários', key='3')],
                        [sg.Button('4- Opções', key='4')],
                        [sg.Button('5- Ajuda', key='5')],
                        [sg.Button('6- Finalizar programa', key='6')]]
    return layout_principal


def retorna_layout_botoes_enumerados(titulo, lista_opcoes):
    layout = [[sg.Text(titulo)]]
    for n, opcao in enumerate(lista_opcoes):
        layout.append([sg.Button(f'{n + 1} - {opcao}', key=opcao)])
    layout.append([sg.Button('Retornar', key='retornar')])
    return layout


def retorna_layout_opcoes():
    layout_opcoes = [[sg.Text('     Cripythongrafia: Opções')],
                     [sg.Text('Tema:' + ' ' * 40), sg.Text('Idioma:')],
                     [sg.Listbox(sg.theme_list(), select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(20, 5),
                      key="tema", default_values=[banco_de_dados.retornar_tema_configurado()]),
                      sg.Listbox(['Portugues', 'Ingles'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(20, 5),
                      key="idioma", default_values=['Portugues'])]]
    subdivisao_chaves_padroes_cifras = [[sg.Text('Cifras:'), sg.Combo(opcoes_cifras, enable_events=True, key="nova_opcao")]]
    for cifra, modos in banco_de_dados.dic_criptografias_disponiveis.items():
        subdivisao_layout = []
        lista_elementos_atuais = []
        for modo in modos:
            if len(lista_elementos_atuais) == 4:  # Sempre pular para a próxima linha após colocar 4 elementos.
                subdivisao_layout.append(lista_elementos_atuais[:])
                lista_elementos_atuais = []
            lista_elementos_atuais += [sg.Text(f'{modo}'), sg.Input(key=f'{cifra}-{modo.strip()}')]
        subdivisao_layout.append(lista_elementos_atuais)
        subdivisao_chaves_padroes_cifras.append([sg.Frame(cifra, layout=subdivisao_layout, visible=False, key=cifra)])
    layout_opcoes.append([sg.Frame('Chaves padrões cifras', layout=subdivisao_chaves_padroes_cifras)])
    layout_opcoes.append([sg.Output(size=(100,10))])
    layout_opcoes.append([sg.Button('Retornar', key='retornar'), sg.Button('Aplicar', key='aplicar')])
    return layout_opcoes


def executar_menu(titulo, dicionario_funcoes, tela_anterior, layout):
    tela_atual = sg.Window(titulo, layout)
    while True:
        evento, valores = tela_atual.read()
        if evento in ('retornar', None):
            utilidades_menu.voltar_para_tela_anterior(tela_anterior, tela_atual)
            break
        tela_atual.Hide()
        for opcao, funcao in dicionario_funcoes.items():
            if evento == opcao:
                funcao(tela_atual)


def menu_encriptar(tela_anterior):
    titulo = 'Cripythongrafia: Encriptação'
    layout_encriptar = retorna_layout_botoes_enumerados(titulo, dic_criptografias_disponiveis.keys())
    dic_funcoes_menus_cifras_encript = {
        'Cifra de César':menus_cifras.menu_cifra_de_cesar_encriptação,
        'Substituição simples':menus_cifras.menu_subst_simples_encriptação,
        'Cifra de Vigenère':menus_cifras.menu_cifra_de_vigenere_encriptação
    }

    executar_menu(titulo, dic_funcoes_menus_cifras_encript, tela_anterior, layout_encriptar)


def menu_traducao(tela_anterior):
    titulo = "Cripythongrafia: Tradução"
    layout_traducao = retorna_layout_botoes_enumerados(titulo, dic_criptografias_disponiveis.keys())
    dic_funcoes_menus_cifras_traduc = {
        'Cifra de César':menus_cifras.menu_cifra_de_cesar_tradução,
        'Substituição simples':menus_cifras.menu_subst_simples_tradução,
        'Cifra de Vigenère':menus_cifras.menu_cifra_de_vigenere_tradução
    }

    executar_menu(titulo, dic_funcoes_menus_cifras_traduc, tela_anterior, layout_traducao)


def menu_utilitarios(tela_anterior):
    titulo = "Cripythongrafia: Utilitários"
    layout_utilitarios = retorna_layout_botoes_enumerados(titulo, lista_utilitarios_disponiveis)
    dic_funcoes_utilitarios = {
        'Força bruta César':menus_utilitarios.menu_forca_bruta_cesar,
        'Adivinhador César':menus_utilitarios.menu_adivinhador_cesar
    }

    executar_menu(titulo, dic_funcoes_utilitarios, tela_anterior, layout_utilitarios)


def menu_opcoes():
    # Criação do layout do menu opções.
    tela_opcoes = sg.Window('Cripythongrafia: Opções', retorna_layout_opcoes())
    resposta = ''
    while True:
        evento, valores = tela_opcoes.read(timeout=1000)
        if evento in ('retornar', None):
            tela_opcoes.close()
            break
        if evento == 'nova_opcao':
            for cifra in opcoes_cifras:
                if valores["nova_opcao"] == cifra:
                    tela_opcoes.Element(cifra).update(visible=True)
                    tela_opcoes.Element(cifra).unhide_row()
                else:
                    tela_opcoes.Element(cifra).hide_row()
        if evento == 'aplicar':
            resposta = banco_de_dados.aplicar_novas_configuracoes(valores)
            tela_opcoes.close()
            tela_opcoes = sg.Window('Cripythongrafia: Opções', retorna_layout_opcoes())
        elif resposta:  # Imprimir respostas (é preciso esperar um pouco para imprimi-las, por isso é utilizado o timeout).
            print(resposta)
            resposta = ''

#db = sqlite3.connect('configs.db')
#banco_de_dados = db.cursor()
#print(banco_de_dados.execute("SELECT * FROM chaves_padroes").fetchall())
#print(banco_de_dados.execute('SELECT chave FROM chaves_padroes WHERE cifra = "Substituição simples" AND modo LIKE "Apenas letras%"').fetchall())
main()
