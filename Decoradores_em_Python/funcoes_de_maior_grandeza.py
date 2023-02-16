"""
Funções de Maior Grandeza - Higher Order Functions - HOF
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.
Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen
"""


# Exemplo - Definindo uma função
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando
print(calcular(3, 4, somar))
print(calcular(3, 4, diminuir))
print(calcular(3, 4, multiplicar))
print(calcular(3, 4, dividir))

# Nested Functions - Funções Aninhadas
"""
Podemos ter funções dentro de funções: Nested Functions ou Inner Functions
"""
# Exemplo
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto de você '))
    return humor() + pessoa  # retornando a execução da função


# testando
print(cumprimento('Felicity'))
print(cumprimento('Angelina'))


# Retornando funções de outras funções
def faz_me_rir():
    def rir():
        return choice(('kkkkk', 'hahaha', 'jajaja'))
    return rir  # retornando a função e não a execução


rindo = faz_me_rir()
print(rindo())  # executando a função rir

# Inner Functions / Nested Functions podem acessar o escopo de funções mais externas


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'kakaka'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Carol')
print(rindo())
