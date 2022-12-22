"""
Sorted
OBS: não confunda com a funçao sort() que já estudamos em Listas.
Podemos utilizar o sorted() com qualquer iterável.
sorted() serve para ordenar.

OBS: O sorted SEMPRE retorna uma lista com os elementos do iterável ordenado.
"""
# Exemplo
numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # ordenar do menor para o maior.
# convertendo para tupla
print(tuple(sorted(numeros)))

"""
A diferença entre sort e sorted:
O sort() modifica a própria lista, o sorted() não modifica, retorna uma nova lista.
"""
# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor.

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "gustavo", "tweets": ["Eu não gosto de bolos"]},
    {"username": "joe", "tweets": []},
    {"username": "carla", "tweets": ["Eu adoro gatos"]},
    {"username": "bob123", "tweets": [], "musica": "rock", "cor": "azul"},
    {"username": "ana", "tweets": ["gatos são bons", "Eu adoro bolos", "viva a vida"]}
]

print(usuarios)
# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # dictionarys
# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# último exemplo
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "All in", "tocou": 1},
    {"titulo": "Video Games", "tocou": 5},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))