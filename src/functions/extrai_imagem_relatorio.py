import os
import logging
import xlwings as xw
from PIL import ImageGrab
import time

def extrai_imagem_relatorio(assunto, nome_arquivo_excel, caminho_arquivo_excel, nome_arquivo_imagem, caminho_arquivo_imagem, log_file, intervalo, aba):

    # Configurações de Excel
    arquivo_excel = os.path.join(nome_arquivo_excel, caminho_arquivo_excel)

    # Configurações de Imagem
    arquivo_imagem = os.path.join(nome_arquivo_imagem, caminho_arquivo_imagem)

    # Configuração do log
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Função para registrar eventos no log
    def log_event(message):
        logging.info(message)
        print(message)

    # Abrir o Excel com xlwings
    app = xw.App(visible=False)  # Define o Excel em modo invisível
    wb = app.books.open(arquivo_excel)

    # Seleciona a planilha onde a área será exportada
    ws = wb.sheets[f'{aba}']  # Substitua pelo nome correto da aba

    # Definir a área da planilha a ser exportada (ajuste conforme necessário)
    intervalo_visivel = ws.range(intervalo)  # Exemplo: "C9:Q64"

    # Copiar a área como imagem para a área de transferência
    intervalo_visivel.api.CopyPicture(Format=2)  # 2 é xlPicture (formato de imagem)

    # Aguardar para garantir que a cópia foi processada corretamente
    time.sleep(1)  # Pausa de 1 segundo

    # Capturar a imagem da área de transferência
    img = ImageGrab.grabclipboard()  # Isso pega a imagem da área de transferência

    if img is not None:
        # Salvar a imagem
        img.save(arquivo_imagem, 'PNG')  # Salva como PNG (ou JPG, se preferir)
        log_event(f"{assunto} Imagem exportada com sucesso para: {arquivo_imagem}")
        print(f"{assunto} Imagem exportada com sucesso para: {arquivo_imagem}")
    else:
        log_event(f"{assunto} Erro: Nenhuma imagem encontrada na área de transferência.")
        print(f"{assunto} Erro: Nenhuma imagem encontrada na área de transferência.")

    # Fechar o Excel
    wb.close()
    app.quit()
