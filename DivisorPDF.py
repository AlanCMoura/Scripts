import os
import PyPDF2

def separar_primeira_pagina_pdfs(pasta_origem, pasta_destino):
    # Verifica se a pasta de destino existe, caso contrário, a cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Percorre todos os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        if nome_arquivo.endswith('.pdf'):
            caminho_origem = os.path.join(pasta_origem, nome_arquivo)
            
            with open(caminho_origem, 'rb') as arquivo:
                leitor_pdf = PyPDF2.PdfReader(arquivo)
                escritor_pdf = PyPDF2.PdfWriter()
                
                primeira_pagina = leitor_pdf.pages[0]
                escritor_pdf.add_page(primeira_pagina)
                
                nome_arquivo_destino = f'primeira_pagina_{nome_arquivo}'
                caminho_destino = os.path.join(pasta_destino, nome_arquivo_destino)
                
                with open(caminho_destino, 'wb') as novo_arquivo:
                    escritor_pdf.write(novo_arquivo)
                
                print(f'Primeira página de {nome_arquivo} separada e salva como {nome_arquivo_destino}.')

# Exemplo de uso
pasta_origem = r'C:\\Users\\Dep. Pessoal\\Desktop\\Livros'
pasta_destino = r'C:\\Users\\Dep. Pessoal\\Desktop\\CapasPDF'
separar_primeira_pagina_pdfs(pasta_origem, pasta_destino)