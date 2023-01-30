"""
O bloco try/except
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previninndo assim que o programa pare de funcionar e o usuário receba mensagens de erro
inesperadas.
A forma geral mais simples é:
try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema
"""

# Exemplo 1 - Tratando um erro genérico
# tente executar a função geek(), caso você encontre erros, imprima a mensagem de erros.
try:
    geek()
except:
    print('Deu algum problema')

# OBS: Tratar erro de forma genérica não é a melhor forma. Trate de forma específica.
# Exemplo 2 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de errs de uma vez.

try:
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, "game"))
