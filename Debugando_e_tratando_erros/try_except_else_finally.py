"""
Try / Except / Else / Finally
Quando tratar o código:
TODA A ENTRADA DO USUÁRIO DEVE SER TRATADA / TODA ENTRADA DEVE SER TRATADA
"""

# Exemplo

num = 0  # caso a variável seja capturada pelo erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
print(f'Você digitou {num}')

# else - executado somente se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:  # tenta receber o dado e converter para inteiro, se der erro: imprima a linha 20, caso não, imprima a linha 22.
    print(f'Você digitou {num}')

# finally - utilizado para fechar ou desalocar recursos
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:  # tenta receber o dado e converter para inteiro, se der erro: imprima a linha 20, caso não, imprima a linha 22.
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# Exemplo ERRADO
'''def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')
except TypeError:
    print('Divisão inválida')
except NameError:
    print('Valor incorreto')
else:
    print(dividir(num1, num2))
finally:
    print('Executando o finally')'''


# Exemplo CORRETO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero.'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))


# Exemplo Tratamento Genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))


# Exemplo Tratamento Semi-Genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))