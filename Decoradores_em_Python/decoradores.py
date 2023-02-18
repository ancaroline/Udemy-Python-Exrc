"""
Decoradores (Decorators)
O que são?
1. Decorators são funções;
2. Envolvem outras funções e aprimoram seus comportamentos;
3. Também são exemplos de Higher Order Functions;
4. Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)
"""


# Decorators como funções (SINTAXE NÃO RECOMENDADA)
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo(a)')


# Testando 1
teste = seja_educado(saudacao)
teste()


# Testando 2
def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)
raiva_educada()

"""
DECORATORS COM SYNTAX SUGAR
"""


def seja_educado_mesmo(funcao):  # decorator function
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo()


@seja_educado_mesmo  # decorator
def apresentando():
    print('Meu nome é Pedro')


# Testando
apresentando()


"""
Não confunda Decorator Function com Decorator
"""