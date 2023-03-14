"""
- Literal type
- Union
- Final
- Typed dictionaries
- Protocols
"""

# LITERAL TYPE
from typing import Literal


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass
    """Vai retornar uma string que pode ser: ou a string conectado ou desconectado."""


# Imagina que temos uma função que conforme o parâmetro ela faz uma coisa ou outra
def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # !r -> coloca o valor em aspas simples


calcula_v1('+', 6, 4)
calcula_v1('-', 6, 4)
calcula_v1('*', 3, 5)


# Com Literal type
def calcula_v1(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # !r -> coloca o valor em aspas simples


calcula_v1('+', 6, 4)
calcula_v1('-', 6, 4)
calcula_v1('*', 3, 5)  # acusará o erro

# UNION
from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é grande.'
    else:
        return resultado


# FINAL
from typing import Final

# para criar constantes
NOME: Final = 'Geek'

from typing import final  # -> importando um decorator


@final  # quando a gente decora uma classe com final: nenhuma outra classe pode extender ela.
class Pessoa:
    pass


class Estudante(Pessoa):  # então isto é um erro
    pass

    @final
    def estudar(self):  # não pode extender em classes filhas
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):  # então isto é um erro
        print('Estudando e estagiando')


# Typed Dictionaries
from typing import TypedDict


class CursoPython(TypedDict):
    # cria um adicionario, chave e valor
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2023)
print(geek)

# Potocols
from typing import Protocol


class Curso(Protocol):
    titulo: str  # todo objeto que seguir esse protocolo terá o atributo 'título'
    # não pode ser instanciado

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Python'  # -> atributo titulo


v1 = Venda()  # -> venda não tem o tipo título
estudar(v1)
