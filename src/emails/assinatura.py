from src.emails.config.config import EMAIL_CONFIG  # Importando as configurações de e-mail

def assinatura_padrao(nome=None, cargo=None, telefone=None, email_empresa=None, logo_empresa=None, redes_sociais=None):
    """
    Retorna a assinatura padrão do e-mail em HTML com base nas configurações do config.py.

    Args:
    - nome (str): Nome do remetente (opcional, usa valor do config.py se não passado).
    - cargo (str): Cargo do remetente (opcional, usa valor do config.py se não passado).
    - telefone (str): Número de telefone de contato (opcional, usa valor do config.py se não passado).
    - email_empresa (str): E-mail da empresa (opcional, usa valor do config.py se não passado).
    - logo_empresa (str): Caminho da imagem do logo (opcional, usa valor do config.py se não passado).
    - redes_sociais (dict): Dicionário com links das redes sociais (opcional).

    Returns:
    - str: Assinatura em formato HTML.
    """
    # Usar as configurações do config.py, ou valores passados como argumento
    nome = nome or EMAIL_CONFIG["nome_remetente"]
    cargo = cargo or EMAIL_CONFIG["cargo_remetente"]
    telefone = telefone or EMAIL_CONFIG["telefone_remetente"]
    email_empresa = email_empresa or EMAIL_CONFIG["email_empresa"]
    logo_empresa = logo_empresa or EMAIL_CONFIG["logo_empresa_path"]
    redes_sociais = redes_sociais or EMAIL_CONFIG["redes_sociais"]

    # Estrutura básica da assinatura
    assinatura_html = f"""
    <br><br>
    <p>Atenciosamente,<br>
    <strong>{nome}</strong><br>
    <em>{cargo}</em><br>
    {telefone}<br>
    <a href="mailto:{email_empresa}">{email_empresa}</a></p>
    """
    
    # Se houver logo, incluir no final da assinatura
    if logo_empresa:
        assinatura_html += f"""
        <p><img src="cid:logo_empresa" alt="Logo da Empresa" style="width: 100px; height: auto;"></p>
        """
    
    # Incluir links de redes sociais, se fornecidos
    if redes_sociais:
        assinatura_html += "<p>"
        for rede, link in redes_sociais.items():
            assinatura_html += f'<a href="{link}"><img src="cid:{rede}" alt="{rede}" style="width: 20px; height: auto;"></a> '
        assinatura_html += "</p>"

    return assinatura_html
