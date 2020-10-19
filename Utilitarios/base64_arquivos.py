import dicionarios
import Cifras.base_64 as base_64
import Cifras.bases_numericas as bases_numericas
import os

def encoding_base64_arquivos(endereco_arquivo):
    try:
        with open(endereco_arquivo, 'rb') as arquivo:
            texto_bin = arquivo.read()
            return base_64.codificar_arquivo_base_64(texto_bin)
    except:
        return dicionarios.retorna_erro_arquivo()

def decoding_base64(texto_base64):
    texto_final = []
    if (not texto_base64 or len(texto_base64) % 4 != 0):
        return False
    try:
        for i in range(0, len(texto_base64) - 4, 4):
            texto_bin = ''
            for j in range(4):
                texto_bin += base_64.dicionario_base_64[texto_base64[i + j]]
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[:8]))
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[8:16]))
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[16:]))
        parte_final = texto_base64[-4:]
        if parte_final.count('=') == 2:
            texto_bin = (base_64.dicionario_base_64[parte_final[0]] + base_64.dicionario_base_64[parte_final[1]])[:-4]
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[:8]))
        elif parte_final.count('=') == 1:
            texto_bin = (base_64.dicionario_base_64[parte_final[0]] + base_64.dicionario_base_64[parte_final[1]] + base_64.dicionario_base_64[parte_final[2]])[:-2]
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[:8]))
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[8:]))
        else:
            texto_bin = ''
            for j in range(4):
                texto_bin += base_64.dicionario_base_64[parte_final[j]]
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[:8]))
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[8:16]))
            texto_final.append(bases_numericas.converter_binario_para_decimal(texto_bin[16:]))
        return bytes(texto_final)
    except:
        return False


def decoding_base64_arquivos(endereco_arquivo, dados):
    with open(endereco_arquivo, 'wb') as arquivo:
        texto_bin = decoding_base64(dados)
        if not texto_bin:
            os.remove(endereco_arquivo)
            return dicionarios.retorna_mensagem_erro_salvar()
        arquivo.write(texto_bin)
        return dicionarios.retorna_mensagem_sucesso_salvar()
