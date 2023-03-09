"""
Antes e após hooks
hooks -> testes em si, a execução dos testes.
Antes e após os testes

setup() -> executado antes de cada método de teste. Útil para criarmos instâncias de objetos e outros dados.
tearDown() -> executado ao final de cada método de teste. Útil para excluir dados ou fechar conexões com BD.
"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setup()
        pass

    def test_primeiro(self):
        # setup vai rodar antes do teste.
        # teardown vai rodar após o teste.
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
