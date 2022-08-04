"""
Listas

Listas em Python funciona como vetores/arrays/matrizes, com a diferença
de serem DINÂMICAS e podermos colocar QUALQUER tipo de dado.

--> Dinâmico: não possui tamanho fixo, podemos criar a lista e ir adicionando
--> Qualquer tipo de dado: Não possuem tipo de dado fixo, podemos colocar qualquer tipo de dado
--> As listas são representadas por []
"""

lista1 = [1, 20, 4, 5, 23, 1]
lista2 = ['g', 'e', 'u', '', 'J']
lista3 = []
lista4 = list(range(11)) # vai transformar em uma lista de 10 elementos
lista5 = list('Geek University')

# Como checar se determinado valor está contido na lista
num = 18
if num in lista4: # só consegue verificar um elemento
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

if 'e' in lista4:
    print('Encontrei')
else:
    print('Não encontrei')

# Podemos ordenar uma lista
print(lista1)
lista1.sort()
print(lista1)

# Ordenar string
print(lista5)
lista5.sort()
print(lista5)

# podemos contar o número de ocorrências em uma lista
print(lista1.count(1))
print(lista5.count('g'))

# Adicionar elementos em listas
"""
Para adicionar elementos utilizamos a função append

OBS: Com append só podemos adicionar um elemento por vez
"""
print(lista1)
lista1.append(42)
print(lista1)
# Mas podemos adicionar elemento do tipo lista
lista1.append([100, 101, 102]) # sublista
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

"""
O extend não aceita valor único, valores únicos se utilizar o append
Extend aceita: string, [] 
"""
lista1.extend([123, 44, 67]) # adicionados individualmente, não em formato de lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(2, 'Novo Valor') # isso não substitui o valor
print(lista1)

# Podemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)
# isto é igual o extend, porém o de cima está criando uma lista nova
lista4.extend(lista2)
print(lista4)

# imprimir a lista inversa
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# ou pode usar o slice
print(lista1[::-1])

# Copiar uma lista
lista7 = lista2.copy()
print(lista7)

# Como saber o tamanho da lista
print(len(lista1))

# Remover o último elemento de uma lista
print(lista5)
lista5.pop() # remove e retorna o elemento
print(lista5)

# Podemos remover o elemento pelo índice
# Se não houver o elemento no índice informado, teremos o indexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista

curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)
# Por padrão, o split separa os elementos pelo espaço entre elas
# Exemplo 2
curso1 = 'Programação,em,Python'
print(curso1)
curso1 = curso1.split(',')
print(curso1)

# Transformar lista em string
lista8 = ['Programação', 'em', 'Python']
print(lista8)
curso3 = ' '.join(lista8) # pegue a lista e coloque espaços entre cada elemento e transforme em uma string
print(curso3)

# Iterando sobre listas
# Exemplo 1 -- Utilizando For

for elemento in lista1:
    print(elemento)

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(f'A soma dos elementos é: {soma}')

# Exemplo 2 -- Utilizando While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto) # append: adiciona um elemento por vez
for produto in carrinho:
    print(produto)

