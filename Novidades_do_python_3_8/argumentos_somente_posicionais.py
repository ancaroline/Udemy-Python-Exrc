"""
Argumentos somente posicionais
-> informar somente o valor
"""


# Exemplo
def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('João'))
print(cumprimenta_v1(nome='João'))


# Com argumento somente posicional
def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print(cumprimenta_v2('João'))
print(cumprimenta_v2(nome='João'))  # -> Isto dará erro, pois aceita somente o valor


# Com mais de um parâmetro
def cumprimenta_v3(nome, /, mensagem='Olá'):  # parâmetro nome posicional e mensagem com valor padrão
    return f'{mensagem}, {nome}'


print(cumprimenta_v3('João'))
print(cumprimenta_v3('João', mensagem='Hello'))
print(cumprimenta_v3('João', 'Bem-vindo'))


# Ambos os parâmetro sejam posicionais
def cumprimenta_v4(nome, mensagem='Olá', /):
    # A barra indica que tudo que estiver antes dela é posicional
    return f'{mensagem}, {nome}'


print(cumprimenta_v4('João'))
print(cumprimenta_v4('João', mensagem='Hello'))  # -> Isto dará erro, pois aceita somente o valor
print(cumprimenta_v4('João', 'Bem-vindo'))


# É possível obrigar a informar o parâmetro
def cumprimenta_v5(*, nome):
    # todos os argumentos após o * serão obrigatórios
    return f'Olá {nome}'


print(cumprimenta_v5(nome='João'))
print(cumprimenta_v5('João'))  # -> Isto dará erro, pois é obrigatório informar o parâmetro


# Função com todas as possibilidades
def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1}, {nome}, {mensagem2}'


print(cumprimentar_v6('João', mensagem2='Seja bem-vindo'))
print(cumprimentar_v6('João', mensagem1='Hello', mensagem2='Seja bem-vindo'))
# print(cumprimentar_v6('João', mensagem1='Hello', 'Seja bem-vindo'))
# -> Isto dará erro, pois é obrigatório informar o parâmetro