"""
POO - Herança (Inheritance)
A ideia de herança é a de reaproveitar código. Também extender nossas classes.
OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidades?
Sim. 'Pessoa'.

OBS: Quando uma classe herda de outra classe,
ela herda todos os atributos e métodos da classe herdada.
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # Esse Cliente é do tipo Pessoa
    """
    A partir do momento que eu falo que Cliente é do tipo Pessoa,
    eu posso retirar o método e os atributos do construtor de Cliente deixando
    apenas renda.
    Exemplo:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    Depois:

    def __init__(self, renda):
    self.__renda = renda

    A partir do momento que uma classe herda da outra,
    devemos utilizar o construtor da classe de cima,
    utilizando o super().__init__
    Com o super() é possivel acessar qualquer método ou atributo da super classe.
    """

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # Modo que faz acesso ao construtor de Pessoa
        # Isto é o mesmo de:
        #       Pessoa.__init__(self, nome, sobrenome, cpf)  -> Forma não comum.
        self.__renda = renda

    """
    Quando uma classe herda de outra classe, a classe herdada é conhecida por:
        [Pessoa]
        - Super classe;
        - Classe mãe;
        - Classe pai;
        - Classe base;
        - Classe Genérica;
        
    Quando uma classe herda de outra classe, a classe herdeira é conhecida por:
        [Cliente, Funcionario]
        - Sub Classe;
        - Classe filha;
        - Classe específica;
    """


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Exemplo de Overriding
    def nome_completo(self):
        print(super().nome_completo())  # Com o super é possível acessar qualquer atributo ou método da superclasse
        print(self._Pessoa__cpf)  # Aqui não é preciso o super, pois funcionario herda de pessoa.
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Renan', 'Duarte', '123.56.789-99', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

# Sobrescrita de Métodos (Overriding)
"""Quando trabalhamos com herança pode ocorrer que na super classe
tenha um método que é comum nas classes filhas, exemplo:

        def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
        
Este método foi comum para Cliente e Funcionario.
Mas pode acontecer de haver uma classe que não necessite desse método
ou que o método seja insuficiente. Isto não há problema, pois é possível
replementar o mesmo método na classe filha.
Este processo é chamado de Overriding.
"""
