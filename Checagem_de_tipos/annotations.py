"""# Correto
texto: str

# Incorreto
texto:str
texto : str

# Correto
) -> str

# Incorreto
)->str
) ->str

# Correto
alinhamento: bool = True"""

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)

# É possível utilizar o type hinting para tudo
nome: str = 'Geek'
ativo: bool
ativo = True
ativo1: bool = True

print(nome)
print(__annotations__)


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='João', idade=37, peso=50.5)
print(p.__dict__)
"""A instância não tem annotation:
# print(p.__annotation__)  -> daria erro
"""
print(p.andar.__annotations__)
print(p.__init__.__annotations__)  # annotation do init
