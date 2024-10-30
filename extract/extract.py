# CARGA BASES DE INTERESSE

import sys
import os
from apoio.global_slots import LOGGER, DIR_PARENT, YAML_MEM, NOME_COMP_DESTINO_LOG, USER
from apoio.global_slots import VERSAO_EXECUCAO, HOSTNAME
sys.path.append(r'C:\Users\{}\Desktop\Dados Pessoais'.format(USER))
from pers.global_slots import YAML_MEM_PERS
sys.path.append('\\'.join([d for d in os.path.dirname(os.path.realpath(__file__)).split(
    '\\')][:-1]))
from stpstone.loggs.create_logs import CreateLog
from stpstone.cals.handling_dates import DatesBR
from stpstone.directories_files_manag.managing_ff import DirFilesManagement


class DatabasesExtract:

    pass
