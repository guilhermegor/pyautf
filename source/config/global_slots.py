### ESPAÇOS DE MEMÓRIA GLOBAIS

import os
import sys
from getpass import getuser
from socket import gethostname
sys.path.append('\\'.join([d for d in os.path.dirname(os.path.realpath(__file__)).split(
    '\\')][:-2]))
from stpstone.opening_config.setup import reading_yaml
from stpstone.loggs.create_logs import CreateLog
from stpstone.cals.handling_dates import DatesBR
from stpstone.directories_files_manag.managing_ff import DirFilesManagement

# configuring machine user
USER = getuser()

# configuring machine hostname
HOSTNAME = gethostname()

# alocação do yaml em memória
YAML_MEM = reading_yaml(r'{}\general.yaml'.format(
    os.path.dirname(os.path.realpath(__file__))))

# versão de execução do código
VERSAO_EXECUCAO = YAML_MEM['painel_controle']['versao']

# diretório pai
DIR_PARENT = YAML_MEM['nome_completo_arquivo_log']['diretorio_pai'].format(
    DatesBR().curr_date)
_ = DirFilesManagement().mk_new_directory(DIR_PARENT)

# iniciando logging
if VERSAO_EXECUCAO in ['DESENVOLVIMENTO', 'PRODUCAO']:
    NOME_COMP_DESTINO_LOG = YAML_MEM['nome_completo_arquivo_log']['destino'].format(
        DatesBR().curr_date, VERSAO_EXECUCAO.lower(), USER, 
        DatesBR().curr_date.strftime('%Y%m%d'),
        DatesBR().curr_time.strftime('%H%M%S'))
else:
    raise Exception(
        'Versão de execução do código mal definida no YAML, favor validar')

LOGGER = CreateLog().basic_conf(NOME_COMP_DESTINO_LOG)
