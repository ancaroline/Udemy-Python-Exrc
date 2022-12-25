"""
Min e Max
max() -> Retorna o maior valor em um iterável ou o maior de dois, ou mais elemento.
"""
# Exemplo
lista = [1, 8, 4, 99, 44]
print(max(lista))

tupla = (1, 8, 4, 99, 44)
print(max(tupla))

conjunto = {1, 8, 4, 99, 44}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4}
print(max(dicionario))  # fala a maior chave
print(max(dicionario.values()))

print(max(3, 34))  # 34
print(max('a', 'b', 'c'))
print(max('a', 'abc', 'b'))
print(max(3.14, 6.2))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

"""
min() -> retorna o menor valor em um iterável ou o menor de dois ou mais elementos
"""
# Exemplo
lista = [1, 8, 4, 99, 44]
print(min(lista))

tupla = (1, 8, 4, 99, 44)
print(min(tupla))

conjunto = {1, 8, 4, 99, 44}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4}
print(min(dicionario))  # fala a maior chave
print(min(dicionario.values()))

print(min(3, 34))  # 34
print(min('a', 'b', 'c'))
print(min('a', 'abc', 'b'))
print(min(3.14, 6.2))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

list_nomes = ['arya', 'samson', 'dora', 'tim']
print(max(list_nomes))  # ordem alfabetica
print(min(list_nomes))

print(max(list_nomes, key=lambda nome: len(nome)))
print(min(list_nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "All in", "tocou": 1},
    {"titulo": "Video Games", "tocou": 5},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o titulo da musica e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar a música mais e menos tocada sem usar max, min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 99999
for musica in musicas:
    if musica['tocou'] > min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])