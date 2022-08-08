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






