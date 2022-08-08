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