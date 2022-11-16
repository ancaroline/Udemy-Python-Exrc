"""
Listas aninhadas (Nested Lists)
- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
- Unidimensionais (Array/Vetores):
- Multidimensionais (Matrizes)

Em python nós temos as listas
num = [1, 2, 3, 4]
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # como se fosse uma matriz
print(listas)
print(type(listas))

# Como acessar os dados?

print(listas[0])
print(listas[0][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    # imprimir cada um dos elementos
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['x' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
