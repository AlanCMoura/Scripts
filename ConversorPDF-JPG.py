import fitz
from PIL import Image

# Diretório contendo os arquivos PDF
diretorio_pdf = r'C:\\Users\\Dep. Pessoal\\Desktop\\CapasPDF'

# Diretório de saída para os arquivos JPG convertidos
diretorio_saida = r'C:\\Users\\Dep. Pessoal\\Desktop\\CapasJPG'

# Percorra os arquivos na pasta PDF
for nome_arquivo in os.listdir(diretorio_pdf):
    if nome_arquivo.endswith('.pdf'):
        # Caminho completo para o arquivo PDF
        caminho_pdf = os.path.join(diretorio_pdf, nome_arquivo)

        # Abra o arquivo PDF
        pdf = fitz.open(caminho_pdf)

        # Converta cada página em imagem JPEG
        for num_pagina in range(pdf.page_count):
            pagina = pdf.load_page(num_pagina)
            pixmap = pagina.get_pixmap()
            imagem = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

            # Crie o nome do arquivo JPG com base no nome do arquivo PDF e número da página
            nome_jpg = f'{os.path.splitext(nome_arquivo)[0]}_{num_pagina}.jpg'
            caminho_jpg = os.path.join(diretorio_saida, nome_jpg)

            # Salve a imagem como arquivo JPEG
            imagem.save(caminho_jpg, 'JPEG')

        # Feche o arquivo PDF
        pdf.close()

print('Conversão concluída.')
