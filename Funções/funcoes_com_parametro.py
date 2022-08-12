"""
Funções com Parâmetro (de entrada)
-> Funções que recebem dados para serem processados dentro da mesma
Se a gente pensar em um programa, temos:
entrada -> processamento -> saída
Se a gente pensar em uma função, já sabemos que temos funções:
— Não possuem entrada
— Não possuem saída
— Possuem entrada, mas não saída
— Não possuem entrada, mas sim saída
— Possuem entrada e saída
"""


# função
def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())  # sempre será o mesmo resultado, pois não tem nenhuma entrada e o processamento é o mesmo


# refatorando
def quadrado(numero):  # será quadrado do número que receber
    return numero * numero
    # return numero ** 2


print(quadrado(4))


# refatorando segunda função
def cantar_parabens(aniversariante):
    print('Parabéns')
    print('Nesta data querida')
    print('Muitas felicidades')
    print(f'Viva o/a {aniversariante}!')


cantar_parabens('Carol')

"""
Funções podem ter N parâmetros de entrada.
Ou seja, podemos receber como entrada em uma função quantos parâmetros forem necessários.
Eles são separados por vírgula.
"""


# Exemplo
def soma(a, b):  # parâmetros
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def exemplo(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))  # argumentos
print(multiplica(2, 8))
print(exemplo(3, 2, 'Geek '))


# Se a gente informar um número errado de parâmetro ou argumento, teremos TypeError

# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Caroline', 'Aragão'))

"""
Diferença entre parâmetros e argumentos
-> Parâmetros são variáveis declaradas na definição de uma função
-> Argumentos são dados passados durante a execução da função
-> A ordem dos parâmetros importa!
"""

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem
nome = 'João'
sobrenome = 'Carlos'
print(nome_completo(nome='Carol', sobrenome='Aragão'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
# a partir do momento que utilizo argumentos nomeados, posso inverter a ordem:
print(nome_completo(sobrenome='Marques', nome='Juca'))


# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
            # return total -> o return finaliza a função, seria um erro colocá-lo aqui
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

