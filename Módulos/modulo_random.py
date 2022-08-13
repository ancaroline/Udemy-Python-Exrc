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


