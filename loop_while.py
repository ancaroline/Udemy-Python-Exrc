"""
Loop while
--> do while não tem em python

Forma geral:
while expressão_booleana:
    //execução do loop

O bloco será repetido enquanto a expressão for verdadeira.

"""

numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
# OBS: É importante ter o critério de parada

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')