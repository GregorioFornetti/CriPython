import Cifras.bases_numericas as bases_numericas
import dicionarios

def codificar_texto_para_UTF8(texto):
    if not texto:
        return dicionarios.retorna_erro_mensagem()
    
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
        else:  # "Passou do limite do programa" (é possível ler mais bytes, mas nesse programa não será lido...)
            return dicionarios.retorna_erro_mensagem()
            
    return codigo_final_utf8

def decodificar_UTF8_para_texto(codigo_UTF8):
    tamanho_codigo_UTF8 = len(codigo_UTF8)
    if not codigo_UTF8 or tamanho_codigo_UTF8 % 8 != 0:
        return dicionarios.retorna_erro_mensagem()

    texto_decodicado = ''
    i = 0
    
    while i < tamanho_codigo_UTF8:
        if codigo_UTF8[i:i+5] == '11110':
            bin_atual = codigo_UTF8[i+5:i+8] + codigo_UTF8[i+10:i+16] + codigo_UTF8[i+18:i+24] + codigo_UTF8[i+26:i+32]
            i += 32
        elif codigo_UTF8[i:i+4] == '1110':
            bin_atual = codigo_UTF8[i+4:i+8] + codigo_UTF8[i+10:i+16] + codigo_UTF8[i+18:i+24]
            i += 24
        elif codigo_UTF8[i:i+3] == '110':
            bin_atual = codigo_UTF8[i+3:i+8] + codigo_UTF8[i+10:i+16]
            i += 16
        elif codigo_UTF8[i] == '0':
            bin_atual = codigo_UTF8[i+1:i+8]
            i += 8
        else:
            return dicionarios.retorna_erro_mensagem()
        
        UNICODE_novo_caractere = bases_numericas.converter_binario_para_decimal(bin_atual, tirar_zeros_esq=False)
        if not UNICODE_novo_caractere:
            return dicionarios.retorna_erro_mensagem()
        texto_decodicado += chr(bases_numericas.converter_binario_para_decimal(bin_atual, tirar_zeros_esq=False))
    return texto_decodicado

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
