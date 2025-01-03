### UNIT TESTS FOR EXTRACTION MODULES ###

# consultando módulos da python org
from unittest import TestCase, main
import os
import sys
# consultando módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from model.raw import RawDBs


class TestRawDB(TestCase, RawDBs):

    def test_mock(self):
        '''
        DOCSTRING:
        INPUTS:
        OUTPUTS:
        '''
        pass


if __name__ == '__main__':
    TestRawDB().test_mock()
