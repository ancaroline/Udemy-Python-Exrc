"""
Módulo Collections - Counter (contador)
Collections -> High performance Container Datetypes (tipo de dados de container de alta performance)

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor, a quantidade
de ocorrências desse elemento.
"""

# Utilizando o Counter

from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 7]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

"""
Para cada elemento da lista, o Counter cria uma chave e colocou como valor a quantidade
de ocorrências
"""

# Exemplo 2
print(Counter('Geek'))

# Exemplo 3
texto = """ Sega CD é um acessório baseado em CD-ROM para o Mega Drive projetado 
e produzido pela Sega como parte da quarta geração de consoles de jogos eletrônicos. 
Foi lançado em 12 de dezembro de 1991 no Japão, 
15 de outubro de 1992 na América do Norte e 2 de abril de 1993 na Europa. """

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)
# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
