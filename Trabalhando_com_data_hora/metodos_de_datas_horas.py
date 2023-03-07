"""
Métodos de datas e horas
"""
import datetime

agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Qual a diferença entre o now e o today?
"""O now() pode especificar um parâmetro de timezone. No today não conseguimos especificar."""

# Mudanças ocorrendo à meia-noite
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana, weekday()
# Os dias da semana do método weekday() começam em 0, sendo este a segunda-feira.
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

aniversario = input('Qual a sua data de nascimento?')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')


# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

# criando uma função
def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'


hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
hoje_formatado1 = hoje.strftime('%d de %B de %Y')
print(hoje_formatado)
print(hoje_formatado1)
print(formata_data(hoje))

"""pip install textblob"""
import datetime
from textblob import TextBlob

"""TextBlob -> Traduções"""


def formata_data1(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-bt')} de {data.year}"


print(formata_data1(hoje))

# Transformando string em objeto datetime
nascimento = datetime.datetime.strptime('10/04/1999', '%d/%m/%Y')
print(nascimento)

nascimento = input('Qual a sua data de nascimento? (dd/mm/yyyy)')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

# Somente a hora
almoco = datetime.time(12, 30, 0)
print(almoco)

# Mancando tempo de execução do nosso código com timeit
import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=100)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=100)
print(tempo)

import functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=1000))   # melhor forma de testar
# partial -> qual função nossa quer testar e qual o parâmetro da entrada da função
