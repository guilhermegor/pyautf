### TESTES UNITÁRIOS PARA MÓDULO DAS REGRAS DE NEGÓCIO ###

from unittest import TestCase, main
import os
import sys
sys.path.append('\\'.join([d for d in os.path.dirname(os.path.realpath(__file__)).split(
    '\\')][:-1]))
from classes.extract import DatabasesExtract


class TestModule(TestCase, DatabasesExtract):

    def test_mock(self):
        '''
        DOCSTRING:
        INPUTS:
        OUTPUTS:
        '''
        pass


if __name__ == '__main__':
    TestModule().test_mock()
