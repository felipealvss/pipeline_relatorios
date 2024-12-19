import os
import logging
#import src.config.config as config # Configurações de produção
import src.config.tests.config as config # Configurações de teste
from src.functions.atualiza_relatorio import atualiza_relatorio
from src.functions.move_relatorio import move_relatorio
from src.functions.extrai_imagem_relatorio import extrai_imagem_relatorio

# Arquivo log
log_file = os.path.join(
   config.DIRECTORIES["dir_log_file"],
   config.FILE_CONFIG["arq_log_file"]
)

# Configuração do log
logging.basicConfig(filename=log_file, level=logging.INFO, 
                     format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Função para registrar eventos no log
def log_event(message):
   logging.info(message)
   print(message)

def atualizar_relatorio(log_file):
    try:
        atualiza_relatorio(
            assunto=config.LOG_CONTEXT_CONFIG['pendente_ga'],
            origin_excel_file=config.DIRECTORIES['dir_origem_rel'],
            name_excel_file=config.FILE_CONFIG['arq_rel_pendentes_ga'],
            log_file=log_file
        )
    except Exception as e:
        log_event(f"Erro ao atualizar relatório: {e}")
        raise

def extrair_imagem_relatorio(log_file):
    try:
        extrai_imagem_relatorio(
            assunto=config.LOG_CONTEXT_CONFIG['pendente_ga'],
            caminho_arquivo_excel=config.DIRECTORIES['dir_origem_rel'],
            nome_arquivo_excel=config.FILE_CONFIG['arq_rel_pendentes_ga'],
            caminho_arquivo_imagem=config.DIRECTORIES['dir_final_img'],
            nome_arquivo_imagem=config.FILE_CONFIG['arq_img_pendentes_ga'],
            aba=config.WORKSHEET_TAB['tab_pendentes_ga'],
            intervalo=config.WORKSHEET_RANGE['range_pendentes_ga'],
            log_file=log_file
        )
    except Exception as e:
        log_event(f"Erro ao extrair imagem do relatório: {e}")
        raise

def mover_relatorio(log_file):
    try:
        move_relatorio(
            assunto=config.LOG_CONTEXT_CONFIG['pendente_ga'],
            origin_excel_file=config.DIRECTORIES['dir_origem_rel'],
            name_excel_file=config.FILE_CONFIG['arq_rel_pendentes_ga'],
            dest_dir=config.DIRECTORIES['dir_final_rel'],
            log_file=log_file
        )
    except Exception as e:
        log_event(f"Erro ao mover relatório: {e}")
        raise
