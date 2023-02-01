"""
Debugando código com PDB
PDB -> Python Debugger
"""


# OBS: A utilizaçãoo do print() para debugar código é uma prática ruim.
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))


# Existem formas mais profissionais de fazer o 'debug', utilizando o debugger

# Exemplo com o PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

"""
Colocando 'breakpoints' para onde começar e terminar o debugg.
Iniciando o debugg, selecionando uma parte do código e ativar a função 'add to watches' 
irá mostrar o resultado daquele determinado código.
"""

# Exemplo com o PDB - Python Debugger - Exemplo 1
"""
Para utilizar o Python Debugger,
precisamos* importar a biblioteca PDB e então utilizar a função set_trace()
* A partir do Python 3.7, não é mais necessáario importar a biblioteca pdb,
pois o comando de debug foi incorporado como função built-in (integrado) chamada
breakpoint()
"""
# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()  # breakpoint no pdb
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 2

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb;

pdb.set_trace()  # Dois comandos na mesma linha, ponto e virgula
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# utilizar este formato?
"""
O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports
de bibliotecas no inicio do arquivo. Por isso, ao invés de colocarmos o import
do pdb no início do arquivo, nós colocamos somente onde vamos debuggar, e ao finalizar,
fazemos a remoção.
"""

# Exemplo 3
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
# Se os nomes das variáveis forem as mesmas dos comandos pdb, utilize o 'p' na frente da variável
