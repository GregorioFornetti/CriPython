import sqlite3
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.subst_simples as subst_simples
import dicionarios
import PySimpleGUI as sg

idioma_configurado = ''
tema_configurado = ''

def criar_banco_de_dados_se_ainda_nao_existir():
    criptografias_disponiveis = {'Cifra de César': ['Apenas letras', 'Vários caracteres'],
                                 'Substituição simples': ['Apenas letras (letras mensagem comum)      ', 'Apenas letras (letras mensagem encriptada)     ',
                                                      'Vários caracteres (letras mensagem comum)', 'Vários caracteres (letras mensagem encriptada)'], 
                                 'Cifra de Vigenère': ['Apenas letras', 'Vários caracteres']}
    try:  # Verificar se banco de dados existe.
        open('configs.db', 'r')
    except:  # Se não existir, criar o banco de dados e suas tabelas.
        db = sqlite3.connect('configs.db')
        banco_de_dados = db.cursor()
        # Criar tabela "opções", onde ficarão as opções de tema, fonte, tamanho da fonte, etc.
        banco_de_dados.execute('CREATE TABLE opcoes (opcao TEXT, escolha TEXT)')
        # Adicionando os valores padrões da tabela "opções"
        banco_de_dados.execute('INSERT INTO opcoes VALUES ("tema", "DarkGrey5")')
        banco_de_dados.execute('INSERT INTO opcoes VALUES ("idioma", "Portugues")')
        # Criar tabela "chave_padroes", onde ficarão as chaves salvas pelos usuário.
        banco_de_dados.execute('CREATE TABLE chaves_padroes (cifra TEXT, modo TEXT, chave TEXT)')
        # Colocar valores "place holder" na tabela chaves padrões
        for cifra, modos in dicionarios.criptografias_disponiveis.items():
            for modo in modos:
                banco_de_dados.execute('INSERT INTO chaves_padroes VALUES (?, ?, ?)', [cifra, modo.strip(), ''])
        db.commit()
        db.close()


def restaurar_padrao():
    # Voltar o banco de dados para suas configurações iniciais
    global idioma_configurado
    global tema_configurado
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    banco_de_dados.execute('UPDATE opcoes SET escolha = "DarkGrey5" WHERE opcao = "tema"')
    tema_configurado = 'DarkGrey5'
    sg.theme('DarkGrey5')
    banco_de_dados.execute('UPDATE opcoes SET escolha = "Portugues" WHERE opcao = "idioma"')
    idioma_configurado = 'Portugues'
    dicionarios.atualizar_idioma('Portugues')


    for cifra, modos in dicionarios.criptografias_disponiveis.items():
        for modo in modos:
            banco_de_dados.execute('UPDATE chaves_padroes SET chave = ""')
    db.commit()
    db.close()
    return 'Configurações restauradas !'

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
            for indice_modo, titulo_cifra in enumerate(titulos_cifras):  # Imprimir mensagem de sucesso
                dic_texto = dicionarios.retorna_mensagem_menu_opcoes()
                return dic_texto[titulo_cifra]
        else:
            for indice_modo, titulo_cifra in enumerate(titulos_cifras):  # Imprimir mensagem de erro
                dic_texto = dicionarios.retorna_mensagem_menu_opcoes(erro=True)
                return dic_texto[titulo_cifra]
    return ''  # Caso não tenha sido digitado nenhuma chave, retornar mensagem vazia


def aplicar_novas_configuracoes(dic_opcoes):
    global idioma_configurado
    global tema_configurado
    mensagem = ''
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    if dic_opcoes['idioma'][0] != idioma_configurado:  # Definir novo idioma
        idioma_configurado = dic_opcoes['idioma'][0]
        dicionarios.atualizar_idioma(idioma_configurado)
        banco_de_dados.execute('UPDATE opcoes SET escolha = ? WHERE opcao = "idioma"', dic_opcoes['idioma'])
        mensagem += dicionarios.retorna_mensagem_idioma(idioma_configurado)

    if dic_opcoes['tema'][0] != tema_configurado:  # Definindo o novo tema escrito pelo usuario
        tema_configurado = dic_opcoes['tema'][0]
        sg.theme(tema_configurado)  # Aplicar novo tema.
        banco_de_dados.execute('UPDATE opcoes SET escolha = ? WHERE opcao = "tema"', dic_opcoes['tema'])
        mensagem += dicionarios.retorna_mensagem_temas(tema_configurado)
    
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


def coleta_tema_configurado():  # Coleta o tema configurado (o que está armazenado no DB) e armazena em uma variavel.
    global tema_configurado
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    tema_configurado = banco_de_dados.execute('SELECT escolha FROM opcoes WHERE opcao = "tema"').fetchone()[0]
    db.close()


def coleta_idioma_configurado():  # Coleta o idioma configurado e armazena em uma variavel.
    global idioma_configurado
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    idioma_configurado = banco_de_dados.execute('SELECT escolha FROM opcoes WHERE opcao = "idioma"').fetchone()[0]
    db.close()


def retorna_chaves_padroes(cifra, modo):
    lista_chaves = []
    modo += '%'
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    chaves = banco_de_dados.execute('SELECT chave FROM chaves_padroes WHERE cifra = ? AND modo LIKE ?', [cifra, modo]).fetchall()
    for chave in chaves:
        if chave[0]:
            lista_chaves.append(chave[0])
        else:
            return False
    return lista_chaves

criar_banco_de_dados_se_ainda_nao_existir()
coleta_idioma_configurado()
coleta_tema_configurado()
'''
db = sqlite3.connect('configs.db')
bd = db.cursor()
print(bd.execute('SELECT * FROM opcoes').fetchall())
print(bd.execute('SELECT * FROM chaves_padroes').fetchall())
'''