"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.
Sintaxe:
variavel := expressão
"""
from typing import Dict, List, Tuple, Set

nome: str = 'Geek'
print(nome)

# com walrus
nome: str
print(nome := 'Geek')

# sem walrus

cesta: List[str] = []
fruta: str = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

# com walrus
cesta: List[str] = []
fruta: str
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)

print(cesta)
