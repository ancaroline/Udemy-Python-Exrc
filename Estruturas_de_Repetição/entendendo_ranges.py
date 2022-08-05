"""
Utilizados para gerar sequeências numéricas, não de forma aleatória, mas sim de maneira espeficada.

Forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

Forma 2
range(valor_de_inicio, valor de parada)
OBS: valor_de_parada não inclusive (início especificado, e passo de 1 em 1)

Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado, e passo especificado)

Forma 4 (inversa)
range(valor_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado, e passo especificado)
"""

# Forma 1
print('Forma 1')
for num in range(11): # vai começar em 0 até 10
    print(num)


# Forma 2
print('Forma 2')
for num in range(1, 11):
    print(num)

# Forma 3
print('Forma 3')
for num in range(1, 10, 2):
    print(num)

# Forma 4
print('Forma 4')
for num in range(5, -1, -1):
    print(num)


