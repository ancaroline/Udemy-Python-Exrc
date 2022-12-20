"""
filter() -> Serve para filtrar dados de uma determinada coleção
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor:
dados = [1.3, 2.7, 0.8, 5.3, -0.1]
# Calculando a média dos dados utilizando a função mean()
# o mean vai somar os valores e dividir pela quantidade de elementos
media = statistics.mean(dados)
print(f'Média: {media}')
"""
OBS: Assim como a função map,a filter recebe dois parâmetros
Sendo uma função e um iterável
"""
# selecionar os dados acima da média:
res = filter(lambda x: x > media, dados)
print(type(res))  # filter object
print(list(res))
print(f'Novamente: {list(res)}')  # assim como o map, após serem utilizados os dados, eles são excluídos da memória.

# Remoção de dados faltantes
paises = ['', 'Brasil', '', '', 'Chile', 'Venezuela']
print(f'Países com dados faltantes: {paises}')
res = filter(None, paises)  # none vai fazer com que os dados vazios sejam eliminados
print(f'Países filtrados: {list(res)}')
# Outras formas utilizando função
# res = filter(lambda pais: len(pais) > 0, paises
# res = filter(lambda pais: pais != '', paises)

"""
A diferença entre MAP e FILTER é: 
-> map() recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando
a função para cada elemento do iterável
-> filter() recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando
apenas os elementos de acordo com a função
"""