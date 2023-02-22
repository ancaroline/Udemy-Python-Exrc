"""
Módulo Collections - Default Dict
"""

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])

"""
Quando não tem chave encontrada, ocorre KeyError, 
para evitar o Key Error pode utilizar o Default Dict -> nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores
"""
# Fazendo import
from collections import defaultdict

dicionario1 = defaultdict(lambda: 0)
print(dicionario1)

dicionario1['curso'] = 'Programação em Python'
print(dicionario1)
print(dicionario1['outro'])  # KeyError no dicionário comum, mas aqui não
# Irá acrescentar e atribuir o valor 0
print(dicionario1)