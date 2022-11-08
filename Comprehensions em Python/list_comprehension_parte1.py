"""
List Comprehension
— Utilizando List Comprehension nós podemos utilizar novas listas
com dados processados a partir de outro iterável
[ dado  for dado in iterável ]
"""

# Exemplos
list_numero = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in list_numero]
print(res)

"""
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
- A primeira parte: for numero in list_numero
- A segunda parte: numero * 10
"""
res = [numero / 2 for numero in list_numero]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in list_numero]
print(res)

# List Comprehension versos Loop

# Loop
list_numero = [1, 2, 3, 4, 5]
list_numeroDouble = []
for numero in list_numero:
    numero_dobrado = numero * 2
    list_numeroDouble.append(numero_dobrado)

print(list_numeroDouble)

# List Comprehension
print([numero * 2 for numero in list_numero])

# Outros exemplos
# 1
nome = 'Geek University'
print([letra.upper() for letra in nome])


# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro']
print([amigo[0].upper() for amigo in amigos])
print([caixa_alta(amigo) for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

