from PIL import Image

# Abrir a imagem
imagem = Image.open('logo.jpg')

# Definir a área de corte (esquerda, superior, direita, inferior)
area = area = (500, 500, 800, 800)

# Cortar a imagem
imagem_corte = imagem.crop(area)

# Salvar a imagem cortada
imagem_corte.save('exemplo_corte.jpg')

