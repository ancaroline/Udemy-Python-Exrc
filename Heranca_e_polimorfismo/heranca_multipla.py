"""
POO — Herança Múltipla: Possibilidade de uma classe herdar de múltiplas classes.
Fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.
Enquanto em Java só é possível herdar de uma classe,
Em Python é possível herdar de múltiplas classes.

OBS: A herança múltipla pode ser feita de duas maneiras:
    — Por Multiderivação Direta;
    — Por Multiderivação Indireta;
"""


# Exemplo 1 — Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):  # Direta, pois esta classe está herdando diretamente de Base1, Base2.
    pass


# Exemplo 2 — Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):  # Indireta, pois está herdando indiretamente a base 2 e 1
    pass


"""OBS: Não importa se a derivação é direta ou indireta.
A classe que realizar a herança herderá todos os atributos e métodos
da super classe."""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# testando
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Qual cumprimentar? Method Resolution Order - MRO (Eu sou Tux da terra!)
# Ordem de herança altera como será o comportamento do seu objeto.

# Como descobrir se Objeto é instância de ...
print(f'Tux é instância de Pinguim?  {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquático?  {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre?  {isinstance(tux, Terrestre)}')
print(f'Tux é instância de object?  {isinstance(tux, object)}')  # por padrão uma classe herda de object
print(f'Tux é instância de animal? {isinstance(tux, Animal)}')
