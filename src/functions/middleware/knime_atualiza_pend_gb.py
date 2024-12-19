import os
import gc
import logging
import win32com.client as win32
#import src.config.config as config # Configurações de produção
import src.config.tests.config as config # Configurações de teste

def knime_atualiza_pend_gb(assunto, log_file):

    # Configuração do log
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Função para registrar eventos no log
    def log_event(message):
        logging.info(message)
        print(message)

    # Caminhos dos arquivos Excel
    arquivo_origem = os.path.join(
        config.DIRECTORIES["dir_rel_knime"],
        config.FILE_CONFIG["arq_rel_knime"]
    )

    arquivo_destino = os.path.join(
        config.DIRECTORIES["dir_origem_rel"],
        config.FILE_CONFIG["arq_rel_pendentes_gb"]
    )

    # Inicializa o Excel
    excel = None
    try:
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = False  # Excel invisível
        log_event(f"{assunto} Excel inicializado com sucesso.")
    except Exception as e:
        log_event(f"{assunto} Falha ao inicializar o Excel: {str(e)}")
        if excel:
            excel.Quit()
        exit()

    try:
        # Carregar a planilha de origem e destino
        wb_origem = excel.Workbooks.Open(arquivo_origem)
        wb_destino = excel.Workbooks.Open(arquivo_destino)

        # Verificar se a aba "knime_pend_gb" existe na planilha de destino, senão criá-la
        aba_destino = None
        for sheet in wb_destino.Sheets:
            if sheet.Name == 'Relação das Ordens':
                aba_destino = sheet
                break

        # Se a aba "knime_pend_gb" não existir, criá-la
        if aba_destino is None:
            aba_destino = wb_destino.Sheets.Add()
            aba_destino.Name = 'Relação das Ordens'

        # Acessar as abas desejadas
        aba_origem = wb_origem.Sheets('GB')

        # 1. Limpar os dados da aba "knime_pend_gb" a partir da linha 8
        ultima_linha_destino = aba_destino.Cells(aba_destino.Rows.Count, 3).End(-4162).Row  # Última linha com dados na coluna C

        # Limpar apenas os dados a partir da linha 8 (sem afetar o cabeçalho)
        if ultima_linha_destino >= 8:
            aba_destino.Range(aba_destino.Cells(8, 3), aba_destino.Cells(ultima_linha_destino, aba_destino.Columns.Count)).ClearContents()
            log_event(f"{assunto} Dados da linha 8 até a última linha ({ultima_linha_destino}) foram limpos.")
        else:
            log_event(f"{assunto} Não há dados abaixo da linha 8 para limpar.")

        # 2. Captura dos dados da aba "GB"
        # Determina a última linha e a última coluna da planilha de origem
        ultima_linha = aba_origem.Cells(aba_origem.Rows.Count, 1).End(-4162).Row  # Última linha com dados
        ultima_coluna = aba_origem.Cells(1, aba_origem.Columns.Count).End(-4159).Column  # Última coluna com dados

        # Adicionando log para verificar a captura dos intervalos
        log_event(f"{assunto} Última linha com dados: {ultima_linha}")
        log_event(f"{assunto} Última coluna com dados: {ultima_coluna}")

        # Captura os dados no intervalo identificado
        dados_origem = aba_origem.Range(aba_origem.Cells(1, 1), aba_origem.Cells(ultima_linha, ultima_coluna)).Value

        # Converte os dados para uma lista de listas para permitir alterações
        dados_origem = [list(row) for row in dados_origem]

        # Adicionando mais detalhes de depuração para verificar os dados
        if dados_origem:
            log_event(f"{assunto} Dados de origem capturados com sucesso.")
            num_linhas = len(dados_origem)
            num_colunas = len(dados_origem[0])
            log_event(f"{assunto} Dados de origem possuem {num_linhas} linhas e {num_colunas} colunas.")
        else:
            log_event(f"{assunto} Nenhum dado encontrado na origem.")

        # Garantir que a coluna A (numero_ordem) seja tratada como texto
        for i in range(1, ultima_linha + 1):
            # Garantir que cada célula na coluna A seja tratada como texto, mantendo 10 caracteres
            numero_ordem = str(dados_origem[i - 1][0]).zfill(10)  # Adiciona zeros à esquerda, se necessário
            dados_origem[i - 1][0] = numero_ordem  # Substitui o valor na matriz

        # Agora, tentamos copiar os dados para a aba de destino a partir da célula C8
        if dados_origem:
            # Copiar apenas o número correto de linhas e colunas
            aba_destino.Range(aba_destino.Cells(8, 3), aba_destino.Cells(8 + num_linhas - 1, ultima_coluna + 2)).Value = dados_origem
            log_event(f"{assunto} Dados copiados para '{aba_destino.Name}' a partir da célula C8.")

            # Formatar a coluna A como texto
            aba_destino.Range('A:A').NumberFormat = '@'  # Formato de texto para a coluna A

            # 3. Excluir a tabela existente, se houver
            for table in aba_destino.ListObjects:
                table.Delete()

            # 4. Criar uma nova tabela a partir do intervalo de dados copiados
            tabela = aba_destino.ListObjects.Add(1, aba_destino.Range(aba_destino.Cells(8, 3), aba_destino.Cells(8 + num_linhas - 1, ultima_coluna + 2)))

            tabela.Name = "GB"

            log_event(f"{assunto} Tabela recriada com sucesso na aba '{aba_destino.Name}'.")

            # Estilo do cabeçalho
            tabela.HeaderRowRange.Interior.Color = 0x494529  # Cor para o cabeçalho
            tabela.HeaderRowRange.Font.Color = 0xFFFFFF  # Texto branco no cabeçalho

            # Estilo das colunas (cor branca para as colunas)
            for col in tabela.ListColumns:
                col.DataBodyRange.Interior.Color = 0xFFFFFF  # Cor branca para as colunas

            log_event(f"{assunto} Estilo personalizado aplicado à tabela '{tabela.Name}'.")

        # 5. Validação: verificar o número de linhas e colunas após a cópia
        try:
            linhas_destino = aba_destino.UsedRange.Rows.Count
            colunas_destino = aba_destino.UsedRange.Columns.Count

            # Log detalhado da validação
            log_event(f"{assunto} Validação após cópia: {linhas_destino} linhas e {colunas_destino} colunas na aba '{aba_destino.Name}'.")

            # if linhas_destino == num_linhas and colunas_destino == num_colunas:
            #     log_event(f"{assunto} Validação bem-sucedida: {linhas_destino} linhas e {colunas_destino} colunas copiados para 'knime_pend_gb'.")
            # else:
            #     log_event(f"{assunto} Validação falhou: Dados copiados não correspondem ao esperado ({linhas_destino} linhas, {colunas_destino} colunas).")
        except Exception as e:
            log_event(f"{assunto} Erro durante a validação dos dados copiados: {str(e)}")

        # # 6. Ocultar a aba "knime_pend_gb"
        # aba_destino.Visible = False

        # Salvar a planilha de destino
        wb_destino.Save()

    except Exception as e:
        log_event(f"{assunto} Erro durante a atualização: {str(e)}")

    finally:
        # Fechar as planilhas se os objetos COM forem válidos
        if wb_origem is not None:
            wb_origem.Close(False)  # Fechar sem salvar
        if wb_destino is not None:
            wb_destino.Close(False)  # Fechar sem salvar

        # Fechar o Excel
        if excel is not None:
            excel.Quit()
            # Libera objetos COM de forma explícita
            del wb_origem
            del wb_destino
            del excel
            gc.collect()  # Força a coleta de lixo para liberar objetos COM não utilizados

        # Finalização
        log_event(f"{assunto} Atualização executada com sucesso!")
