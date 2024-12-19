import os
import logging
import time
import gc
import win32com.client as win32

def atualiza_relatorio(assunto, name_excel_file, origin_excel_file, log_file):

    # Configurações do arquivo Excel
    excel_file = os.path.join(origin_excel_file, name_excel_file)

    # Configuração do log
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Função para registrar eventos no log
    def log_event(message):
        logging.info(message)
        print(message)

    # Início do script
    log_event(f"{assunto} Iniciando atualização...")

    # Inicializa o Excel
    try:
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = False  # Excel invisível
        log_event(f"{assunto} Excel inicializado com sucesso.")
    except Exception as e:
        log_event(f"{assunto} Falha ao inicializar o Excel: {str(e)}")
        exit()

    if not os.path.exists(excel_file):
        log_event(f"{assunto} O arquivo {excel_file} não foi encontrado. Verifique o caminho.")
        exit()

    # Tenta abrir o arquivo Excel
    try:
        workbook = excel.Workbooks.Open(excel_file)
        log_event(f"{assunto} Sucesso ao abrir o arquivo: {name_excel_file}")
    except Exception as e:
        log_event(f"{assunto} Erro ao abrir o arquivo: {str(e)}")
        excel.Quit()
        exit()

    # Desabilitar o cálculo automático (melhora o desempenho)
    excel.Calculation = win32.constants.xlCalculationManual

    # Atualiza todos os dados
    log_event(f"{assunto} Iniciando atualização de dados...")
    workbook.RefreshAll()

    # Aguardar 10 segundos para garantir que o refresh foi concluído
    time.sleep(10)

    # Atualizando as Tabelas Dinâmicas (e os gráficos associados)
    for sheet in workbook.Sheets:
        log_event(f"{assunto} Verificando a planilha: {sheet.Name}")
        for pivot_table in sheet.PivotTables():
            try:
                pivot_table.RefreshTable()  # Atualiza cada Tabela Dinâmica
                log_event(f"{assunto} Tabela Dinâmica {pivot_table.Name} atualizada.")
            except Exception as e:
                log_event(f"{assunto} Erro ao atualizar a Tabela Dinâmica {pivot_table.Name}: {str(e)}")
                time.sleep(5)

    # Aguardar até que o Excel termine de atualizar os dados (dinâmico)
    while excel.CalculationState == 1:  # Aguardando cálculo (1 == xlCalculating)
        log_event(f"{assunto} O Excel ainda está calculando. Aguardando conclusão...")
        time.sleep(1)

    # Restaura o cálculo automático
    excel.Calculation = win32.constants.xlCalculationAutomatic

    # Salvar a planilha
    log_event(f"{assunto} Salvando e fechando o arquivo...")
    workbook.Save()

    # Fechar o workbook
    if workbook is not None:
        workbook.Close(SaveChanges=True)
        del workbook

    # Fechar o Excel
    if excel:
        excel.Quit()
        # Libera objetos COM de forma explícita
        gc.collect()  # Força a coleta de lixo para liberar objetos COM não utilizados

    # Finalização
    log_event(f"{assunto} Atualização executada com sucesso!")
