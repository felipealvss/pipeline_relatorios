# config.py

# Configurações do servidor SMTP
SMTP_SERVIDOR = 'smtp.gmail.com'  # ou 'smtp-mail.outlook.com' para Outlook
SMTP_PORTA = 587  # Porta para conexão segura (TLS)

# Informações de autenticação do e-mail
EMAIL_USUARIO = 'seu_email@gmail.com'  # Altere para o seu e-mail
EMAIL_SENHA = 'sua_senha_de_app'  # Senha de app ou senha gerada (não a senha normal)

# Destinatário padrão (pode ser alterado no código se necessário)
DESTINATARIO = 'destinatario@exemplo.com'

# Caminhos padrão dos arquivos
CAMINHO_RETORNO_RELATORIO = 'data/output/relatorio_gerado.xlsx'
CAMINHO_IMAGEM = 'images/grafico.png'

# Configuração do assunto do e-mail
ASSUNTO_EMAIL = 'Relatório Gerado - {data_atual}'  # O assunto será dinâmico

# Configurações relacionadas ao envio de e-mails e assinatura
EMAIL_CONFIG = {
    "nome_remetente": "João Silva",  # Nome do remetente
    "cargo_remetente": "Analista de Dados",  # Cargo do remetente
    "telefone_remetente": "(11) 98765-4321",  # Telefone do remetente
    "email_empresa": "contato@empresa.com",  # E-mail de contato
    "logo_empresa_path": "images/logo_empresa.png",  # Caminho para o logo da empresa (opcional)
    
    # Redes sociais para a assinatura (opcional)
    "redes_sociais": {
        "facebook": "https://facebook.com/empresa",
        "twitter": "https://twitter.com/empresa",
        "linkedin": "https://linkedin.com/company/empresa"
    }
}
