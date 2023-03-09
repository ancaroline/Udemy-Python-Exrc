import unittest
from atividades import comer, dormir, eh_engracada


# nomeia a classe com o mesmo nome do módulo que queremos testar
class AtividadesTestes(unittest.TestCase):
    # o unittest considera cada função como um teste, então iremos dividir em duas funções
    def test_comer_saudavel(self):  # por convenção: test_
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('verduras', True),  # primeiro parâmetro
            'Estou comendo verduras, quero manter a forma.'  # segundo parâmetro
        )

    def test_comer_nsaudavel(self):
        """Testando o retorno com comida não saudável."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),  # argumentos nomeados
            'Estou comendo pizza, pois só se vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado por dormir apenas 4 horas.'
        )

    def test_dormir_muito(self):
        """Testando o retorno com dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Estou atrasado, acordei tarde.'
        )

    # Outros tipos de assertions
    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('Inês Silva'), False)  # None != False // função implementada ...
        self.assertFalse(eh_engracada('Inês Silva'))
        """espera que o resultado seja False, o teste irá passar, pois entenderá que None seja False:
                self.assertFalse(eh_engracada('Inês Silva')) 
                porém, nossa função ainda não foi implementada"""
        self.assertTrue(
            eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')  # especificando mensagem de erro


# se o nome da minha aplicação for igual a main, execute unittest.main
if __name__ == '__main__':
    unittest.main()
