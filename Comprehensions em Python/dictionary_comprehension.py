"""
Dictionary Comprehension
Se quisermos criar uma lista fazemos:
lista = [1, 2, 3]
Se quisermos criar uma tupla:
tupla = (1, 2, 3)
Se quisermos criar um conjunto:
conjunto = {1, 2, 3}
Se quisermos criar um dicionário:
dicionario = {'a': 1, 'b': 2, 'c': 3}

# Sintaxe
{chave:valor for valor in iterável} -> dictionary comprehension
[valor for valor in iterável] -> list comprehension
"""

# Exemplos

num = {'a': 1, 'b': 2, 'c': 3}
quadrado = {chave: valor ** 2 for chave, valor in num.items()}
print(quadrado)

lista_num = [1, 2, 3]
quadrados = {valor: valor ** 2 for valor in lista_num}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)