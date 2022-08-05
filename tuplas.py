"""
Tuplas (tuple)
Tuplas são parecidas com listas
Existem 2 diferenças
1 - As tuplas são representadas por ()
2 - As tuplas são imutáveis, ao se criar uma tupla, ela não muda. Toda operação gera uma nova tupla
"""

"""
OBS1: As tuplas são representadas por (), porém elas podem ser declaradas sem ()
"""
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

"""
OBS2: Tuplas com 1 elemento
"""
tupla3 = (4) # Isto não será uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isto é uma tupla
print(tupla4)

tupla5 = 4, # Isto é uma tupla
print(tupla5)

"""
Conclusão: Tuplas são definidas pela vírgula e não pelo uso dos ()
"""

tupla = tuple(range(11)) # gerar um range de 1 a 10 e transforme em uma tupla
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tuplaCurso = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tuplaCurso
print(escola)
print(curso)
# Gera 'ValueError' se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição, remoção de elementos nas tuplas não existem
# Soma*, Valor Máximo*, Valor mínimo* e tamanho
# * Se os valores foram todos inteiros ou reais

tuplaSoma = (1, 2, 3)
print(sum(tuplaSoma))
print(max(tuplaSoma))
print(min(tuplaSoma))
print(len(tuplaSoma))

# Concatenação de tuplas
tuplaConcat = (1, 2, 3)
print(tuplaConcat)
tuplaConcat1 = (4, 3, 5)
print(tuplaConcat1)
print(tuplaConcat + tuplaConcat1)
# Mas as tuplas não foram alteradas
print(tuplaConcat)
print(tuplaConcat1)

# São imutáveis, mas podemos sobrescrever seus valores
tuplaConcat2 = tuplaConcat + tuplaConcat1
tuplaConcat1 = tuplaConcat2 + tuplaConcat

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla) # O número 3 está na tupla?

# Iterando sobre uma tupla
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)