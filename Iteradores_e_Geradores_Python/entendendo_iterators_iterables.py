"""
Entendendo Iterators e Iterables
Iterator:
    — Um objeto que pode ser iterado.
    — Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada:
Iterable:
    — Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""
nome = 'Geek'  # A string Geek é um iterable, mas não um iterator
numeros = [1, 2, 3, 4]  # É um iterable, mas não um iterator

it1 = iter(nome)  # iterator
it2 = iter(numeros)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

for letra in nome:
    print(f'{letra}')
