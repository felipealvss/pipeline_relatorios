from datetime import datetime
import src.functions.envia_email as envia_email # função que organiza o envio do email
import src.emails.config.config as EmailConfig  # Importando as constantes
import src.emails.assinatura as assinatura

def enviar_relatorio_por_email(destinatario=None, relatorio_path=None, imagem_path=None):
    """
    Função que envia o relatório gerado por e-mail com a data de hoje no assunto.

    Args:
    - destinatario (str): Endereço de e-mail do destinatário.
    - relatorio_path (str): Caminho do arquivo Excel (relatório gerado).
    - imagem_path (str): Caminho da imagem a ser embutida no corpo do e-mail.
    """
    destinatario = destinatario or EmailConfig.DESTINATARIO  # Se destinatário não for fornecido, usa o padrão
    relatorio_path = relatorio_path or EmailConfig.CAMINHO_RETORNO_RELATORIO  # Usar caminho padrão se não fornecido
    imagem_path = imagem_path or EmailConfig.CAMINHO_IMAGEM  # Usar caminho padrão se não fornecido

    # Informações para assinatura
    nome = "João Silva"  # Nome do remetente
    cargo = "Analista de Dados"  # Cargo do remetente
    telefone = "(11) 98765-4321"  # Telefone de contato
    email_empresa = "contato@empresa.com"  # E-mail de contato
    logo_empresa = 'images/logo_empresa.png'  # Logo da empresa (opcional)

    # Formatação do título do e-mail com a data de hoje
    data_atual = datetime.now().strftime('%d/%m/%Y')
    assunto = f"Relatório Gerado - {data_atual}"

    # Corpo do e-mail (HTML)
    corpo = f"""
    <html>
    <body>
        <h1 style="color: #1e90ff; font-size: 24px;">Relatório Gerado - {datetime.now().strftime('%d/%m/%Y')}</h1>
        <p style="color: #666666; font-size: 14px;">Olá,</p>
        <p style="color: #666666; font-size: 14px;">Segue o relatório gerado com as informações solicitadas.</p>
        <p style="color: red; font-weight: bold;">Este é um aviso importante!</p>
        <p><img src="cid:image1" alt="Imagem do relatório"></p>
        <p style="font-family: 'Courier New', monospace; font-size: 16px;">Este texto está com uma fonte personalizada e um estilo diferente.</p>
        <p>Atenciosamente,<br>Equipe de Relatórios</p>
        {assinatura(nome, cargo, telefone, email_empresa, logo_empresa)}
    </body>
    </html>
    """ # Fontes Externas: Muitos clientes de e-mail não carregam fontes externas (como Google Fonts), então é melhor usar fontes comuns, como Arial, Times New Roman, ou Courier New, que são amplamente suportadas.

    # Chamada da função envia_email para enviar o e-mail com anexo e imagem embutida
    envia_email(destinatario, assunto, corpo, relatorio_path, imagem_path)
