"""
Módulo Collections: Ordered Dict
"""
# Em um dicionário a ordem não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

"""
Ordered Dict mantém a ordem de inserção
"""
from collections import OrderedDict

dicionario1 = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario1.items():
    print(f'chave={chave}: valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True/False? True, pois a ordem não importa para os dicionários

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'a': 2, 'b': 1})

print(odict1 == odict2)  # False, a ordem importa
