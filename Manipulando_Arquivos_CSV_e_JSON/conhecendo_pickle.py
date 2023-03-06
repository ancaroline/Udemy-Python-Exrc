"""
Conhecendo o Pickle
Às vezes precisamos salvar dados sensíveis
Salvar dados de forma binária
A função do Pickle é realizar o seguinte processo:
Objeto Python -> Binarização
Binarização -> Objeto Python

Processo chamado de serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos e destaforma
não é recomendado trabahar com arquivos pickle vindos de outras pessoas
que você não conheça ou de fontes desconhecidas.
"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


felix = Gato('Felix')

# Fazendo a escrita em arquivos pickle

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump(felix, arquivo)  # se eu tivesse mais de um objeto, eu passaria uma tupla ex: ((felix, pluto), arquivo)

# Fazer a leitura de dados em arquivos pickle
with open('animais.pickle', 'rb') as arquivo:
    gato = pickle.load(arquivo)  # load -> descompactar
    # se eu tivesse dois objetos: gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    print(f'O tipo do gato é {type(gato)}')
