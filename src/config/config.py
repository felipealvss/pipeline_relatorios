# config.py - Variáveis em ambiente de produção

# Configurações gerais de arquivos
FILE_CONFIG = {
    "arq_log_file": "log_atualizacao.txt", # Nome padrão do relatório que será utilizado
    "arq_rel_pendentes_ga": "",
    "arq_rel_pendentes_gb": "",
    "arq_img_pendentes_ga": "",
    "arq_img_pendentes_gb": ""
}

# Diretórios de destino e origem
DIRECTORIES = {
    "dir_log_file": "C:/FELIPE/py_testes/pipeline_relatorios/logs",
    "dir_origem_rel": "C:/FELIPE/py_testes/pipeline_relatorios/data/start",
    "dir_final_rel": "C:/FELIPE/py_testes/pipeline_relatorios/data/output",
    "dir_final_img": "C:/FELIPE/py_testes/pipeline_relatorios/images"
}

WORKSHEET_TAB = {
    "tab_pendentes_ga": "", # Aba a ser utilizada para tirar o print
    "tab_pendentes_gb": ""
}

# Definições de intervalo de planilha (para exportar como imagem)
WORKSHEET_RANGE = {
    "range_pendentes_ga": "", # Intervalo que será utilizado para tirar o print
    "range_pendentes_gb": ""
}

# Assunto do contexto de log
LOG_CONTEXT_CONFIG = {
    "pendente_ga": "GA_PEND", # Assunto que será utilizado como parametro na geração dos LOGs de execução
    "pendente_gb": "GB_PEND"
}

# Configuração de logs (Opcional, pode se expandir conforme necessário)
LOG_CONFIG = {
    "log_file_path": FILE_CONFIG["arq_log_file"],
    "log_level": "INFO",  # Exemplo: 'INFO', 'ERROR', etc.
    "ambient": "PROD"
}
