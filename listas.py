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

# Utilizando variáveis em listas
n01 = [1, 2, 3, 4, 5]
print(n01)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

n01 = [num1, num2, num3, num4, num5]
print(n01)

# Acessar elementos: index
cores = ['verde', 'azul', 'vermelho']
print(cores[0]) # verde
print(cores[1]) # azul

# Acessar elementos: index inverso
# pense na lista como um círculo, onde o final do elemento está ligado com o início da lista
print(cores[-1]) # vermelho
print(cores[-2]) # azul

# ---

cores1 = ['roxo', 'rosa', 'lilás']

for cor in cores1:
    print(cor)

indice = 0
while indice < len(cores1):
    print(cores1[indice])
    indice = indice + 1

# Gerar índice em um for
for indice, cor in enumerate(cores1): # enumerate gera pares: chave e valor, cores1 no índice e o valor em cor
    print(indice, cor)

# Listas aceitam valores repetidos
# ---> Outros métodos <---
# Encontrar o índice de um elemento na lista
ex = [3, 4, 5, 10, 2, 3]

# Em qual índice está o valor 2?
ex2 = ex.index(2)
print(f'O valor está no index: {ex2}')
print(ex.index(4))
print(ex.index(3)) # retorna o índice do primeiro elemento encontrado

# podemos fazer busca dentro de um range, qual indice começar a buscar
print(ex.index(3, 1)) # encontrar o valor 3 a partir do index 1

# podemos fazer busca dentro do range, inicio/fim
ex3 = ex.index(4, 0, 3) # busca o numero 8 entre 6 e 8
print(f'O valor 4 entre os índices 0 e 3 está no index: {ex3}')

# ---------------

# Revisão de slicing
# lista[início:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'início'

Lista = [1, 2, 3, 4]
print(Lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes
print(Lista[::]) # Pegar todos os elementos
print(Lista[-1:])

# Trabalhando com slice de lista com o parâmetro 'fim'

print(Lista[:2]) # Começa em 0, pega até o índice 2-1
print(Lista[:4])
print(Lista[1:3])

# Trabalhando com slice de lista com o parâmetro 'passo'

print(Lista[1::2]) # Começa em 1, vai até o final de 2 em 2
print(Lista[::2]) # Começa em 0, vai até o final de 2 em 2
print(Lista[1::-1])

# Invertendo valores em uma lista
Nomes = ['Geek', 'University']
Nomes[0], Nomes[1] = Nomes[1], Nomes[0]
print(Nomes)
# É o mesmo de utilizar o reverse
Nomes.reverse()
print(Nomes)

# --- Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

listaExemplos = [1, 2, 3, 4, 5, 6]
print(sum(listaExemplos)) # soma
print(max(listaExemplos)) # máximo valor
print(min(listaExemplos)) # mínimo valor
print(len(listaExemplos)) # tamanho da lista

# Transformar uma lista em tupla
print(listaExemplos)
print(type(listaExemplos))

tupla = tuple(listaExemplos)
print(tupla)
print(type(tupla))


