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
