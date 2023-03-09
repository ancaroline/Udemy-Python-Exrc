import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('setUp() sendo executado')

    def test_carregar(self):
        # megaman = Robo('Mega Man', bateria=50) -> para não ter repetição de código, utilizaremos o setup, onde iremos
        # criar uma variável
        # megaman.carregar() -> agora para fazer acesso: self.nome_da_variável
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)  # se megamen.bateria (propriedade) é igual a 100

    def test_dizer_nome(self):
        # megaman = Robo('Mega Man', bateria=50)
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49')

    def tearDown(self):
        print('tearDown() sendo executado')


if __name__ == '__main__':
    unittest.main()
