"""
Type Hinting
"""


def cumprimentar(nome: str) -> str:  # o tipo de parâmetro -> o tipo de retorno
    return f'Olá. {nome}'


print(cumprimentar('Geek'))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek'))
print(cabecalho('geek', alinhamento=False))