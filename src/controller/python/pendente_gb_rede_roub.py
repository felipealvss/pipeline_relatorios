import os
import logging
#import src.config.config as config # Configurações de produção
import src.config.tests.config as config # Configurações de teste
from src.functions.atualiza_relatorio import atualiza_relatorio
from src.functions.move_relatorio import move_relatorio
from src.functions.extrai_imagem_relatorio import extrai_imagem_relatorio
from src.functions.middleware.knime_atualiza_pend_gb import knime_atualiza_pend_gb
from src.functions.middleware.knime_atualiza_pend_gb_rede_roubada import knime_atualiza_pend_gb_rede_roubada

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
            assunto=config.LOG_CONTEXT_CONFIG['pendente_gb'],
            origin_excel_file=config.DIRECTORIES['dir_origem_rel'],
            name_excel_file=config.FILE_CONFIG['arq_rel_pendentes_gb_rede_roub'],
            log_file=log_file
        )
    except Exception as e:
        log_event(f"Erro ao atualizar relatório: {e}")
        raise

def mover_relatorio(log_file):
    try:
        move_relatorio(
            assunto=config.LOG_CONTEXT_CONFIG['pendente_gb'],
            origin_excel_file=config.DIRECTORIES['dir_origem_rel'],
            name_excel_file=config.FILE_CONFIG['arq_rel_pendentes_gb_rede_roub'],
            dest_dir=config.DIRECTORIES['dir_final_rel'],
            log_file=log_file
        )
    except Exception as e:
        log_event(f"Erro ao mover relatório: {e}")
        raise
