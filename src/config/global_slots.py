### ESPAÇOS DE MEMÓRIA GLOBAIS ###

# consultando módulos da python org
import os
import sys
from getpass import getuser
from socket import gethostname
from keyring import get_password
# consultando módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.helper import HelperFuncs
# consultando pacotes alocados na pasta acima do projeto
sys.path.append(HelperFuncs().root_py_dev)
from stpstone.opening_config.setup import reading_yaml
from stpstone.loggs.create_logs import CreateLog
from stpstone.cals.handling_dates import DatesBR
from stpstone.directories_files_manag.managing_ff import DirFilesManagement
from stpstone.pool_conn.postgresql import PostgreSQLDB
from stpstone.webhooks.slack import WebhookSlack


# configuring machine user
USER = getuser()

# configuring machine hostname
HOSTNAME = gethostname()

# root - diretório central dos arquivos de exportação
ROOT_DIR_XPT = get_password('ROOT_DIR_XPT', 'PATH')

# alocação do yaml em memória
YAML_USER_CFG = reading_yaml(r'{}\settings\_user_cfg.yaml'.format(
    os.path.dirname(os.path.realpath(__file__))))

# webhooks
YAML_WEBHOOKS = reading_yaml(r'{}\settings\webhooks.yaml'.format(
    os.path.dirname(os.path.realpath(__file__))))

# databases
YAML_DBS = reading_yaml(r'{}\settings\dbs.yaml'.format(
    os.path.dirname(os.path.realpath(__file__))))

# versão de execução do código
AMBIENTE_EXECUCAO = YAML_USER_CFG['painel_controle']['ambiente']

# diretório pai
DIR_PARENT = YAML_USER_CFG['nome_completo_arquivo_log']['diretorio_pai'].format(
    ROOT_DIR_XPT, DatesBR().curr_date
)
_ = DirFilesManagement().mk_new_directory(DIR_PARENT)

# iniciando logging
if AMBIENTE_EXECUCAO in ['DEV', 'PRD']:
    NOME_COMP_DESTINO_LOG = YAML_USER_CFG['nome_completo_arquivo_log']['destino'].format(
        ROOT_DIR_XPT,
        DatesBR().curr_date, 
        AMBIENTE_EXECUCAO.lower(), 
        USER, 
        DatesBR().curr_date.strftime('%Y%m%d'),
        DatesBR().curr_time.strftime('%H%M%S')
    )
else:
    raise Exception(
        'Versão de execução do código mal definida no YAML, favor validar')

LOGGER = CreateLog().basic_conf(NOME_COMP_DESTINO_LOG)

# conexões com bancos de dados
#   ! SCHEMA RAW, CASO SEJA NECESSÁRIO OUTRO FAVOR CRIAR UMA NOVA VARIÁVEL GLOBAL
CLS_POSTGRESQL_RAW = PostgreSQLDB(
    get_password(
        YAML_USER_CFG['postgresql']['keys']['nome_banco'], 
        YAML_USER_CFG['postgresql']['keys']['db_name']
    ),
    get_password(
        YAML_USER_CFG['postgresql']['keys']['nome_banco'], 
        YAML_USER_CFG['postgresql']['keys']['username']
    ), 
    get_password(
        YAML_USER_CFG['postgresql']['keys']['nome_banco'], 
        YAML_USER_CFG['postgresql']['keys']['password']
    ), 
    get_password(
        YAML_USER_CFG['postgresql']['keys']['nome_banco'], 
        YAML_USER_CFG['postgresql']['keys']['host']
    ),
    get_password(
        YAML_USER_CFG['postgresql']['keys']['nome_banco'], 
        YAML_USER_CFG['postgresql']['keys']['port']
    ), 
    get_password(
        YAML_USER_CFG['postgresql']['keys']['nome_banco'], 
        YAML_USER_CFG['postgresql']['keys']['schema_raw']
    ), 
)

# conexões com webhooks
CLS_WEBHOOK_SLACK = WebhookSlack(
    get_password(
        YAML_WEBHOOKS['keys']['nome_webhook'], 
        YAML_WEBHOOKS['keys']['url']
    ),
    get_password(
        YAML_WEBHOOKS['keys']['nome_webhook'], 
        YAML_WEBHOOKS['keys']['id_channel']
    ),
    get_password(
        YAML_WEBHOOKS['keys']['nome_webhook'], 
        YAML_WEBHOOKS['keys']['username']
    ),
    get_password(
        YAML_WEBHOOKS['keys']['nome_webhook'], 
        YAML_WEBHOOKS['keys']['icon_emoji']
    ),
)
