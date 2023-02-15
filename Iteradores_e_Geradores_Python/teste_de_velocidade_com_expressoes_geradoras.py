"""
Teste de velocidade com expressões geradoras
"""


# Generators
def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)
print(next(ge1))

# Generator Expression
ge2 = (num for num in range(1, 10))
print(ge2)
print(next(ge2))

# Realizando o teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio
# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')  # Generator Expression levou 10.960800409317017
print(f'List Comprehension levou {list_tempo}')  # List Comprehension levou 48.06023168563843
