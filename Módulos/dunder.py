"""
Dunder Name e Dunder Main
Dunder -> Doble Under
Dunder Name -> __name__
Dunder Main -> __main__

Em python são utilizados dunder para criar funções, atributos, propriedades,
utilizando Dundle Undeer para não gerar conflito com os nomes desses
elementos na programação.

# Se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é
o módulo de execução principal.
"""
from dunder_funcao import soma_impares

# o print do módulo não foi executado

import dunder_primeiro
import dunder_segundo