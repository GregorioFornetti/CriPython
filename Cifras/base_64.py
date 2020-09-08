import Cifras.bases_numericas as bases_numericas
import dicionarios

dicionario_base_64 = {'000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D', '000100': 'E',
                      '000101': 'F', '000110': 'G', '000111': 'H', '001000': 'I', '001001': 'J',
                      '001010': 'K', '001011': 'L', '001100': 'M', '001101': 'N', '001110': 'O',
                      '001111': 'P', '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T',
                      '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X', '011000': 'Y',
                      '011001': 'Z', '011010': 'a', '011011': 'b', '011100': 'c', '011101': 'd',
                      '011110': 'e', '011111': 'f', '100000': 'g', '100001': 'h', '100010': 'i',
                      '100011': 'j', '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n',
                      '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r', '101100': 's',
                      '101101': 't', '101110': 'u', '101111': 'v', '110000': 'w', '110001': 'x',
                      '110010': 'y', '110011': 'z', '110100': '0', '110101': '1', '110110': '2',
                      '110111': '3', '111000': '4', '111001': '5', '111010': '6', '111011': '7',
                      '111100': '8', '111101': '9', '111110': '+', '111111': '/'}
# Criando as conversões reversas para o dicionario (chave: caractere | valor: binario)
dic_place_holder = {}
for valor_bin, caractere in dicionario_base_64.items():
    dic_place_holder[caractere] = valor_bin
dicionario_base_64.update(dic_place_holder)
dic_place_holder.clear()
# Recomendação para aprender mais sobre UTF-8 / base_64: https://www.youtube.com/watch?v=RNL8m2voKbI

def codificar_base_64(texto):
    if not texto:
        return dicionarios.retorna_erro_mensagem()
    texto_codificado = ''
    indice_codigo = 24
    texto_UTF8 = codificar_texto_para_UTF8(texto)
    tamanho_codigo = len(texto_UTF8)
    while indice_codigo <= tamanho_codigo:  # Construindo o texto base 64... cada loop iterando sobre 24 digitos (4 blocos de 6).
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 24: indice_codigo - 18]]
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 18: indice_codigo - 12]]
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 12: indice_codigo - 6]]
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 6: indice_codigo]]
        indice_codigo += 24
    # Finalizando o enconding... 
    n_digitos_finais = indice_codigo - tamanho_codigo
    if n_digitos_finais == 24:  # Todo o texto ja passou pelo encode, retornar o código base 64
        pass
    elif n_digitos_finais == 16:  # Para completar, faltou 16 digitos. Completar antepenultimo bloco com mais 4 zeros e adicionar 2 iguais no final.
        texto_UTF8 += '0000'
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 24: indice_codigo - 18]]
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 18: indice_codigo - 12]] + '=='
    else:  # Faltou 8 digitos para completar. Antepenultimo recebe 2 zeros, e bloco faltante será substituido por um "=".
        texto_UTF8 += '00'
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 24: indice_codigo - 18]]
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 18: indice_codigo - 12]]
        texto_codificado += dicionario_base_64[texto_UTF8[indice_codigo - 12: indice_codigo - 6]] + '='
    return texto_codificado


def traduzir_base_64(texto):
    if not texto:
        return dicionarios.retorna_erro_mensagem()
    texto_traduzido = ''
    i = 0
    quant_de_iguais = texto.count('=')
    codigo_binario = transformar_texto_para_binario_6bits(texto)
    tamanho_codigo_bin = len(codigo_binario)
    if quant_de_iguais == 1:
        codigo_binario = codigo_binario[:tamanho_codigo_bin - 2]
    elif quant_de_iguais == 2:
        codigo_binario = codigo_binario[:tamanho_codigo_bin - 4]
    while i <= tamanho_codigo_bin:
        if codigo_binario[i:i+5] == '11110':
            bin_atual = codigo_binario[i+5:i+8] + codigo_binario[i+10:i+16] + codigo_binario[i+18:i+24] + codigo_binario[i+26:i+32]
            i += 32
        elif codigo_binario[i:i+4] == '1110':
            bin_atual = codigo_binario[i+4:i+8] + codigo_binario[i+10:i+16] + codigo_binario[i+18:i+24]
            i += 24
        elif codigo_binario[i:i+3] == '110':
            bin_atual = codigo_binario[i+3:i+8] + codigo_binario[i+10:i+16]
            i += 16
        else:
            bin_atual = codigo_binario[i+1:i+8]
            i += 8
        texto_traduzido += chr(bases_numericas.converter_binario_para_decimal(bin_atual))
    texto_traduzido = texto_traduzido.rstrip('\x00')
    return texto_traduzido

def codificar_texto_para_UTF8(texto):
    codigo_final_utf8 = ''
    for caractere in texto:
        num_binario = bases_numericas.converter_decimal_para_binario(ord(caractere))
        if len(num_binario) <= 7:
            codigo_final_utf8 += transformar_7bits_UTF8(num_binario)
        elif len(num_binario) <= 11:
            codigo_final_utf8 += transformar_11bits_UTF8(num_binario)
        elif len(num_binario) <= 16:
            codigo_final_utf8 += transformar_16bits_UTF8(num_binario)
        elif len(num_binario) <= 21:
            codigo_final_utf8 += transformar_21bits_UTF8(num_binario)
        else:
            pass  # ERRO AQUI (o valor digitado pelo usuário excedeu o números de bits possiveis)...
    return codigo_final_utf8
        

def transformar_texto_para_binario_6bits(texto):
    string_binario = ''
    for caractere in texto:
        if caractere != '=':
            string_binario += dicionario_base_64[caractere]
    return string_binario

def transformar_7bits_UTF8(num_binario):
    return '0' * (8 - len(num_binario)) + num_binario

def transformar_11bits_UTF8(num_binario):
    num_binario = '0' * (11 - len(num_binario)) + num_binario
    return '110' + num_binario[:5] + '10' + num_binario[5:]

def transformar_16bits_UTF8(num_binario):
    num_binario = '0' * (16 - len(num_binario)) + num_binario
    return '1110' + num_binario[:4] + '10' + num_binario[4:10] + '10' + num_binario[10:]

def transformar_21bits_UTF8(num_binario):
    num_binario = '0' * (21 - len(num_binario)) + num_binario
    return '11110' + num_binario[:3] + '10' + num_binario[3:9] + '10' + num_binario[9:15] + '10' + num_binario[15:]

