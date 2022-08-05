"""
Loop for
Loop -> Estrutura de repetição
For -> Uma dessas estruturas
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # temos que transformar em uma lista

# Exemplo 1 - string
for letra in nome:
    print(letra)

# Exemplo 2 - lista
for numero in lista:
    print(numero)

# Exemplo 3 - range
for numero in range(1, 10):
    print(numero)
# Enumerate -> ((0, 'G'), (1, 'e')...)
for i, letra in enumerate(nome):
    print(nome[i])

for i, letra in enumerate(nome):
    print(letra)

# Descartando o índice
# Quando não precisamos de um valor, podemos descarta-lo utilizando um underline(_)
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor) #para trazer somente o índice: valor[0], para trazer somente a letra: valor[1]

qtd = int(input('Quantas vezes esse loop deve rodar? '))
for n in range(1, qtd+1): # para executar a quantidade desejada, adicionar qtd+1, pois o valor final do range não é contado
    print(f'Imprimindo {n}')

# outro exemplo
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1): # para executar a quantidade desejada, adicionar qtd+1, pois o valor final do range não é contado
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

# Em python existe o /n por default, se não quiser o /n, utilize:
nome = 'anne carol'
for letra in nome:
    print(letra, end='')

# concatenando
"""
nome = 'Geek'
nome + 'University'
nome * 3 = GeekGeekGeek
"""
# Emojis
# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num) # A barra é um caracter de scape, pedindo para ignorar
