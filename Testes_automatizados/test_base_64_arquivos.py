import dicionarios
import Utilitarios.base64_arquivos as base64_arquivos

# ENCODING DE ARQUIVOS BASE64
def test_base64_encoding_arquivos_imagem_pequena_png():
    with open('Arquivos_teste/Cod_imgPNG1.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/ImagemPNG1.png') == codigo_correto

def test_base64_encoding_arquivos_imagem_media_png():
    with open('Arquivos_teste/Cod_imgPNG2.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/ImagemPNG2.png') == codigo_correto

def test_base64_encoding_arquivos_imagem_grande_png():
    with open('Arquivos_teste/Cod_imgPNG3.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/ImagemPNG3.png') == codigo_correto

def test_base64_encoding_arquivos_imagem_pequena_jpg():
    with open('Arquivos_teste/Cod_imgJPG1.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/ImagemJPG1.jpg') == codigo_correto

def test_base64_encoding_arquivos_imagem_media_jpg():
    with open('Arquivos_teste/Cod_imgJPG2.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/ImagemJPG2.jpg') == codigo_correto

def test_base64_encoding_arquivos_imagem_grande_jpg():
    with open('Arquivos_teste/Cod_imgJPG3.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/ImagemJPG3.jpg') == codigo_correto

def test_base64_encoding_arquivos_pdf():
    with open('Arquivos_teste/Cod_PDF.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/TestePDF.pdf') == codigo_correto

def test_base64_encoding_arquivos_txt():
    with open('Arquivos_teste/Cod_TXT.txt', 'r') as arq_texto:
        codigo_correto = arq_texto.read()
    assert base64_arquivos.encoding_base64_arquivos('Arquivos_teste/TesteTXT.txt') == codigo_correto

# DECODING ARQUIVOS BASE64
def test_base64_decoding_arquivos_imagem_pequena_png():
    with open('Arquivos_teste/Cod_imgPNG1.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/ImagemPNG1.png', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_imagem_media_png():
    with open('Arquivos_teste/Cod_imgPNG2.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/ImagemPNG2.png', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_imagem_grande_png():
    with open('Arquivos_teste/Cod_imgPNG3.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/ImagemPNG3.png', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_imagem_pequena_jpg():
    with open('Arquivos_teste/Cod_imgJPG1.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/ImagemJPG1.jpg', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_imagem_media_jpg():
    with open('Arquivos_teste/Cod_imgJPG2.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/ImagemJPG2.jpg', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_imagem_grande_jpg():
    with open('Arquivos_teste/Cod_imgJPG3.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/ImagemJPG3.jpg', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_pdf():
    with open('Arquivos_teste/Cod_PDF.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/TestePDF.pdf', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin

def test_base64_decoding_arquivos_txt():
    with open('Arquivos_teste/Cod_TXT.txt', 'r') as arq_texto:
        codigo_base_64 = arq_texto.read()
    with open('Arquivos_teste/TesteTXT.txt', 'rb') as arq_texto:
        cod_bin = arq_texto.read()
    assert base64_arquivos.decoding_base64(codigo_base_64) == cod_bin
