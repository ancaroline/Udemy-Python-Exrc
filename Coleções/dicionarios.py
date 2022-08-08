"""
Dicionários

OBS: Em algumas linguagens são conhecidos por mapas, pois
dicionários são coleções do tipo chave/valor
Mapeamento entre chave e valor

Dicionários são representados por {}
"""
"""
--> Chave:valor
--> Tanto a chave quanto o valor podem ser de qualquer tipo
--> Podemos misturar tipos de dados
"""
print(type({})) # dict

# Criação de dicionários
# Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'pt': 'Portugal'} # 3 itens
print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos')
print(paises)
print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br']) # informando a chave
# se não tiver a chave, dará o erro keyError

# Forma 2 -> Forma recomendada -> Acessando via get
print(paises.get('br'))
print(paises.get('pt')) # não dará erro, aparecerá "none"
# Valor padrão para caso não encontrarmos a chave informada
print(paises.get('ru', 'Não encontrado')) # se não encontrar, coloque esse valor no lugar

# Podemos verificar se determinada chave se encontra
print('br' in paises) # essa chave se encontra nesse dicionário?
print('Brasil' in paises) # temos Brasil, mas não como chave e sim como valor

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado, inclusive listas, tuplas, como chaves de dicionarios
# Tuplas são interessantes de serem utilizados como chaves de dicionários, pois
# são imutáveis
localidades = {
    (35.6565, 45.2323): 'Escritório em Tókio',
    (84.484, 39.2626): 'Escritório em Orlando',
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 > Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)






