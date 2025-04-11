import os
from PIL import Image

# Caminho da pasta com as imagens (use raw string com 'r' antes)
pasta_origem = r"C:\Users\user1\OneDrive\Desktop\ConversorDeFotos\Parte1"

# Extensões permitidas
extensao_origem = ".webp"
extensao_destino = ".png"

# Cria uma nova pasta para as imagens convertidas (chamada "convertidas")
pasta_destino = os.path.join(pasta_origem, "convertidas")
os.makedirs(pasta_destino, exist_ok=True)

# Converte cada arquivo
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.lower().endswith(extensao_origem):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
        novo_nome = nome_arquivo.replace(extensao_origem, extensao_destino)
        caminho_novo = os.path.join(pasta_destino, novo_nome)

        with Image.open(caminho_arquivo) as img:
            img.convert("RGBA").save(caminho_novo, "PNG")
            print(f"Convertido: {nome_arquivo} → {novo_nome}")

print("\n✅ Conversão finalizada.")