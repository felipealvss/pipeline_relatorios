import os
import logging
#import src.config.config as config # Configurações de produção
import src.config.tests.config as config # Configurações de teste
from src.controller.executor import executar_processo_relatorio

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

def main():

   # Ambiente
   ambient = config.LOG_CONFIG['ambient']
   log_event(f'Ambiente: {ambient} - Arquivo log definido: {log_file}')
 
   # Executar processo de relatório
   executar_processo_relatorio(log_file)

if __name__ == "__main__":
   main()