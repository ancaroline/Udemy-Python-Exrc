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

# Outro exemplo
autores = ['Rafael Oliveira', 'Anne Rosen', 'Arthur Sanches', 'Ana F. Pimenta', 'Douglas Adams',
           'Carlos Souza Mart']

print(autores)
# ordenação por sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())  # parâmetro: sobrenome
print(autores)


# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    # Retorna a função f(x) = a * x ** 2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))  # x valendo 0
print(teste(1))  # x valendo 1
print(teste(2))  # x valendo 2
print(geradora_funcao_quadratica(2, 3, 4)(2))  # x valendo 2

# A gente aplica lambda para fazer filtragem e geração de dados
