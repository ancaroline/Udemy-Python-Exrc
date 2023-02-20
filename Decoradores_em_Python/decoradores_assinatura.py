"""
Decoradores com diferentes assinaturas

Assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
"""


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# testando
print(saudacao('Angelina'))


# print(ordenar('Picanha', 'Batata frita'))  # para resolver, utilizamos Decorator Pattern


# Refatorando com Decorator Pattern
def gritar1(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar1
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar1
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# testando
print(saudacao('Felicity'))
print(ordenar('Picanha', 'Batata Frita'))


@gritar1
def lol():
    return 'lol'


print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados
print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))


# Decorator com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)  # o primeiro argumento deve ser 10
def soma_dez(num1, num2):
    return num1 + num2


# testando
print(soma_dez(10, 12))
print(comida_favorita('pizza', 'doce'))