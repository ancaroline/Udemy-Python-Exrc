"""
Escopo de variáveis
"""
"""
Reatribuição
"""
numero = 42 # Exemplo de variável global
print(numero)

numero = 'geek'
print(numero)

numero = 42
if numero > 10:
    novo = numero + 10 # Exemplo de variável local
    print(novo)