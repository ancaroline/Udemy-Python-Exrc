"""
Reduce
OBS: A partir do python3+ a função reduce() não é mais uma função integrada (buil-in).
Agora temos que importar e utilizar esta função a partir do módulo 'functools'

Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes
um loop for é mais legível.
"""
""""
Para entender o reduce()
-> Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3,..., an]
# E você tem uma função que recebe dois parâmetros:
def funcao(x, y):
    return x * y
    
Assim como map e filter, a função reduce recebe dois parâmetros: a função e o iterável
-> reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento 
    e guarda o result.
    Passo 3: res3 = f(res2, a4)
    Isso é repetido até o final.

Alternativamente, poderíamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), an)
"""

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista
from functools import  reduce

dados = [1, 2, 3, 4, 5]
# para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)