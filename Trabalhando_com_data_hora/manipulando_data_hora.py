"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime.
"""

import datetime

# print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2023-03-07 09:14:16.798532
# Representação
print(repr(datetime.datetime.now()))  # datetime.datetime(2023, 3, 7, 9, 15, 23, 859012)

# Fazendo ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)
# Alterar o horário para 16 horas  -> Imagina que está querendo enviar um email programado
inicio = inicio.replace(year=2025, hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# É possível criar uma data/hora?
import datetime

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/12/2018'))
print(evento)

nascimento = input('Informe a sua data de nascimento (dd/mm/yyyy):')

# transformar a string em uma data
nascimento = nascimento.split('/')  # vira uma list
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))

# Acesso individual dos elementos de data e hora
inicio = datetime.datetime.now()
print(f'Acessando o ano: {inicio.year}')
