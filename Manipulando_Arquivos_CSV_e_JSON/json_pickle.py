"""
Trabalhando com JSON e Pickle
JSON -> JavaScript Object Notation
API -> Meios de comunicação entre os serviços oferecidos por empresas (twitter, facebook) e terceiros (devs)
"""
import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])  # dumps faz a formatação para o json
print(type(ret))
print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


gatos = Gato('Felix', 'Vira-Lata')
print(gatos.__dict__)

ret = json.dumps(gatos.__dict__)
print(ret)

"""Integrando o JSON com o Pickle
pip install jsonpickle
"""
import jsonpickle

ret = jsonpickle.encode(gatos)  # ao invés de usar json.dumps
print(ret)

# Escrevendo o arquivo json/pickle
"""with open('gatos.json', 'w') as arquivo:
    ret = jsonpickle.encode(gatos)
    arquivo.write(ret)"""

# Lendo o arquivo json/pickle
with open('gatos.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)  # decode para decodificar
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)


