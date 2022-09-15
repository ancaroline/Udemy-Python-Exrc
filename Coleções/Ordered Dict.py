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