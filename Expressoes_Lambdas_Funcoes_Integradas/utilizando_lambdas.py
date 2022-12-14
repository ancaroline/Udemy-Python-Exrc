"""
São funções sem nome, ou seja, funções anônimas
"""


# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda
# Como utilizar? Declarando um nome
calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('anne', ' CAROLINE '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também.

amar = lambda: 'Como não amar python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ...., xn: <expressao>
print(amar())
print(uma(5))
print(duas(5, 6))
print(tres(5, 6, 7))

# obs: se passarmos mais argumentos do que parâmetros esperados, teremos TypeError
