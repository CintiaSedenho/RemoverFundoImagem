from PIL import Image
import numpy as np

# Abrir a imagem original
original_image = Image.open("BrasilColorido.jpg").convert("RGBA")

# Cortar a imagem para remover a legenda (ajuste se necessário)
# (esquerda, cima, direita, baixo) — estimado como 0, 0, largura, 480
cropped_image = original_image.crop((0, 0, original_image.width, 480))

# Converter para array
data = np.array(cropped_image)

# Separar canais RGBA
r, g, b, a = data[..., 0], data[..., 1], data[..., 2], data[..., 3]

# Máscara para fundo branco (ou quase branco)
background_mask = (r > 240) & (g > 240) & (b > 240)

# Substituir fundo por branco puro
data[background_mask] = [255, 255, 255, 255]

# Criar nova imagem
map_only_image = Image.fromarray(data, mode='RGBA')

# Salvar resultado
map_only_image.save("Brasil_Mapa_SemLegenda_FundoBranco.png")
