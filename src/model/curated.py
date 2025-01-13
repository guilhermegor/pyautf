### APLICAÇÃO DE REGRAS DE NEGÓCIO - CURATED ###

# consultando módulos da python org
import sys
import os
import pandas as pd
import numpy as np
# consultando módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.global_slots import LOGGER, DIR_PARENT, YAML_USER_CFG, NOME_COMP_DESTINO_LOG, USER
from config.global_slots import AMBIENTE_EXECUCAO, HOSTNAME
from model.helper import HelperFuncs
# consultando pacotes alocados na pasta acima do projeto
sys.path.append(HelperFuncs().root_py_dev)
from stpstone.loggs.create_logs import CreateLog
from stpstone.cals.handling_dates import DatesBR
from stpstone.directories_files_manag.managing_ff import DirFilesManagement
from stpstone.finance.cvm.cvm_web import CVMWeb_WS_Funds
from stpstone.handling_data.lists import HandlingLists


class CuratedData:

    pass