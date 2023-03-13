"""
Tipos em comentários
"""
import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')
