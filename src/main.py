import os
import time
import logging
import src.config.config as config
import src.functions.atualiza_relatorio as att_rel
import src.functions.move_relatorio as mov_rel
import src.functions.extrai_imagem_relatorio as ext_img_rel

def main():

   # Ambiente
   ambient = config.LOG_CONFIG['prod_ambient']
   
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

   log_event(f'Ambiente: {ambient} - Arquivo log definido: {log_file}')

   # ***** PROCESSO RELATORIO PENDENTES GA ***** #

   # Atualiza o Excel
   att_rel.atualiza_relatorio(
      assunto=config.LOG_CONTEXT_CONFIG[''],
      origin_excel_file=config.DIRECTORIES[''],
      name_excel_file=config.FILE_CONFIG[''],
      log_file=log_file
   )
   # Espera 3 segundos
   time.sleep(3)
   # Move ou copia o arquivo
   mov_rel.move_relatorio(
      assunto=config.LOG_CONTEXT_CONFIG[''],
      origin_excel_file=config.DIRECTORIES[''],
      name_excel_file=config.FILE_CONFIG[''],
      dest_dir=config.DIRECTORIES[''],
      log_file=log_file
   )
   # Espera mais 3 segundos
   time.sleep(3)
   # Extrai imagem do arquivo, que será enviada por E-mail
   ext_img_rel.extrai_imagem_relatorio(
      assunto=config.LOG_CONTEXT_CONFIG[''],
      caminho_arquivo_excel=config.DIRECTORIES[''],
      nome_arquivo_excel=config.FILE_CONFIG[''],
      caminho_arquivo_imagem=config.DIRECTORIES[''],
      nome_arquivo_imagem=config.FILE_CONFIG[''],
      aba=config.WORKSHEET_TAB[''],
      intervalo=config.WORKSHEET_RANGE[''],
      log_file=log_file
   )

if __name__ == "__main__":
   main()