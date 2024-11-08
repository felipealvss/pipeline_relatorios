# config.py - Variáveis em ambiente de teste

# Configurações gerais de arquivos
FILE_CONFIG = {
    "arq_log_file": r"\log_atualizacao.txt", # Nome padrão do relatório que será utilizado
    "arq_rel_pendentes_ga": r"",
    "arq_rel_pendentes_gb": r"",
    "arq_img_pendentes_ga": r"",
    "arq_img_pendentes_gb": r""
}

# Diretórios de destino e origem
DIRECTORIES = {
    "dir_log_file": r"",
    "dir_origem_rel": r"",
    "dir_final_rel": r"",
    "dir_final_img": r""
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
    "log_level": "INFO"  # Exemplo: 'INFO', 'ERROR', etc.
}
