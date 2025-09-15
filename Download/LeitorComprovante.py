from PIL import Image #importa a biblioteca PIL para manipulação da imagem.
from pytesseract import pytesseract #importa biblioteca do pytesseract.

#string que irá guardar o texto referente ao caminho do arquivo.
caminho_imagem = 'C:/Users/Root/Pictures/image1.jpeg'

'''
Primeiro vamos usar a função open da biblioteca PIL.Image
para abrir o arquivo de imagem e armaezar-lo na variável img,
assim teremos a imagem 'carregada' em memória.
A função pytesseract.image_to_string irá receber a imagem,
o argumento lang é importante, pois se trata do idioma, no caso portugues.
O Tesseract irá extrair o texto da imagem e armazenar na variável: texto_extraido
Em caso de erro, iremos executar as trativas nos campos de except.
'''
try:
    img = Image.open(caminho_imagem)
    texto_extraido = pytesseract.image_to_string(img, lang='por')
    print("--- Texto Extraído do Comprovante ---")
    print(texto_extraido)
    print("-----------------------------------")
except FileNotFoundError:
    print(f"Erro: O arquivo de imagem '{caminho_imagem}' não foi encontrado. Verifique o caminho.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")