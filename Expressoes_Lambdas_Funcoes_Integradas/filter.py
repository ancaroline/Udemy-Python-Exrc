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

