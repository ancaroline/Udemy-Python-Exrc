"""
Trabalhando com Módulos Built-in (módulos integrados, já vem instalados no Python)
________________________
|Python|Módulos builtin|
-----------------------
docs.python.org/3/py-modindex.html
"""
# Utilizando 'alias' (apelidos) para módulos/funções
import random as rdm  # o 'as' serviu para criar o 'alias' 'rdm'

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *
from random import *
print(random())

# Utilizando 'alias' (apelidos) para módulos/funções
from random import randint as rdi  # apelidou a função
print(rdi(1, 25))

# E para importar duas funções em simultâneo:
from random import randint as rdi, random as rdm

print(rdi(1, 2))
print(rdm())

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())
print(randint(1, 2))
lista = [1, 2, 3]
shuffle(lista)
print(shuffle())
print(choice())
