"""
Mapas -> Conhecidos como Dicionários
Dicionários são representados por chaves {}
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
# Iterar sobre dicionários
print(receita)

for chave in receita: # Para cada chave em receita, imprima a chave
    print(chave)

for chave in receita: # Imprimir o valor da receita
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Para conhecer todas as chaves
print(receita.keys())

# Recomendável utilizar desta maneira:
for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())
for valor in receita.values():
    print(valor)
