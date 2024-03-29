"""
Zip
zip() -> cria um iterável (zip object) que agrega elemento de cada um dos
iteráveis passados como entrada em pares
"""
# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2, 'abc')
print(zip)  # zip object
print(type(zip1))

# Sempre podemos gerar uma lista, tupla ou dicionário
print(list(zip1))  # irá gerar uma lista com tuplas

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))  # irá gerar uma tupla com tuplas

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))  # irá gerar um set com tuplas

zip1 = zip(lista1, lista2)
print(dict(zip1))

"""
OBS: O zip utiliza como parâmetro o menor tamanho em iterável.
Isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes.
Irá parar quando os elementos do menor iterável acabar.
"""
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (2, 3)]
print(list(zip(*dados)))  # desempacotamento

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

"""
[('maria', 80, 98)...] para cada dado, colocar dado[0] como chave, no caso,
'maria' como chave e comparar dado[1] com dado[2]
"""
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map()
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
