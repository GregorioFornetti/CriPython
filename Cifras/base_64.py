import Cifras.bases_numericas as bases_numericas
import Cifras.utf8 as utf8
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
    texto_UTF8 = utf8.codificar_texto_para_UTF8(texto)
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
    codigo_binario = transformar_textoBase64_em_codigo_binario(texto)
    if not codigo_binario:  # Um caractere fora da tabela da base 64 foi encontrado.
        return dicionarios.retorna_erro_mensagem()
    
    quant_de_iguais = texto.count('=')
    if quant_de_iguais == 1:
        codigo_binario = codigo_binario[:len(codigo_binario) - 2]
    elif quant_de_iguais == 2:
        codigo_binario = codigo_binario[:len(codigo_binario) - 4]

    return utf8.decodificar_UTF8_para_texto(codigo_binario)
        

def transformar_textoBase64_em_codigo_binario(texto):
    string_binario = ''
    if len(texto) % 4 != 0:
        return False
    
    for caractere in texto:
        if caractere != '=':
            try:
                string_binario += dicionario_base_64[caractere]
            except:
                return False
    return string_binario

def codif2_base_64(texto):
    codigo_hex_texto = bytes(texto, encoding='utf-8').hex()
    codigo_base64 = ''
    tamanho_codigo_hex = len(codigo_hex_texto)
    i = 5
    while i < tamanho_codigo_hex:
        bloco_bin_atual = ''
        for j in range(5, -1, -1):
            bloco_bin_atual += bases_numericas.converter_hexa_para_binario(codigo_hex_texto[i - j])
        
        for j in range(4):
            codigo_base64 += dicionario_base_64[bloco_bin_atual[j * 6:(j + 1) * 6]]
        i += 6
    restante = i - tamanho_codigo_hex
    if restante == 3:
        codigo_bin_final = ''
        for j in range(tamanho_codigo_hex - 2, tamanho_codigo_hex):
            codigo_bin_final += bases_numericas.converter_hexa_para_binario(codigo_hex_texto[j])
        codigo_bin_final += '0000'
        codigo_base64 += dicionario_base_64[codigo_bin_final[:6]] + dicionario_base_64[codigo_bin_final[6:]] + '=='
    elif restante == 1:
        codigo_bin_final = ''
        for j in range(tamanho_codigo_hex - 4, tamanho_codigo_hex):
            codigo_bin_final += bases_numericas.converter_hexa_para_binario(codigo_hex_texto[j])
        codigo_bin_final += '00'
        codigo_base64 += dicionario_base_64[codigo_bin_final[:6]] + dicionario_base_64[codigo_bin_final[6:12]] + dicionario_base_64[codigo_bin_final[12:]] + '='
    return codigo_base64

