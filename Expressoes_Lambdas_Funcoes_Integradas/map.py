"""
Map
Com map, fazemos mapeamento de valores para função.
"""
import math


def area(r):
    """Calcula a área de um círculo com raio 'r' """
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 3, 4.9, 8, 2.9]
# forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# forma 2 - MAP
# uma função que recebe dois parâmetros: o primeiro a função, o segundo um iterável.
areas = map(area, raios)
print(areas)  # retorna um map object
print(list(areas))

# forma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map(), depois da primeira utilizaçao do resultado, ele zera.

"""
Para fixar - Map
Temos dados iteráveis:
dados: a1, a2... an
temos uma função:
função: f(x)
Utilizaremos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar
a função.
O Map Object: f(a1), f(a2), f(an)
"""
# Mais um exemplo
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]
print(cidades)

# f= 9/5 * c + 32
# Lambda
c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
