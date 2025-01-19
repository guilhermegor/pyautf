### MAIN PROGRAM PARA ORQUESTRAR OS MÓDULOS MODEL/VIEW ###

# consultando módulos da python org
import sys
import os
import warnings
from time import time
from keyring import get_password
# consultando módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.global_slots import LOGGER, DIR_PARENT, YAML_USER_CFG, NOME_COMP_DESTINO_LOG, \
    USER, AMBIENTE_EXECUCAO, HOSTNAME, CLS_POSTGRESQL_RAW, CLS_WEBHOOK_SLACK, ROOT_DIR_XPT
from model.raw import RawDBs
from model.cleaned import CleanedDatabases
from model.curated import CuratedData
from model.helper import HelperFuncs
# consultando pacotes alocados na pasta acima do projeto
sys.path.append(HelperFuncs().root_py_dev)
from stpstone.opening_config.setup import iniciating_logging
from stpstone.loggs.create_logs import CreateLog
from stpstone.microsoft_apps.teams.teams_integration import TeamsConn
from stpstone.cals.handling_dates import DatesBR
from stpstone.handling_data.json import JsonFiles
from stpstone.directories_files_manag.managing_ff import DirFilesManagement
from stpstone.handling_data.pd import DealingPd


# acionando cronômetro
float_start_time = time()

# desativando mensagens de incompatibilidades futuras
warnings.simplefilter(action='ignore', category=FutureWarning)

# começando processo de gravação de log
iniciating_logging(LOGGER, DIR_PARENT)

# definindo variáveis
CreateLog().infos(LOGGER, 'Iniciando processo de definição de variáveis')

# variáveis de passagem
dict_exportacao = dict()

# arquivos de exportação
nome_completo_json_xpt = YAML_USER_CFG['json']['nome_completo_xpt'].format(
        ROOT_DIR_XPT,
        DatesBR().curr_date, 
        AMBIENTE_EXECUCAO.lower(), 
        USER, 
        DatesBR().curr_date.strftime('%Y%m%d'),
        DatesBR().curr_time.strftime('%H%M%S')
    )

# gerando evidência nos logs
CreateLog().infos(LOGGER, 'Código do operador: {}'.format(USER))
CreateLog().infos(LOGGER, 'Hostname da máquina executando a rotina: {}'.format(HOSTNAME))
CreateLog().infos(LOGGER, 'Versão de execução do código: {}'.format(AMBIENTE_EXECUCAO))
CreateLog().infos(LOGGER, 'YAML em memória: {}'.format(YAML_USER_CFG))
CreateLog().infos(LOGGER, 'Nome completo json de exportação para lugar na rede: {}'.format(
    nome_completo_json_xpt))

CreateLog().infos(LOGGER, 'Finalizando processo de definição de variáveis')

# pool de conexões
CreateLog().infos(LOGGER, 'Iniciando processo de definição de pool de conexões')
cls_db = CLS_POSTGRESQL_RAW
cls_webhook = CLS_WEBHOOK_SLACK
CreateLog().infos(LOGGER, 'Finalizando processo de definição de pool de conexões')

# classes de interesse
CreateLog().infos(LOGGER, 'Iniciando processo de definição de classes de interesse')
cls_raw_dbs = RawDBs()
cls_cleaned_dbs = CleanedDatabases(cls_raw_dbs)
cls_curated_dbs = CuratedData()
CreateLog().infos(LOGGER, 'Finalizando processo de definição de classes de interesse')

# * início das regas de negócio
print('INÍCIO DAS REGRAS DE NEGÓCIO')

# fechando conexões de interesse
CreateLog().infos(LOGGER, 'Iniciando processo de fechamento da conexão com db')
cls_db._close
CreateLog().infos(LOGGER, 'Finalizando processo de fechamento da conexão com db')

# criando json com gravação da saída em lugar na rede
CreateLog().infos(LOGGER,
                  'Iniciando processo de exportação de dicionário, ou lista de '
                  + 'dicionários, para local na rede')
#! substituir dict_exportacao pela lista de dicionários, ou dicionários criados ao longo
#!      do código ou outro objeto hashable a ser exportado
blame_json_dump = JsonFiles().dump_message(dict_exportacao, nome_completo_json_xpt)
CreateLog().infos(LOGGER, 'Status criação do json com os arquivos de exportação: {}'.format(
    blame_json_dump))
CreateLog().infos(LOGGER,
                  'Finalizando processo de exportação de dicionário, ou lista de '
                  + 'dicionários, para local na rede')

# enviando mensagens por webhook
if AMBIENTE_EXECUCAO == 'PRD':
    cls_webhook.send_message(
        YAML_USER_CFG['webhooks']['rotina']['mensagem'].format(
            YAML_USER_CFG['webhooks']['rotina']['titulo'],
            DatesBR().curr_date_time(),
            HOSTNAME, 
            USER, 
            nome_completo_json_xpt, 
            NOME_COMP_DESTINO_LOG
        )
    )

# definindo tempo de execução do script
float_elapsed_time = time() - float_start_time
hours, remainder = divmod(float_elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
CreateLog().infos(LOGGER, f'Tempo de execução (HH:MM:SS): {int(hours)}:{int(minutes)}:{seconds:.2f}')

# fim da rotina
CreateLog().infos(LOGGER, 'Rotina finalizada em {}'.format(str(DatesBR().curr_date_time())))
