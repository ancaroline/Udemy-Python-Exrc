"""
Funções com Parâmetro Padrão (Default Parameters)
-> Funções onde a passagem de parâmetro seja opcional
"""
# Exemplo de parâmetro opcional:
print('olá')
print()


# Exemplo de parâmetro obrigatório:
def quadrado(numero):
    return numero ** 2


print(quadrado(3))
# print(quadrado()) TypeError - precisa ter um parâmetro


# Exemplo de parâmetro padrão/opcional
def exponencial(numero, potencia=2):  # se um parâmetro já recebe um valor, ele já se torna opcional
    return numero ** potencia


print(exponencial(2))
print(exponencial(3, 5))  # o argumento 5 irá substituir o valor 2
