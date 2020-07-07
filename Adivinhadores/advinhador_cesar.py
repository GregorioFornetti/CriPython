import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.valores as valores


def advinhador_cesar(mensagem):
    lista_mensagem = []
    lista_pontuacao = []
    for chave in range(1, 27):
        nova_mensagem = cifra_de_cesar.traduzir_modo_apenas_letras(str(chave), mensagem)
        lista_mensagem.append(nova_mensagem)
        lista_pontuacao.append(calcula_pontuacao(nova_mensagem))
    index_melhor_possibilidade = lista_pontuacao.index(min(lista_pontuacao))
    print(lista_mensagem[index_melhor_possibilidade])
        

def calcula_pontuacao(mensagem):
    dicionario_pontuacao_letras = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0,
                                   'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,
                                   'w':0, 'x':0, 'y':0, 'z':0}
    mensagem = mensagem.lower()
    total_letras_validas = 0
    pontuacao_mensagem = 0
    for caractere in mensagem:
        if ord(caractere) > valores.MIN_MINUSCULA and ord(caractere) < valores.MAX_MINUSCULA:  # Verificar se o caractere atual é uma letra sem acento.
            dicionario_pontuacao_letras[caractere] += 1
            total_letras_validas += 1
    for letra, frequencia in dicionario_pontuacao_letras.items():
        frequencia_perc_atual = dicionario_pontuacao_letras[letra] / total_letras_validas * 100
        pontuacao_mensagem += abs(frequencia_perc_atual - valores.frequencia_alfabeto_pt[letra])
    return pontuacao_mensagem


advinhador_cesar("Vp abkv ilt jvt cj ? Chtvz alzahy h klzpujypwahçãv. Lih Mbujpvuvb !!! Jhyhtih xbl slnhs !!")
