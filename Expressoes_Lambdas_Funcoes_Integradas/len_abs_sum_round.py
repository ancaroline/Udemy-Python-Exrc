"""
Len, Abs, Sum, Round
-> Len() - retorna o tamanho, o número de itens de um iterável
Quando utilizamos a função len, o Python faz o seguinte:
dunder len
print('Geek'.__len__())

-> abs() -> retorna o valor absoluto de um número inteiro ou real.
Seria o seu valor real sem o sinal
"""
# Exemplo Abs
print(abs(-5))
print(abs(3.4))
print(abs(-6.8))
# não existe abs de string.

"""
Sum
sum() -> recebe como parâmetro um iterável, podendo receber um valor inicial
e retorna a soma total dos elementos incluindo o valor inicial
Obs: O valor inicial default = 0
"""
# Exemplo
print(sum([1, 2, 3]))
print(sum([1, 2], 3))  # exemplo de utilização: soma de produtos + frete
print(sum([3.3, 6.2]))
print(sum((1, 2, 3)))
print(sum({1, 2, 3}))
print(sum({'a': 1, 'b': 2}.values()))

"""
round() -> retorna um número arredondado para n digito de precisão
após a casa decimal. Se a precisão não for informada retorna o inteiro mais próximo da entrada.
"""
# exemplo round
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.28863723, 2))  # duas casas de precisão
