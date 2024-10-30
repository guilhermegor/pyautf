### PROGRAMA PRINCIPAL PARA EFETUAR AS CHAMADAS DOS DEMAIS MÓDULOS DA SOLUÇÃO ###

import sys
import os
from source.config.global_slots import LOGGER, DIR_PARENT, YAML_MEM, NOME_COMP_DESTINO_LOG, \
    USER, VERSAO_EXECUCAO, HOSTNAME
sys.path.append('\\'.join([d for d in os.path.dirname(os.path.realpath(__file__)).split(
    '\\')][:-1]))
from stpstone.opening_config.setup import iniciating_logging
from stpstone.loggs.create_logs import CreateLog
from stpstone.microsoft_apps.teams.teams_integration import TeamsConn
from stpstone.cals.handling_dates import DatesBR
from stpstone.handling_data.json import JsonFiles
from stpstone.directories_files_manag.managing_ff import DirFilesManagement
sys.path.append(r'C:\Users\{}\Desktop\Dados Pessoais'.format(USER))
from pers.global_slots import YAML_MEM_PERS

# começando processo de gravação de log
iniciating_logging(LOGGER, DIR_PARENT)

# definindo variáveis
CreateLog().infos(LOGGER, 'Ininciando processo de definição de variáveis')

# variáveis de passagem
dict_exportacao = dict()

# exportação
nome_completo_json_exportacao = YAML_MEM['nomes_completos_exportacao_json'].format(
    DatesBR().curr_date, VERSAO_EXECUCAO.lower(), USER, 
    DatesBR().curr_date.strftime('%Y%m%d'), DatesBR().curr_time.strftime('%H%M%S'))

# gerando evidência nos logs
CreateLog().infos(LOGGER, 'Código do operador: {}'.format(USER))
CreateLog().infos(LOGGER, 'Hostname da máquina executando a rotina: {}'.format(HOSTNAME))
CreateLog().infos(LOGGER, 'Versão de execução do código: {}'.format(VERSAO_EXECUCAO))
CreateLog().infos(LOGGER, 'YAML em memória: {}'.format(YAML_MEM))
CreateLog().infos(LOGGER, 'Nome completo json de exportação para lugar na rede: {}'.format(
    nome_completo_json_exportacao))

CreateLog().infos(LOGGER, 'Finalizando processo de definição de variáveis')

# * começo das regras de negócio
print('TESTE')

# criando json com gravação da saída em lugar na rede
CreateLog().infos(LOGGER,
                  'Iniciando processo de exportação de dicionário, ou lista de '
                  + 'dicionários para local na rede')
#! substituir dict_exportacao pela lista de dicionários, ou dicionários criados ao longo
#!      do código
blame_json_dump = JsonFiles().dump_message(
    dict_exportacao, nome_completo_json_exportacao)
CreateLog().infos(LOGGER, 'Status criação do json com os arquivos de exportação: {}'.format(
    blame_json_dump))
CreateLog().infos(LOGGER,
                  'Finalizando processo de exportação de dicionário, ou lista de '
                  + 'dicionários para local na rede')

# enviando status da rotina por teams para o canal de interesse
if VERSAO_EXECUCAO == 'PRODUCAO':
    TeamsConn().send_message(
        YAML_MEM_PERS['teams']['webhook_opn'],
        YAML_MEM['alerta_teams']['titulo'], HOSTNAME, USER, nome_completo_json_exportacao,
        NOME_COMP_DESTINO_LOG)

# fim da rotina
CreateLog().infos(LOGGER, 'Rotina finalizada em {}'.format(
    str(DatesBR().curr_date_time())))
