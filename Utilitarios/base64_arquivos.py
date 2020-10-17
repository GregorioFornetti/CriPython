import dicionarios
import Cifras.base_64 as base_64

def encoding_base64_arquivos(endereco_arquivo):
    try:
        with open(endereco_arquivo, 'rb') as arquivo:
            texto_bin = arquivo.read()
            return base_64.codificar_arquivo_base_64(texto_bin)
    except:
        return dicionarios.retorna_erro_arquivo()