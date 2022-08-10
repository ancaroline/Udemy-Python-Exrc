"""
Funções com retorno

OBS: Quando uma função não retorna nenhum valor, o retorno é None
Não precisamos necessariamente criar uma variável para recebemos o retorno de uma função.
Podemos passar a execução da função para outras funções.
"""


# Exemplo de Função sem retorno
def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()
print(f'Retorno {ret}')


# Refatorando a função
def quadrado_de_7():
    return 7 * 7  # deve retornar o valor com a palavra return


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')
print(f'Retorno: {quadrado_de_7() + 1}')


# Refatorando a função 'diz_oi'
def diz_oi():
    return 'Oi '


alguem = 'Pedro!'
print(diz_oi() + alguem)

"""
Return:
-> Finaliza a função, sai da execução da função
-> Podemos ter, em uma função, diferentes returns:
-> Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
"""


# Exemplo 1
def diz_oi():
    return 'Oi!'
    print('Estou sendo executado após o return')  # Esta linha nunca será executada


print(diz_oi())


# Exemplo 2
def nova_funcao():
    v = False
    if v:
        return 4
    elif v is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5  # formou uma tupla


num1, num2, num3, num4 = outra_funcao()  # desempacotando a tupla
print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import random  # biblioteca


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


# Refatorando a função 'joga_moeda'
def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

