"""
POO - O método super()
-> Se refere à super classe.
"""


class Animal:  # super classe da classe Gato

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):  # gato é um animal específico

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # não recomendado, mas possível
        super().__init__(nome, especie)  # recomendado
        super().faz_som('auau')  # com o super é possível ter acesso a qualquer elemento
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')