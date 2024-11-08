# Pipeline de Relatórios - Rotina Administrativa

Este repositório contém um pipeline de dados projetado para trabalhar com arquivos Excel e gerar relatórios de rotina administrativa. O pipeline é composto por diversas etapas, cada uma com uma responsabilidade específica, como a extração de dados, processamento, atualização e movimentação dos arquivos.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
pipeline_relatorios/
│
├── data/                # Diretório com os dados de entrada e saída
│   ├── output/          # Arquivos processados e saídas finais
│   └── start/           # Arquivos de entrada para o pipeline
│
├── images/              # Imagens geradas ou utilizadas no processo
│
├── logs/                # Logs gerados pelas execuções do pipeline
│
├── src/                 # Código-fonte do pipeline
│   ├── config/          # Configurações do projeto
│   │   ├── config.py    # Arquivo de configuração principal
│   │   └── tests/       # Testes de configuração
│   ├── controller/      # Funções de controle ou execução
│   │   └── executor.py  # Funções para execução do pipeline
│   ├── functions/       # Funções específicas para o processamento de dados
│   │   ├── atualiza_relatorio.py  # Atualização de relatórios
│   │   ├── extrai_imagem_relatorio.py  # Extração de imagens de relatórios
│   │   └── move_relatorio.py  # Funções para mover relatórios
│   └── main.py          # Script principal que executa o pipeline
│
├── pyproject.toml       # Arquivo de configuração do projeto Python (Poetry)
├── poetry.lock          # Arquivo de bloqueio das dependências (gerado pelo Poetry)
├── requirements.txt     # Arquivo de requisitos do projeto (geralmente para pip)
├── .gitignore           # Arquivo de exclusão do Git
└── README.md            # Este arquivo
```

## Descrição do Pipeline

O pipeline realiza diversas etapas de processamento de dados provenientes de arquivos Excel. Estas etapas são realizadas de forma sequencial e incluem as seguintes fases:

1. **Extração de Dados**: Arquivos Excel contendo informações de ordens e relatórios são extraídos da pasta `data/start/`. Cada arquivo pode conter dados relevantes para análise e relatórios.

2. **Processamento de Dados**: Após a extração, os dados são processados por scripts específicos. Algumas das operações incluem:
    - Filtragem de dados
    - Atualização de registros
    - Cálculos ou transformações necessárias para gerar os relatórios finais.

3. **Geração de Relatórios**: Com os dados processados, são gerados relatórios em diferentes formatos. Imagens ou gráficos podem ser extraídos ou gerados a partir dos dados para enriquecer os relatórios, os quais são armazenados na pasta `images/` ou `output/`.

4. **Movimentação e Armazenamento de Arquivos**: Após a execução das etapas de processamento, os arquivos são movidos para as pastas apropriadas. Relatórios finais são armazenados na pasta `output/` e podem ser acessados posteriormente para distribuição ou análise.

5. **Rotinas Diárias**: Este processo pode ser repetido automaticamente, como uma rotina diária, para garantir que os dados e relatórios estejam sempre atualizados. O arquivo `Pipeline_Rotina_Diaria.md` no diretório `dump/` documenta a execução diária do pipeline.

## Instalação

Para executar este pipeline, você precisa ter o **Poetry** instalado. O **Poetry** facilita o gerenciamento de dependências, o ambiente virtual e o empacotamento do projeto.

### 1. Instalar o Poetry

Se você ainda não tem o **Poetry** instalado, siga as instruções no [site oficial do Poetry](https://python-poetry.org/docs/#installation) ou use o comando abaixo para instalá-lo utilizando o pip:

```bash
pip install poetry
```

### 2. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/pipeline_relatorios.git
cd pipeline_relatorios
```

### 3. Instalar Dependências com o Poetry

O **Poetry** gerencia as dependências do projeto automaticamente. Para instalar as dependências, basta rodar o comando abaixo no diretório raiz do projeto:

```bash
poetry install
```

Este comando vai:
- Criar um ambiente virtual isolado (se ainda não existir).
- Instalar todas as dependências listadas no `pyproject.toml`.

### 4. Ativar o Ambiente Virtual

Após instalar as dependências, o **Poetry** irá configurar um ambiente virtual para o projeto. Para ativá-lo, execute:

```bash
poetry shell
```

### 5. Executar o Pipeline

Com o ambiente configurado, você pode executar o pipeline utilizando o script principal `main.py`. Este script orquestra todas as etapas do processo:

```bash
poetry run python -m src.main
```

## Estrutura do Código

O código-fonte está dividido em diferentes módulos:

- **`src/config/config.py`**: Contém as configurações principais do projeto, como caminhos de diretórios, parâmetros de execução, etc.
  
- **`src/functions/`**: Contém funções responsáveis por etapas específicas do pipeline, como:
  - `atualiza_relatorio.py`: Atualiza os relatórios com os dados processados.
  - `extrai_imagem_relatorio.py`: Extrai ou gera imagens para os relatórios.
  - `move_relatorio.py`: Move os arquivos processados para as pastas corretas.

- **`src/main.py`**: Este é o script principal que executa o pipeline em ordem, chamando as funções necessárias.

## Contribuição

Se você gostaria de contribuir para este projeto, siga as etapas abaixo:

1. Fork o repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Realize as alterações.
4. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
5. Envie para o repositório remoto (`git push origin minha-modificacao`).
6. Abra um Pull Request para revisão.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
