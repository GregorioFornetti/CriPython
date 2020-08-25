import PySimpleGUI as sg
import webbrowser
import Menus.menus_utilitarios as menus_utilitarios
import Menus.menus_cifras as menus_cifras
import Menus.utilidades_menus as utilidades_menu
import dicionarios
import banco_de_dados
# Todos os textos do programa estão no arquivo "dicionarios.py" (textos para cada opcão de idioma).

# Dicionário utilizado para a criação do layout opções e banco de dados.
lista_utilitarios_disponiveis = ['Força bruta César', 'Adivinhador César']
opcoes_cifras_port = dicionarios.retorna_lista_cifras(coletar_port=True)
opcoes_utilitarios_port = dicionarios.retorna_lista_utilitarios(coletar_port=True)

def main():
    # Layout da interface principal do programa.
    sg.theme(banco_de_dados.tema_configurado)
    tela_principal = sg.Window('Cripythongraphy: Tela principal', retorna_layout_principal())  # Aplicar layout anterior e criar a janela.)
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
            tela_principal = sg.Window('Cripythongraphy: Tela principal', retorna_layout_principal())
        if evento == '5':
            # Abrir wiki ajuda
            webbrowser.open(utilidades_menu.dic_links['Wiki'])


def retorna_layout_principal():
    dic_textos = dicionarios.retorna_menu_principal()
    layout_principal =  [[sg.Text(' ' * 7 + dic_textos['titulo'])],
                        [sg.Button(dic_textos['opcao 1'], key='1')],
                        [sg.Button(dic_textos['opcao 2'], key='2')],
                        [sg.Button(dic_textos['opcao 3'], key='3')],
                        [sg.Button(dic_textos['opcao 4'], key='4')],
                        [sg.Button(dic_textos['opcao 5'], key='5')],
                        [sg.Button(dic_textos['opcao 6'], key='6')]]
    return layout_principal


def retorna_layout_botoes_enumerados(titulo, dic_textos, lista_opcoes, lista_chaves):  # Por padrao, a lista de chaves será as opcoes em portugues
    layout = [[sg.Text(dic_textos[titulo])]]
    for n, opcao in enumerate(lista_opcoes):
        layout.append([sg.Button(f'{n + 1} - {opcao}', key=lista_chaves[n])])
    layout.append([sg.Button(dic_textos['Retornar'], key='retornar')])
    return layout


