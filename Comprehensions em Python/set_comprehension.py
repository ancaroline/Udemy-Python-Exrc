"""
Set Comprehension
set = {1, 2, 3, 4}
Relembrando: Não aceita valores repetidos, não tem ordenação
"""
numero = {num for num in range(1, 7)}
print(numero)

# Outro exemplo
numero = {x ** 2 for x in range(10)}
print(numero)

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionário
numero = {x: x ** 2 for x in range(10)}
print(numero)

# Para finalizar
letras = {letra for letra in 'Geek University'}
print(letras)