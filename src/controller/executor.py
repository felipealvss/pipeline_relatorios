import os
import time
import logging
from datetime import datetime
#import src.config.config as config # Configurações de produção
import src.config.tests.config as config # Configurações de teste
import src.controller.python.pendente_ga as pend_ga
import src.controller.python.pendente_gb as pend_gb
import src.controller.python.pendente_gb_rede_roub as pend_gb_rede_roub
import src.controller.python.pendente_gd_gagb as pend_gd_gagb

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

def executar_processo_relatorio(log_file):
    try:
        momento_ini = datetime.now()
        print(f'Momento início processo: {momento_ini}\n')

        log_event("Iniciando o processo de atualização de dados do KNIME.")
        pend_gb.knime_atualizar_pend_gb(log_file)
        time.sleep(3)
        pend_gb.knime_atualizar_pend_gb_rede_roubada(log_file)

        log_event("atualização de dados do KNIME finalizada.")
        time.sleep(3)

        log_event("Iniciando o processo de atualização de relatório.")
        pend_ga.atualizar_relatorio(log_file)
        time.sleep(3)
        pend_gb.atualizar_relatorio(log_file)
        time.sleep(3)
        pend_gb_rede_roub.atualizar_relatorio(log_file)
        time.sleep(3)
        pend_gd_gagb.atualizar_relatorio(log_file)

        log_event("Atualização finalizada.")
        time.sleep(3)

        log_event("Iniciando o processo de extrair imagem.")
        pend_ga.extrair_imagem_relatorio(log_file)
        time.sleep(3)
        pend_gb.extrair_imagem_relatorio(log_file)
        time.sleep(3)
        pend_gd_gagb.extrair_imagem_relatorio(log_file)

        log_event("Extração finalizada.")
        time.sleep(3)

        log_event("Iniciando o processo de mover o relatório.")
        pend_ga.mover_relatorio(log_file)
        time.sleep(3)
        pend_gb.mover_relatorio(log_file)
        time.sleep(3)
        pend_gb_rede_roub.mover_relatorio(log_file)
        time.sleep(3)
        pend_gd_gagb.mover_relatorio(log_file)

        momento_fim = datetime.now()
        tempo_total = momento_fim - momento_ini
        print(f'Momento fim processo: {momento_fim}')
        print(f'Tempo total processo: {tempo_total}\n')

        log_event("Processo completo.")
    except Exception as e:
        log_event(f"Ocorreu um erro durante o processo: {e}")
        raise
