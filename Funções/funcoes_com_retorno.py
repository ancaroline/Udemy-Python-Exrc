"""
Funções com retorno

OBS: Quando uma função não retorna nenhum valor, o retorno é None
Não precisamos necessariamente criar uma variável para recebemos o retorno de uma função.
Podemos passar a execução da função para outras funções.
"""


# Exemplo de Função sem retorno
def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()
print(f'Retorno {ret}')


# Refatorando a função
def quadrado_de_7():
    return 7 * 7  # deve retornar o valor com a palavra return


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')
print(f'Retorno: {quadrado_de_7() + 1}')


# Refatorando a função 'diz_oi'
def diz_oi():
    return 'Oi '


alguem = 'Pedro!'
print(diz_oi() + alguem)




