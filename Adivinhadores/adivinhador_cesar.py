import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.utilidades_cifras as utilidades


def adivinhar_cesar_apenas_letras(mensagem):
    lista_mensagens = []
    lista_pontuacoes = []
    for chave in range(1, 27):
        nova_mensagem = cifra_de_cesar.traduzir_modo_apenas_letras(str(chave), mensagem)
        lista_mensagens.append(nova_mensagem)
        lista_pontuacoes.append(calcula_pontuacao(nova_mensagem.lower()))
    imprimir_resultados(lista_mensagens, lista_pontuacoes)


def adivinhar_cesar_varios_caracteres(mensagem):
    lista_mensagens = []
    lista_pontuacoes = []
    for chave in range(1, 668):
        nova_mensagem = cifra_de_cesar.traduzir_modo_varios_caracteres(str(chave), mensagem)
        lista_mensagens.append(nova_mensagem)
        lista_pontuacoes.append(calcula_pontuacao(nova_mensagem))
    imprimir_resultados(lista_mensagens, lista_pontuacoes)


def calcula_pontuacao(mensagem):
    dicionario_pontuacao_letras = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0,
                                   'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,
                                   'w':0, 'x':0, 'y':0, 'z':0}
    total_letras_validas = 1
    pontuacao_mensagem = 0
    for caractere in mensagem:
        if ord(caractere) > utilidades.MIN_MINUSCULA and ord(caractere) < utilidades.MAX_MINUSCULA:  # Verificar se o caractere atual é uma letra sem acento.
            dicionario_pontuacao_letras[caractere] += 1
            total_letras_validas += 1
    for letra, frequencia in dicionario_pontuacao_letras.items():
        frequencia_perc_atual = dicionario_pontuacao_letras[letra] / total_letras_validas * 100
        pontuacao_mensagem += abs(frequencia_perc_atual - utilidades.frequencia_alfabeto_pt[letra])
    return pontuacao_mensagem


def imprimir_resultados(lista_mensagens, lista_pontuacoes):
    index_melhor_possibilidade = lista_pontuacoes.index(min(lista_pontuacoes))
    print("Após alguns cálculos, a mensagem traduzida com maior probabilidade de ser correta é: ")
    print(f"{lista_mensagens[index_melhor_possibilidade]}\n")
    print("E a chave utilizada para essa tradução foi: ")
    print(index_melhor_possibilidade + 1)
