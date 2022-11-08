"""
Entendendo o *args
— É um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que comece com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo
Mas o que é?
Utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Tuplas são imutáveis.
"""


# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))


# print(soma_todos_numeros(4, 6))  - typeError
# print(soma_todos_numeros(4, 5, 6, 7))  - typeError

# Entendendo o args

def soma1_todos_numeros(nome, *args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma1_todos_numeros('Ana'))
print(soma1_todos_numeros('Ana', 1))
print(soma1_todos_numeros('Ana', 2, 3))


# como é uma tupla, poderia fazer diferente:
def menor_numero(*args):
    return min(args)


print(menor_numero(1, 2))
print(menor_numero(3, 4, 5))


def sub_todos_numeros(*args):
    total = 0
    for numero in args:
        numero = numero - total
        total = numero
    return total


print(sub_todos_numeros(4, 4))


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza de quem é você ...'


print(verifica_info())
print(verifica_info(1, 'true', 'Geek', 'University'))
print(verifica_info('ola', 'Geek'))


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4]

# Desempacotador
print(soma_todos_numeros(*numeros))
# o asterisco serve para informarmos que estamos passando uma coleção de dados e assim, desempacotar os dados.

