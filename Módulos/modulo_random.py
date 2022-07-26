"""
Módulo Random e o que são módulos?
— Em Python, módulos nada mais são do que outros arquivos Python
Módulo Random possuem várias funções para geração de números pseudo-aleatório.
"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste
# Forma 1 — Importando todo o módulo (Não recomendado)
import random  # todas as funções, atributos, classes e propriedades ficarão em memória

# random() -> Gera um número pseudo-aleatório entre 0 e 1
print(random.random())  # nome_do_pacote.nome_da_função
# Não confunda a função random() com o pacote random

# Forma 2 — Importando uma função específica do módulo (Forma recomendada)

from random import random

# do módulo random, importe a função random.
for i in range(10):
    print(random())

# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# shuffle() -> tem a função de embaralhar dados
from random import shuffle

cartas = ['k', 'q', 'j', 'a', '2', '3']
print(cartas)
shuffle(cartas)
print(cartas)
print(cartas[0])  # dando a carta embaralhada
print(cartas.pop())  # retirando a última carta embaralhada
