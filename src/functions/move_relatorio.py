import os
import shutil
import logging
from datetime import datetime

def move_relatorio(assunto, name_excel_file, origin_excel_file, dest_dir, log_file):

    # Configuração do log
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Função para registrar eventos no log
    def log_event(message):
        logging.info(message)
        print(message)

    # Rota completa do arquivo
    excel_file = os.path.join(origin_excel_file, name_excel_file)

    # Verifica se o arquivo de origem existe
    if not os.path.exists(excel_file):
        log_event(f"{assunto} Erro: O arquivo {name_excel_file} não foi encontrado.")
        return

    # Define o ano e mês atual para criar a subpasta
    current_year_month = datetime.now().strftime('%Y%m')
    dest_subfolder = os.path.join(dest_dir, current_year_month)

    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(dest_subfolder):
        os.makedirs(dest_subfolder)

    # Separa o nome do arquivo e a extensão
    arq_name, arq_ext = os.path.splitext(name_excel_file)

    # Define o nome do arquivo com data HOJE no fim do arquivo, padrão YYYYMMDD
    new_filename = f"{arq_name}_{datetime.now().strftime('%Y%m%d')}{arq_ext}"

    new_file_path = os.path.join(dest_subfolder, new_filename)

    # Copia o arquivo para o diretório de destino
    shutil.copy(excel_file, new_file_path)
    log_event(f"{assunto} Arquivo movido e renomeado para: {new_file_path}")
