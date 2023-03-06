"""
Lendo arquivos CSV
CSV - Comma Separeted Values - Valores Separados por vírgula
# Separador por vírgula
    1, 2, 3, 4
    'geek', 'university'
# Separador por ponto e vírgula
    1; 2; 3; 4;
# Separador por espaço
    1 2 3 4

--> O importante é ter um padrão.
"""
# lendo arquivo csv

# Possível, mas não é o ideal (trabalhoso)
with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')  # gera uma lista com o separador vírgula
    print(dados)

"""A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV.
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderDicts"""

# Reader
from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# DictReader
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura em (cm)']}")
        # tem que estar escrito exatamente como o cabeçalho do arquivo

"""Por padrão, reader e dictreader utiliza a virgula como separador,
se houvesse outro:

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')  --> colocando ponto e vírgula
    for linha in leitor_csv:
        # Cada linha é um OrderDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura em (cm)']}")
"""