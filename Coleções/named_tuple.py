"""
Módulos Collections - Named Tuple
Tupla nomeada > tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros
"""
tupla = (1, 2, 3)
print(tupla[1])

# importando
from collections import namedtuple

# precisamos definir o nome e parâmetros
# Forma 1 — Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 — Declaração Named Tuple
cachorro1 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 — Declaração Named Tuple
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')  # variável ray do tipo cachorro
print(ray)

# Acessando os dados
# Forma 1
print(ray[0])  # acessando a idade
print(ray[1])  # acessando a raça
print(ray[2])  # acessando o nome

# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))