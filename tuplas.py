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
