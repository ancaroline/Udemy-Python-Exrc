"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""
# exemplo all()
print(all([0, 1, 2, 3, 4]))  # todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # todos os números são verdadeiros? True
print(all([]))  # True
print(all((1, 2, 3)))  # pode ser uma tupla.
print(all('geek'))  # uma string.

nomes = ['Carlos', 'Camila', 'Cassio']  # se houvesse um nome com letra diferente, seria false
print(all([nome[0] == 'C' for nome in nomes]))
# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # true
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))  # daria uma lista vazia, portanto True
