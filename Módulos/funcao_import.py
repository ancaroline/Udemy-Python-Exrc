def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
            # return total -> o return finaliza a função, seria um erro colocá-lo aqui
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))


def multiplica(num1, num2):
    return num1 * num2
