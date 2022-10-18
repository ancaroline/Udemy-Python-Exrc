"""
Funções com Parâmetro Padrão (Default Parameters)
-> Funções onde a passagem de parâmetro seja opcional
"""
# Exemplo de parâmetro opcional:
print('olá')
print()


# Exemplo de parâmetro obrigatório:
def quadrado(numero):
    return numero ** 2


print(quadrado(3))


# print(quadrado()) TypeError - precisa ter um parâmetro


# Exemplo de parâmetro padrão/opcional
def exponencial(numero, potencia=2):  # se um parâmetro já recebe um valor, ele já se torna opcional
    return numero ** potencia


print(exponencial(2))
print(exponencial(3, 5))  # o argumento 5 irá substituir o valor 2

"""
OBS: Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro número
e será calculado o quadrado deste número;
Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número
e o segundo ao parâmetro potência. Então, será calculada esta potência.

OBS 2: Em funções Pyhton, os parâmetros com valores default (padrão) DEVEM SEMPRE ESTAR ao final da declaração
"""


# Exemplo:
def obs2(potencia, num=2):
    return num ** potencia


print(obs2(6))  # potencia 6, numero default = 2


# Outros exemplos

def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))


# print(soma(4)) -> typeError, pois os parâmetros são obrigatórios
# print(soma()) -> typeError, pois os parâmetros são obrigatórios
# para não haver esses erros, teria que ter valores padrões

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Panda'))
print(mostra_informacao(nome='Red Holy Panda'))

"""
Por quê utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Qualquer tipo de dado.
"""


# Exemplos
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo — Evitar problemas e confusões
# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # global


def diz_oi():
    instrutor = 'Python'  # local
    return f'Oi {instrutor}'


print(diz_oi())


# OBS: A local terá preferência


def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_oi())
# print(prof) # NameError

# ATENÇÃO com variáveis globais (evite)
total = 0


def incrementa():
    # total = total + 1 > A variável não foi inicializada
    global total  # Avisando que estaremos usando a global
    total = total + 1
    return total


print(incrementa())
print(incrementa())


# Podemos ter funções que são declarodas dentro de funções
# forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(fora())

# não posso chamar a função print(dentro())
