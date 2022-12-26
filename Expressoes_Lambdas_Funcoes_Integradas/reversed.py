"""
Reversed
Não confunda com a função reverse() que estudamos nas listas
A função reverse() só funciona em listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""
# Exemplos
lista = [1, 2, 3, 4]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto.
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # em conjuntos, não definimos a ordem dos elementos

# podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')
# podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))
# slice de strigs
print('Geek University'[::-1])
# podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# utilizando o próprio range
for n in range(9, -1, -1):
    print(n)