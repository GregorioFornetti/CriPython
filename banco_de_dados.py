import sqlite3
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.subst_simples as subst_simples

dic_criptografias_disponiveis = {'Cifra de César': ['Apenas letras', 'Vários caracteres'],
                                 'Substituição simples': ['Apenas letras (letras mensagem comum)      ', 'Apenas letras (letras mensagem encriptada)     ',
                                                          'Vários caracteres (letras mensagem comum)', 'Vários caracteres (letras mensagem encriptada)'], 
                                 'Cifra de Vigenère': ['Apenas letras', 'Vários caracteres']}

dic_crips_eng = {'Cifra de César': ['Letters only', 'Several characters'],
                 'Substituição simples': ['Letters only (commom message letters)      ', 'Letters only (cipher message letters)     ',
                                          'Several characters (commom message letters)', 'Several characters (cipher message letters)'], 
                 'Cifra de Vigenère': ['Letters only', 'Several characters']}
opcoes_cifras_eng = ['Caesar Cipher', 'Substituition Cipher', 'Vigenère Cipher']
# FAZER UM DICIONARIO PARA CADA MENSAGEM......

def criar_banco_de_dados_se_ainda_nao_existir():
    try:  # Verificar se banco de dados existe.
        open('configs.db', 'r')
    except:  # Se não existir, criar o banco de dados e suas tabelas.
        db = sqlite3.connect('configs.db')
        banco_de_dados = db.cursor()
        # Criar tabela "opções", onde ficarão as opções de tema, fonte, tamanho da fonte, etc.
        banco_de_dados.execute('CREATE TABLE opcoes (opcao TEXT, escolha TEXT)')
        # Adicionando os valores padrões da tabela "opções"
        banco_de_dados.execute('INSERT INTO opcoes VALUES ("tema", "DarkGrey5")')
        banco_de_dados.execute('INSERT INTO opcoes VALUES ("idioma", "portugues")')
        # Criar tabela "chave_padroes", onde ficarão as chaves salvas pelos usuário.
        banco_de_dados.execute('CREATE TABLE chaves_padroes (cifra TEXT, modo TEXT, chave TEXT)')
        # Colocar valores "place holder" na tabela chaves padrões
        for cifra, modos in dic_criptografias_disponiveis.items():
            for modo in modos:
                banco_de_dados.execute('INSERT INTO chaves_padroes VALUES (?, ?, ?)', [cifra, modo.strip(), ''])
        db.commit()
        db.close()


def tentar_salvar_chave_padrao(titulos_cifras, dic_opcoes, banco_de_dados, funcao_verificadora_de_chave, idioma):
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
                if idioma == 'Portugues':
                    return f'Chave padrão {titulo_cifra} salva com sucesso !\n\n'
                else:
                    # AQUI
                    return f'Default key {dict_cifras_eng[cifra]}-{dic_crips_eng[cifra][indice_modo]} successfully saved !\n\n'
        else:
            for indice_modo, titulo_cifra in enumerate(titulos_cifras):  # Imprimir mensagem de erro
                if idioma == 'Portugues':
                    return f'Erro: não foi possível salvar a chave padrão: {titulo_cifra}.\nA chave digitada não é válida !\nPara verificar as chaves possiveis, clique em "ajuda".\n\n'
                else:
                    # AQUI
                    pass
    return ''  # Caso não tenha sido digitado nenhuma chave, retornar mensagem vazia


def aplicar_novas_configuracoes(dic_opcoes):
    idioma = retornar_idioma_configurado()
    mensagem = ''
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()

    if dic_opcoes['tema'][0] != retornar_tema_configurado():  # Definindo o novo tema escrito pelo usuario
        sg.theme(dic_opcoes['tema'][0])  # Aplicar novo tema.
        banco_de_dados.execute('UPDATE opcoes SET escolha = ? WHERE opcao = "tema"', dic_opcoes['tema'])
        if idioma == 'Portugues':
            mensagem += f'Novo tema: "{dic_opcoes["tema"][0]}" definido com sucesso !'
        else:
            mensagem += f'New theme: "{dic_opcoes["tema"][0]}" successfully applied !'
    if dic_opcoes['idioma'][0] != retornar_idioma_configurado():
        banco_de_dados.execute('UPDATE opcoes SET escolha = ? WHERE opcao = "idioma"', dic_opcoes['idioma'])
        if idioma == 'Portugues':
            mensagem += f'Novo idioma: "{dic_opcoes["idioma"][0]}" definido com sucesso !'
        else:
            mensagem += f'Novo language: "{dic_opcoes["idioma"][0]}" successfully applied !'
    
    mensagem += tentar_salvar_chave_padrao(['Cifra de César-Apenas letras'], dic_opcoes, 
                                           banco_de_dados, cifra_de_cesar.retorna_chave_se_for_valida, idioma)
    mensagem += tentar_salvar_chave_padrao(['Cifra de César-Vários caracteres'], dic_opcoes,
                                           banco_de_dados, cifra_de_cesar.retorna_chave_se_for_valida, idioma)
    mensagem += tentar_salvar_chave_padrao(['Substituição simples-Apenas letras (letras mensagem comum)',
                                            'Substituição simples-Apenas letras (letras mensagem encriptada)'],
                                            dic_opcoes, banco_de_dados, subst_simples.retorna_chaves_se_for_valida, idioma)
    mensagem += tentar_salvar_chave_padrao(['Substituição simples-Vários caracteres (letras mensagem comum)',
                                            'Substituição simples-Vários caracteres (letras mensagem encriptada)'],
                                            dic_opcoes, banco_de_dados, subst_simples.retorna_chaves_se_for_valida, idioma)
    mensagem += tentar_salvar_chave_padrao(['Cifra de Vigenère-Apenas letras'], dic_opcoes, 
                                           banco_de_dados, cifra_de_vigenere.testa_chave_vigenere_apenas_letras, idioma)
    mensagem += tentar_salvar_chave_padrao(['Cifra de Vigenère-Vários caracteres'], dic_opcoes, 
                                           banco_de_dados, cifra_de_vigenere.testa_chave_vigenere_varios_caracteres, idioma)

    db.commit()
    db.close()
    return mensagem


def retornar_tema_configurado():  # Retornar o tema armazenado no banco de dados.
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    tema = banco_de_dados.execute('SELECT escolha FROM opcoes WHERE opcao = "tema"').fetchone()[0]
    db.close()
    return tema


def retornar_idioma_configurado():
    db = sqlite3.connect('configs.db')
    banco_de_dados = db.cursor()
    idioma = banco_de_dados.execute('SELECT escolha FROM opcoes WHERE opcao = "idioma"').fetchone()[0]
    db.close()
    return idioma
