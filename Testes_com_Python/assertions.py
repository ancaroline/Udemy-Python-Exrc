"""
Assertions (Afirmações/Checagens/Questionamentos)

'assert' -> realizar simples afirmações utilizadas nos testes
Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro
personalizada.
# OBS: A palavra 'assert' pode ser utilizada em qualquer funçõe ou cósigo, não precisa ser exclusivamente
nos testes.
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 4)
ret = soma_numeros_positivos(-2, 4)  # AssertionError
# print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'batata frita'
    ], 'A comida precisa ser fast food.'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar 'assert'
"""Se um programa Python for executado com parâmetro -O,
nenhum assertion será validado, todas as suas validações já eram."""