def retorna_layout_opcoes(opcoes_cifras):
    idioma = banco_de_dados.idioma_configurado
    dic_textos = dicionarios.retorna_menu_opcoes()
    layout_opcoes = [[sg.Text(dic_textos['titulo'])],
                     [sg.Text(dic_textos['opcao temas'] + ' ' * 40), sg.Text(dic_textos['opcao idiomas'])],
                     [sg.Listbox(sg.theme_list(), select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(20, 5),
                      key="tema", default_values=[banco_de_dados.tema_configurado]),
                      sg.Listbox(['Portugues', 'English'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(20, 5),
                      key="idioma", default_values=[idioma])]]
    subdivisao_chaves_padroes_cifras = [[sg.Text(dic_textos['cifras']), sg.Combo(opcoes_cifras, enable_events=True, key="nova_opcao")]]

    indice_cifra = 0
    for cifra, modos in dicionarios.criptografias_disponiveis.items():  # Criando opcoes de chaves padroes...
        subdivisao_layout = []
        lista_elementos_atuais = []
        for indice_modo, modo in enumerate(modos):
            if len(lista_elementos_atuais) == 4:  # Sempre pular para a próxima linha após colocar 4 elementos.
                subdivisao_layout.append(lista_elementos_atuais[:])
                lista_elementos_atuais = []
            lista_elementos_atuais += [sg.Text(f'{dic_textos["modos"][cifra][indice_modo]}'), sg.Input(key=f'{cifra}-{modo.strip()}')]
        subdivisao_layout.append(lista_elementos_atuais)
        subdivisao_chaves_padroes_cifras.append([sg.Frame(opcoes_cifras[indice_cifra], layout=subdivisao_layout, visible=False, key=cifra)])
        indice_cifra += 1

    layout_opcoes.append([sg.Frame(dic_textos['chaves padroes'], layout=subdivisao_chaves_padroes_cifras)])
    layout_opcoes.append([sg.Output(size=(100,10))])
    layout_opcoes.append([sg.Button(dic_textos['retornar'], key='retornar'), sg.Button(dic_textos['aplicar'], key='aplicar'),
                          sg.Button(dic_textos['ajuda'], key='link')])
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
    titulo = 'Cripythongraphy: Encriptação'
    layout_encriptar = retorna_layout_botoes_enumerados(titulo, 
                                                        dicionarios.retorna_menu_encript_traduc_utilitarios(),
                                                        dicionarios.retorna_lista_cifras(),
                                                        opcoes_cifras_port)
    dic_funcoes_menus_cifras_encript = {
        'Cifra de César': menus_cifras.menu_cifra_de_cesar_encriptação,
        'Substituição simples': menus_cifras.menu_subst_simples_encriptação,
        'Cifra de Vigenère': menus_cifras.menu_cifra_de_vigenere_encriptação,
        'Bases numéricas': menus_cifras.menu_bases_numericas_encriptação,
    }

    executar_menu(titulo, dic_funcoes_menus_cifras_encript, tela_anterior, layout_encriptar)


def menu_traducao(tela_anterior):
    titulo = 'Cripythongraphy: Tradução'
    layout_traducao = retorna_layout_botoes_enumerados(titulo, 
                                                       dicionarios.retorna_menu_encript_traduc_utilitarios(),
                                                       dicionarios.retorna_lista_cifras(),
                                                       opcoes_cifras_port)
    dic_funcoes_menus_cifras_traduc = {
        'Cifra de César': menus_cifras.menu_cifra_de_cesar_tradução,
        'Substituição simples': menus_cifras.menu_subst_simples_tradução,
        'Cifra de Vigenère': menus_cifras.menu_cifra_de_vigenere_tradução,
        'Bases numéricas': menus_cifras.menu_bases_numericas_tradução
    }

    executar_menu(titulo, dic_funcoes_menus_cifras_traduc, tela_anterior, layout_traducao)


def menu_utilitarios(tela_anterior):
    titulo = "Cripythongraphy: Utilitários"
    layout_utilitarios = retorna_layout_botoes_enumerados(titulo,
                                                          dicionarios.retorna_menu_encript_traduc_utilitarios(),
                                                          dicionarios.retorna_lista_utilitarios(),
                                                          opcoes_utilitarios_port)
    dic_funcoes_utilitarios = {
        'Força bruta César':menus_utilitarios.menu_forca_bruta_cesar,
        'Adivinhador César':menus_utilitarios.menu_adivinhador_cesar
    }

    executar_menu(titulo, dic_funcoes_utilitarios, tela_anterior, layout_utilitarios)


def menu_opcoes():
    # Criação do layout do menu opções.
    opcoes_cifras = dicionarios.retorna_lista_cifras_sem_chaves()
    tela_opcoes = sg.Window('Cripythongraphy: Opções', retorna_layout_opcoes(opcoes_cifras))
    resposta = ''
    while True:
        evento, valores = tela_opcoes.read(timeout=1000)
        if evento in ('retornar', None):
            tela_opcoes.close()
            break
        utilidades_menu.verificar_eventos_gerais('Opcoes', evento, tela_opcoes)
        if evento == 'nova_opcao':
            for indice_cifra, cifra in enumerate(opcoes_cifras):  # Atualizar a tela para mostrar apenas as chaves da cifra escolhida atualmente.
                '''
                OBS: São utilizadas duas listas de opções. Uma no idioma padrão português e outra no idioma selecionado pelo usuario.
                Isso é necessário pois todas as chaves que estão conectadas na interface dos botões e inputs estão em português.
                '''
                if valores["nova_opcao"] == cifra:  # Revelar apenas a cifra escolhida
                    tela_opcoes.Element(opcoes_cifras_port[indice_cifra]).update(visible=True)
                    tela_opcoes.Element(opcoes_cifras_port[indice_cifra]).unhide_row()
                else:  # Esconder as outras
                    tela_opcoes.Element(opcoes_cifras_port[indice_cifra]).hide_row()
        if evento == 'aplicar':
            resposta = banco_de_dados.aplicar_novas_configuracoes(valores)
            tela_opcoes.close()
            opcoes_cifras = dicionarios.retorna_lista_cifras_sem_chaves()  # Atualizar os nomes de opções de cifras caso mude o idioma.
            tela_opcoes = sg.Window('Cripythongraphy: Opções', retorna_layout_opcoes(opcoes_cifras))
        elif resposta:  # Imprimir respostas (é preciso esperar um pouco para imprimi-las, por isso é utilizado o timeout).
            print(resposta)
            resposta = ''


main()
