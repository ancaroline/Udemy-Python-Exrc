"""
Geradores
- Geradores (Generators) são Iterators (Iteradores):
Mas, nem todo iterator é generator
1. Generators podem ser criados com funções geradores;
2. Funções geradoras  utilizam a palavra reservada 'yield';
3. Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)
------------------------------------------------------------------------------
/ Funções                          / Generator Functions                     |
------------------------------------------------------------------------------
/ utilizam return                  / utilizam yield                          |
------------------------------------------------------------------------------
/ retorna uma vez                  / podem utilizar yield múltiplas vezes    |
------------------------------------------------------------------------------
/ quando execut., retorna um valor / quando execut., retorna um generator    |
------------------------------------------------------------------------------

"""


# Exemplo Função Geradora (Generator Function)
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# Um Generator Function não é um Generator. Ela gera um generator.

gen = conta_ate(5)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
for num in gen:
    print(num)

gen = conta_ate(3)
print(next(gen))  # 1
print('Geek')
for num in gen:
    print(num)  # continua a partir do 2

# É possível gerá-los de uma só vez
gen = list(conta_ate(3))
print(gen)
