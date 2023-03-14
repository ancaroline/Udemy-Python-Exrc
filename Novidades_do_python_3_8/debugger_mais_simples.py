"""
Debugger mais simples com f-strings
"""


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado = multiplicar(4.33, 5.44)
print(f'O resultado é {resultado}')
print(f'O resultado é {multiplicar(9, 2):.2f}')
# usando walrus
print(f'{(media := 8 / 2)} é a metade de {media * 2}')  # o parênteses vai dar o escopo da variável

####

geek: str = 'Geek University'
print(f"geek='{geek}'")
print(f'{geek=}')
print(f'{geek.upper()[::-1] = }')
