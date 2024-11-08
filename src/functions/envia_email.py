import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import src.emails.config.config as EmailConfig  # Importando as constantes

def envia_email(destinatario, assunto, corpo, anexo_path, imagem_path):
    """
    Envia um e-mail com anexo e imagem embutida no corpo.

    Args:
    - destinatario (str): Endereço de e-mail do destinatário.
    - assunto (str): Assunto do e-mail.
    - corpo (str): Corpo do e-mail (em formato HTML).
    - anexo_path (str): Caminho do arquivo Excel a ser anexado.
    - imagem_path (str): Caminho da imagem a ser embutida no corpo.
    """
    # Criação do objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = EmailConfig.EMAIL_USUARIO
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo do e-mail
    msg.attach(MIMEText(corpo, 'html'))

    # Anexo (relatório Excel)
    if anexo_path and os.path.exists(anexo_path):
        with open(anexo_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(anexo_path)}')
            msg.attach(part)

    # Imagem embutida (como CID no corpo do e-mail)
    if imagem_path and os.path.exists(imagem_path):
        with open(imagem_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)

    # Conexão SMTP
    try:
        server = smtplib.SMTP(EmailConfig.SMTP_SERVIDOR, EmailConfig.SMTP_PORTA)
        server.starttls()  # Criptografar a conexão
        server.login(EmailConfig.EMAIL_USUARIO, EmailConfig.EMAIL_SENHA)
        server.sendmail(EmailConfig.EMAIL_USUARIO, destinatario, msg.as_string())
        server.quit()
        print(f"E-mail enviado com sucesso para {destinatario}")
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação. Verifique suas credenciais.")
    except smtplib.SMTPException as e:
        print(f"Falha ao enviar e-mail: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
