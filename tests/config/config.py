# config.py - Variáveis em ambiente de teste

# Configurações gerais de arquivos
FILE_CONFIG = {
    "arq_log_file": r"\log_atualizacao.txt", # Nome padrão do relatório que será utilizado
    "arq_rel_pendentes_ga": r"\NC_BASE_ORDENS_PENDENTES_GA.xlsx",
    "arq_rel_pendentes_gb": r"\NC_ORDENS_PENDENTES_GB.xlsx",
    "arq_img_pendentes_ga": r"\PEND_GA.png",
    "arq_img_pendentes_gb": r"\PEND_GB.png"
}

# Diretórios de destino e origem
DIRECTORIES = {
    "dir_log_file": r"C:\FELIPE\py_testes\pipeline_relatorios\logs",
    "dir_origem_rel": r"C:\FELIPE\py_testes\pipeline_relatorios\data\start",
    "dir_final_rel": r"C:\FELIPE\py_testes\pipeline_relatorios\data\output",
    "dir_final_img": r"C:\FELIPE\py_testes\pipeline_relatorios\images"
}

WORKSHEET_TAB = {
    "tab_pendentes_ga": "Painel", # Aba a ser utilizada para tirar o print
    "tab_pendentes_gb": "Evolução-Mes"
}

# Definições de intervalo de planilha (para exportar como imagem)
WORKSHEET_RANGE = {
    "range_pendentes_ga": "B1:AB102", # Intervalo que será utilizado para tirar o print
    "range_pendentes_gb": "C9:Q64"
}

# Assunto do contexto de log
LOG_CONTEXT_CONFIG = {
    "pendente_ga": "GA_PEND", # Assunto que será utilizado como parametro na geração dos LOGs de execução
    "pendente_ga": "GA_PEND"
}

# Configuração de logs (Opcional, pode se expandir conforme necessário)
LOG_CONFIG = {
    "log_file_path": FILE_CONFIG["arq_log_file"],
    "log_level": "INFO",  # Exemplo: 'INFO', 'ERROR', etc.
    "test_ambient": "TEST",
    "prod_ambient": "PROD"
}
