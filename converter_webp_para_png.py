import os
from PIL import Image
from tkinter import Tk, filedialog

# Abre uma janela para o usuário escolher a pasta
Tk().withdraw()  # Esconde a janela principal do Tkinter
pasta_origem = filedialog.askdirectory(title="Selecione a pasta com imagens WebP")

if not pasta_origem:
    print("❌ Nenhuma pasta selecionada. Encerrando...")
    exit()

# Extensões permitidas
extensao_origem = ".webp"
extensao_destino = ".png"

# Cria uma nova pasta para as imagens convertidas (dentro da pasta escolhida)
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
            print(f"✅ Convertido: {nome_arquivo} → {novo_nome}")

print("\n🎉 Conversão finalizada!")
print(f"Imagens salvas em: {pasta_destino}")
