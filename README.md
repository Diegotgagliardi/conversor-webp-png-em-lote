# 🖼️ WebP to PNG Batch Converter

Um script simples e eficiente em Python para converter **imagens `.webp` em `.png`** em massa, com suporte a **seletor de pastas via interface gráfica**.

Ideal para uso pessoal ou profissional, como organização de imagens de e-commerce, acervo de produtos ou otimização de assets visuais.

---

## 🚀 Funcionalidades

- Conversão em lote de `.webp` para `.png`
- Preserva a qualidade da imagem (RGBA)
- Interface para seleção da pasta com um clique (via `tkinter`)
- Cria uma subpasta automática chamada `convertidas` para armazenar as novas imagens

---

## 🛠️ Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas:
  - [`Pillow`]

### 📦 Instalação das dependências:

pip install pillow

Como usar
Clone ou baixe este repositório.

Coloque o script converter_webp_para_png.py em qualquer pasta.

Execute com:
python converter_webp_para_png.py
Será aberta uma janela para selecionar a pasta com imagens .webp.

O script criará uma subpasta convertidas com todas as imagens .png.

Exemplo de uso
> python converter_webp_para_png.py
✅ Convertido: cadeira_01.webp → cadeira_01.png
✅ Convertido: cadeira_02.webp → cadeira_02.png

🎉 Conversão finalizada!
Imagens salvas em: C:/Users/Diego/Desktop/Imagens/convertidas
