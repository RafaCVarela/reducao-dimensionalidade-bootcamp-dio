from PIL import Image

def converterParaCinza(inputPath, outputPath=None):

    img = Image.open(inputPath, mode='r')
    
    largura, altura = img.size
    pixels_originais = img.load()

    img_cinza = Image.new("L", (largura, altura))
    pixels_cinza = img_cinza.load()

    for x in range(largura):
        for y in range(altura):
            r, g, b = pixels_originais[x, y]
            valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels_cinza[x, y] = valor_cinza

    img_cinza.save(outputPath)

def converterParaPretoBranco(inputPath, outputPath=None):

    img = Image.open(inputPath, mode='r')
    pixels_originais = img.load()
    largura, altura = img.size

    img_preto_branco = Image.new('1', (largura, altura))
    novos_pixels = img_preto_branco.load()

    limiar = 127
    
    for x in range(largura):
        for y in range(altura):
            valores = pixels_originais[x, y]
            valor_preto_branco = 1 if valores > limiar else 0
            novos_pixels[x, y] = valor_preto_branco
    
    img_preto_branco.save(outputPath)        



converterParaCinza('lena.png', 'lena_cinza.png')
converterParaPretoBranco('lena_cinza.png', 'lena_preto_branco.png')