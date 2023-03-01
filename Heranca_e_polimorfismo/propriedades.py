"""
POO - Propriedades - Properties
"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    """
    A melhor forma da gente ter acesso a valores de atributos é:
    criando métodos para manipulá-los.
    Esses métodos são chamados de getters e setters
    """
    """Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
    costumamos a criar métodos públicos para manipulação desses atributos.
    Esses métodos são conhecidos por getters e setters, onde os GETTERS RETORNAM o valor
    do atributos e os SETTERS ALTERAM o valor do atributo."""

    # GET -> acessar os valores dos atributos
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    # SET -> Retorna o valor e altera o atributo
    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

"""
soma = conta1._Conta__saldo + conta2._Conta__saldo  --> Acesso Errado! A melhor forma para ter acesso: getters e setters
print(f' A soma do saldo das conts é {soma}')  
"""
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(99999)
print(conta1.__dict__)

# EM PYTHON
"""UTILIZAMOS PROPRIEDADES"""


# Para utilizar usaremos decorator


class Conta:
    contador = 0

    # Construtor
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    """Se precisar de get e set, crie, se não, não crie.
    Se for necessário consultar -> get
    Se for necessário consultar e alterar -> set"""
    # property
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # Criando um SET para o limite
    @limite.setter  # @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    # Métodos de instância
    # É possível criar métodos como propriedades
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Saber o valor total que o seu cliente tem em caixa, juntando o saldo e o limite
    @property
    def valor_total(self):  # usar um método como uma propriedade
        return self.__saldo + self.__limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

soma = conta1.saldo + conta2.saldo  # acessando a propriedade saldo e não o atributo
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76842
print(conta1.__dict__)
print(conta1.limite)  # imprimindo o valor

print(conta2.valor_total)
print(conta1.valor_total)