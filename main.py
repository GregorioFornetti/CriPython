import PySimpleGUI as sg
import webbrowser
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.subst_simples as subst_simples
import Menus.menus_utilitarios as menus_utilitarios
import Menus.menus_cifras as menus_cifras
import Menus.utilidades_menus as utilidades_menu
import sqlite3

# Dicionário utilizado para a criação do layout opções e banco de dados.
dic_criptografias_disponiveis = {'Cifra de César': ['Apenas letras', 'Vários caracteres'],
                                  'Substituição simples': ['Apenas letras (letras mensagem comum)      ', 'Apenas letras (letras mensagem encriptada)     ',
                                                           'Vários caracteres (letras mensagem comum)', 'Vários caracteres (letras mensagem encriptada)'], 
                                  'Cifra de Vigenère': ['Apenas letras', 'Vários caracteres']}
lista_utilitarios_disponiveis = ['Força bruta César', 'Adivinhador César']

def main():
    # Layout da interface principal do programa.
    criar_banco_de_dados_se_ainda_nao_existir()
    sg.theme(retornar_tema_configurado())
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
                     [sg.Text('Tema:')],
                     [sg.Listbox(sg.theme_list(), select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(20, 5), enable_events=True,
                      key="tema", default_values=[retornar_tema_configurado()])],
                     [sg.Text('Chaves padrões:')]]
    for cifra, modos in dic_criptografias_disponiveis.items():
        subdivisao_layout = []
        lista_elementos_atuais = []
        for modo in modos:
            if len(lista_elementos_atuais) == 4:  # Sempre pular para a próxima linha após colocar 4 elementos.
                subdivisao_layout.append(lista_elementos_atuais[:])
                lista_elementos_atuais = []
            lista_elementos_atuais += [sg.Text(f'{modo}'), sg.Input(key=f'{cifra}-{modo.strip()}')]
        subdivisao_layout.append(lista_elementos_atuais)
        layout_opcoes.append([sg.Frame(cifra, layout=subdivisao_layout)])
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
        if evento == 'aplicar':
            resposta = aplicar_novas_configuracoes(valores)
            tela_opcoes.close()
            tela_opcoes = sg.Window('Cripythongrafia: Opções', retorna_layout_opcoes())
        elif resposta:  # Imprimir respostas (é preciso esperar um pouco para imprimi-las, por isso é utilizado o timeout).
            print(resposta)
            resposta = ''

def aplicar_novas_configuracoes(dic_opcoes):
    mensagem = ''
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()

    if dic_opcoes['tema'][0] != retornar_tema_configurado():  # O usuário escolheu um novo tema
        sg.theme(dic_opcoes['tema'][0])  # Aplicar novo tema.
        banco_de_dados.execute('UPDATE opcoes_de_video SET escolha = ? WHERE opcao = "tema"', dic_opcoes['tema'])
        mensagem += f'Novo tema: "{dic_opcoes["tema"][0]}" definido com sucesso !'
    
    mensagem += tentar_salvar_chave_padrao(['Cifra de César-Apenas letras'], dic_opcoes, 
                                           banco_de_dados, cifra_de_cesar.retorna_chave_se_for_valida)
    mensagem += tentar_salvar_chave_padrao(['Cifra de César-Vários caracteres'], dic_opcoes,
                                           banco_de_dados, cifra_de_cesar.retorna_chave_se_for_valida)
    mensagem += tentar_salvar_chave_padrao(['Substituição simples-Apenas letras (letras mensagem comum)',
                                            'Substituição simples-Apenas letras (letras mensagem encriptada)'],
                                            dic_opcoes, banco_de_dados, subst_simples.retorna_chaves_se_for_valida)
    mensagem += tentar_salvar_chave_padrao(['Substituição simples-Vários caracteres (letras mensagem comum)',
                                            'Substituição simples-Vários caracteres (letras mensagem encriptada)'],
                                            dic_opcoes, banco_de_dados, subst_simples.retorna_chaves_se_for_valida)
    mensagem += tentar_salvar_chave_padrao(['Cifra de Vigenère-Apenas letras'], dic_opcoes, 
                                           banco_de_dados, cifra_de_vigenere.testa_chave_vigenere_apenas_letras)
    mensagem += tentar_salvar_chave_padrao(['Cifra de Vigenère-Vários caracteres'], dic_opcoes, 
                                           banco_de_dados, cifra_de_vigenere.testa_chave_vigenere_varios_caracteres)

    db.commit()
    db.close()
    return mensagem


