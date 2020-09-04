from bases_numericas import converter_decimal_para_binario

# Recomendação para aprender mais sobre UTF-8 / base_64: https://www.youtube.com/watch?v=RNL8m2voKbI

def codificar_texto_para_UTF8(texto):
    codigo_final_utf8 = ''
    for caractere in texto:
        num_binario = converter_decimal_para_binario(ord(caractere))
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
    print(codigo_final_utf8)
        

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

codificar_texto_para_UTF8('a¥')