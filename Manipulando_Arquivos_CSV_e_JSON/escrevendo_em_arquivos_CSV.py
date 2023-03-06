"""
Escrevendo em arquivos CSV
reader(), writer()
writerow() -> escreve uma linha
"""

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV,
# Utilizamos o método writerow() p/ escrever cada linha. Este método recebe uma lista.
from csv import writer

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])


# Para acrecentar, utilizar 'a' e não 'w'
# with open('filmes.csv', 'a', encoding='utf-8') as arquivo:

# DictWriter

from csv import DictWriter
# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho
with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Títutlo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({'Títutlo': filme, 'Gênero': genero, 'Duração': duracao})