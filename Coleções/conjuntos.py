"""
Conjuntos
— Estamos fazendo referência à Teoria dos Conjuntos da Matemática
— Os Conjuntos são nomeados de Sets
‘Sets’ não possuem valores duplicados;
Não possuem valores ordenados;
Elementos não são acessados via índice, ou seja, conjuntos não são indexados;
Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas
não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.
‘Sets’ são referenciados com chaves {}

Diferença entre Conjuntos e Mapas:
    — Um dicionário tem chave/valor
    — Um conjunto tem apenas valor;
"""

# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 4, 3, 2, 1}) # não gera erro, mas não adiciona valores repetidos
print(s) # {1, 2, 3, 4, 5}
print(type(s))

# Forma 2 — Mais comum
s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem
# listas aceitam valores duplicados
lista = [29, 29, 3, 4, 5]
print(f'Lista: {lista} com {len(lista)} elementos')
# Tuplas aceitam valores duplicados
tupla = (29, 29, 3, 4, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')
# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys([29, 29, 3, 4, 5], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')
# Conjuntos não aceitam valores duplicados
conjunto = {29, 29, 3, 4, 5}
print(f'Conjuntos: {conjunto} com {len(conjunto)} elementos')

# Podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22}
print(s)
print(type(s))

# Podemos iterar em um ‘set’ normalmente
for valor in s:
    print(valor)

"""
Exemplos de usos com sets

Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu
e os visitantes informam manualmente a cidade de onde vieram.
Nós adicionamos cada cidade em uma lista Python, já que em uma lista
podemos adicionar novos elementos e ter repetição
"""
cidades = ['São Luís', 'São Paulo', 'São Luís', 'São Bento']
print(cidades)
print(f'{len(cidades)} pessoas visitaram o museu.') # Para saber a quantidade de pessoas que vieram
# Agora precisamos saber quantas cidades distintas temos
# Podemos usar o set para isso:
print(f'Temos {len(set(cidades))} cidades diferentes')

# Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)
s.add(4) # os conjuntos são mutáveis
s.add(4) # duplicidade não gera erro, porém é ignorado
print(s)

# Remover elementos em um conjunto
# Forma 1
s.remove(2) # isto não é índice, é valor, pois conjuntos não são indexados
print(s) # se não existir o valor, key error

# Forma 2
s.discard(4)
print(s) # se não existir o valor, nenhum erro é gerado

# Copiando um conjunto para outro
s = {'a', 'b', 'c'}
# Forma 1 - Deep Copy // dois objetos independentes
novo = s.copy()
print(novo)
novo. add('d')
print(novo)
print(s)

# Forma 2 - Shallow Copy
s = {'a', 'b', 'c'}
novo = s
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

"""
Métodos Matemáticos de Conjuntos

Imagine que temos dois conjuntos:
1. Estudantes do curso de Python
2. Estudantes do curso de Java
"""
estudantesPython = {'Marcos', 'Samuel', 'Carol', 'Pedro'}
estudantesJava = {'Ana', 'Gustavo', 'Carol', 'Samuel'}
"""
Alguns alunos que estudam Python também estudam Java

Precisamos gerar um conjunto com nomes de estudantes únicos
"""
# Forma 1 — Utilizando Union (união entre dois ou mais conjuntos)
unicos1 = estudantesPython.union(estudantesJava) # mais recomendado
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantesPython | estudantesJava
print(unicos2)

"""
> Gerar um conjunto de estudantes que estão em ambos os cursos
"""
# Forma 1 - Utilizando intersection
ambos1 = estudantesPython.intersection(estudantesJava)
print(ambos1)
# Forma 2 — Utilizando o &
ambos2 = estudantesPython & estudantesJava
print(ambos2)

"""
> Gerar um conjunto de estudantes que não estão no outro
"""
soPython = estudantesPython.difference(estudantesJava)
print(f'Os alunos {soPython} estão matriculados apenas em Python')
soJava = estudantesJava.difference(estudantesPython)
print(f'Os alunos {soJava} estão matriculados apenas em Java')

# Soma* , Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros e reais
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))