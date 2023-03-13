"""
mypy-lang.org
pip install mypy
terminal -> mypy arquivo.py

1. Utilize o type hinting
2. Utilizar o mypy para verificar
"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek'))
print(cabecalho('geek', alinhamento=False))
