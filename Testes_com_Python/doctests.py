"""
Doctests

São testes que colocamos na docstring das funções/métodos Python.
Para rodar um test do doctest:
python -m doctest -v nome_do_modulo.py
"""


def soma(a, b):
    """Soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


"""Para executar o teste pelo terminal:
        python -m doctest -v doctests.py -> doctests.py é o nome do arquivo"""


# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


# Erro inesperado ...
"""Se tivesse com aspas duplas daria erro.
Dentro do doctest, o Python não reconhece string com aspas duplas."""


def fala_oi():
    """Fala oi

    >>> fala_oi()
    'oi'
    """
    return "oi"


# Outro caso ...
"""Cuidado com espaços sem necessidade."""

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
