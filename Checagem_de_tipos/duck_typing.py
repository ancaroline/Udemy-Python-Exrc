"""
Duck Typing
O tipo ou a classe de um objeto é menos importante que os métodos que o define
e ao invés de checar a classe ou o tipo de dado, é checada a presença ou não de métodos
ou atributos específico.
"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))
nome = 'geek'
lista = [12, 11, 10]
dicio = {"carlos": 12}
print(len(nome))
print(len(lista))
print(len(dicio))

idade = 42  # não é similar ao outros. "pato"
print(len(idade))