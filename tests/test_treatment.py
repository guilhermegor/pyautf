### UNIT TESTS FOR TREATMENT MODULES ###

from unittest import TestCase, main
import os
import sys
sys.path.append('\\'.join([d for d in os.path.dirname(os.path.realpath(__file__)).split(
    '\\')][:-1]))
from .src.model.treatment import Treatments


class TestExtract(TestCase, DatabasesExtraction):

    def test_mock(self):
        '''
        DOCSTRING:
        INPUTS:
        OUTPUTS:
        '''
        pass


if __name__ == '__main__':
    TestExtract().test_mock()
