"""
Generator Expression
Aulas anteriores:
- List comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension, pois se chamam Generators
"""
# exemplo:
nomes = ['Carlos', 'Carol', 'Ana']
print(any([nome[0] == 'C' for nome in nomes]))
# Como ficaria com Generators:
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)  # -> só utiliza se precisar dessa lista, pois generator tem mais desempenho

# Generator -> gasta menos recurso da máquina, pois só tem um objeto em memória
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# getsizeof retorna a quantidade de bytes em memória do elemento como parâmetro
from sys import getsizeof

print(getsizeof('Geek'))  # quantos bytes a string está ocupando
print(getsizeof(9))
print(getsizeof(True))

# gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
# gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
# gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
# gerando uma lista de números com Generator Expression
generator_comp = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')  # pois, precisam de recursos de checagem
print(f'Dictionary Comprehension: {dic_comp} bytes')  # pois, precisam de recursos de checagem
print(f'Generator: {generator_comp} bytes')

# Eu posso iterar no Generator Expression? Sim
gen = (x * 10 for x in range(5))
for num in gen:
    print(num)