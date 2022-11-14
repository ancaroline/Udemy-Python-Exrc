"""
**kwargs
Diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados e transforma esses
parâmetros extras em um dicionário
"""


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():  # chave, valor e usando .items
        print(f'A cor favorita de {pessoa.title()} é {cor}')  # deixando pessoa com maiúscula


cores_favoritas(marcos='verde', julia='rosa', carol='amarelo')


# OBS: Os parâmetros *args e **kwargs não são obrigatórios

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

"""
Nas nossas funções, podemos ter (nesta ordem):
- Parâmetros obrigatórios
- *args;
- Parâmetros default (não obrigatório)
- **kwargs
"""


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entendendo por quê é importante manter a ordem dos parâmetros na declaração


def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# Função com a ordem incorreta de parâmetros
# def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
#     return [a, b, args, instrutor, kwargs]
# o args ficaria vazio, não receberia o 3
"""
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor)
"""

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
# print(mostra_nomes(nomes)) -> daria erro
print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
soma_multiplos_numeros(*lista)

# E se fosse um dicionário?
dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)  # duplo asterisco

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função
# dicionario = dict(f=1, g=2, y=3) TypeError
