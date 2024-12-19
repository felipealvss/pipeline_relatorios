import paramiko
import os
from stat import S_ISDIR

# Função para verificar se um caminho é um diretório
def is_dir(ftp, path):
    try:
        # Tentar obter status do arquivo/diretório
        ftp.stat(path)
    except FileNotFoundError:
        return False
    return True

# Conectar via SFTP e baixar os arquivos
def download_files_from_sftp():
    # Informações de conexão
    host = '10.154.78.75'
    port = 22
    username = 'sftpce'
    keyfile = r'C:\FELIPE\Filezilla\chave\keyFileZila.ppk'
    remote_dir = '/synergia/archivos/batch/lst/diarios'
    local_dir = r'C:\FELIPE\Filezilla\extracoes\ARQ_REL'
    file_pattern = 'COELCE_elaazisysd00_Ligacao_Nova_Ordens_*'

    # Carregar chave privada
    private_key = paramiko.RSAKey.from_private_key_file(keyfile)

    # Inicializar cliente SFTP
    try:
        # Criar cliente SSH e se conectar
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, pkey=private_key)

        sftp = paramiko.SFTPClient.from_transport(transport)

        # Listar arquivos no diretório remoto
        files = sftp.listdir(remote_dir)
        print(f"Arquivos encontrados no diretório remoto {remote_dir}: {files}")

        # Filtrar os arquivos que correspondem ao padrão
        files_to_download = [f for f in files if f.startswith('COELCE_elaazisysd00_Ligacao_Nova_Ordens_')]
        print(f"Arquivos a serem baixados: {files_to_download}")

        # Verificar e criar diretórios locais
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        # Baixar os arquivos
        for file in files_to_download:
            remote_file_path = os.path.join(remote_dir, file)
            local_file_path = os.path.join(local_dir, file)

            # Verificar se o arquivo remoto é um diretório
            if not is_dir(sftp, remote_file_path):
                # Baixar o arquivo se não for um diretório
                print(f"Baixando: {file}")
                sftp.get(remote_file_path, local_file_path)

        # Fechar a conexão SFTP
        sftp.close()
        transport.close()

    except Exception as e:
        print(f"Erro durante a transferência de arquivos: {e}")

if __name__ == "__main__":
    download_files_from_sftp()