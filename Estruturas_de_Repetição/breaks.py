"""
Saindo de loops com breaks

Funciona da mesma forma que nas linguagens C ou Java
Break seve para sair de loops de maneira projetada
"""

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('fora do loop')

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
