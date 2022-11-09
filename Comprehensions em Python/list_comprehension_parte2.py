"""
List Comprehension
Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
"""
# Exemplos
# 1

list_numero = [1, 2, 3, 4, 5]

pares = [numero for numero in list_numero if numero % 2 == 0]
impares = [numero for numero in list_numero if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar
# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in list_numero if not numero % 2]
impares = [numero for numero in list_numero if numero % 2]
print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero/2 for numero in list_numero]
print(res)