def tentar_salvar_chave_padrao(titulos_cifras, dic_opcoes, banco_de_dados, funcao_verificadora_de_chave):
    if dic_opcoes[titulos_cifras[0]]:
        lista_chaves = []
        for titulo in titulos_cifras:
            lista_chaves.append(dic_opcoes[titulo])
        chaves_verificadas = funcao_verificadora_de_chave(lista_chaves)
        if chaves_verificadas:
            if type(chaves_verificadas) == list:  # Caso existam mais do que uma chave na cifra, executar um loop de "update".
                for indice_titulo, chave in enumerate(chaves_verificadas):
                    lista_valores_db = [chave] + titulos_cifras[indice_titulo].split('-')
                    banco_de_dados.execute('UPDATE chaves_padroes SET chave = ? WHERE cifra = ? AND modo = ?', lista_valores_db)
            else:  # Caso tenha apenas uma chave, realizar apenas um update.
                lista_valores_db = [chaves_verificadas] + titulos_cifras[0].split('-')  # Criar lista com elementos a serem colocados no banco de dados (cifra, modo e chave)
                banco_de_dados.execute('UPDATE chaves_padroes SET chave = ? WHERE cifra = ? AND modo = ?', lista_valores_db)
            for titulo_cifra in titulos_cifras:  # Imprimir mensagem de sucesso
                return f'Chave padrão {titulo_cifra} salva com sucesso !\n\n'
        else:
            for titulo_cifra in titulos_cifras:  # Imprimir mensagem de erro
                return f'Erro: não foi possível salvar a chave padrão: {titulo_cifra}.\nA chave digitada não é válida !\nPara verificar as chaves possiveis, clique em "ajuda".\n\n'
    return ''  # Caso não tenha sido digitado nenhuma chave, retornar mensagem vazia


def criar_banco_de_dados_se_ainda_nao_existir():
    try:  # Verificar se banco de dados existe.
        open('configs.db', 'r')
    except:  # Se não existir, criar o banco de dados e suas tabelas.
        db = sqlite3.connect('configs.db')
        banco_de_dados = db.cursor()
        # Criar tabela "opções_de_video", onde ficarão as opções de tema, fonte, tamanho da fonte, etc.
        banco_de_dados.execute('CREATE TABLE opcoes_de_video (opcao TEXT, escolha TEXT)')
        # Adicionando os valores padrões da tabela "opções_de_video"
        banco_de_dados.execute('INSERT INTO opcoes_de_video VALUES ("tema", "DarkGrey5")')
        # Criar tabela "chave_padroes", onde ficarão as chaves salvas pelos usuário.
        banco_de_dados.execute('CREATE TABLE chaves_padroes (cifra TEXT, modo TEXT, chave TEXT)')
        # Colocar valores "place holder" na tabela chaves padrões
        for cifra, modos in dic_criptografias_disponiveis.items():
            for modo in modos:
                banco_de_dados.execute('INSERT INTO chaves_padroes VALUES (?, ?, ?)', [cifra, modo.strip(), ''])
        db.commit()
        db.close()


def retornar_tema_configurado():  # Retornar o tema armazenado no banco de dados.
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    tema = banco_de_dados.execute('SELECT escolha FROM opcoes_de_video WHERE opcao = "tema"').fetchone()[0]
    db.close()
    return tema

#db = sqlite3.connect('configs.db')
#banco_de_dados = db.cursor()
#print(banco_de_dados.execute("SELECT * FROM chaves_padroes").fetchall())
#print(banco_de_dados.execute('SELECT chave FROM chaves_padroes WHERE cifra = "Substituição simples" AND modo LIKE "Apenas letras%"').fetchall())
main()
