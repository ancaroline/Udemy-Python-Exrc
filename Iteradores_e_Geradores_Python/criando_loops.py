"""
Criando a sua própria versão de loop
"""
for num in [1, 2, 3, 4]:
    print(num)


# Criando
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek')