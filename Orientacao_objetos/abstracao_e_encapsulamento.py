"""
POO — Abstração e Encapsulamento

Objetivo da POO: encapsular o nosso código dentro de um grupo lógico e hierárquico utilizando classes.
Encapsulamento -> agrupamento de atributos e métodos

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa,
contendo um atributo privado chamado __nome
e um método privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe.
Mas Python são bloqueia este acesso fora da classe.
Com Python acontece um fenômeno chamado Name Mangling,
que faz uma alteração na forma de se acessar os elementos privados, conforme:

_Classe__elemento
Exemplo - Acessando elementos privados fora da classe:  (acesso errado)
instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e métodos privados do usuário.
"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador  # receber o número 400
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta1 = Conta('Augusto', 150.00, 1500.0)
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# Como o acesso está público, podemos alterar os dados
conta1.saldo = 9999999
conta1.limite = 9999999999

print(conta1.__dict__)
conta1.extrato()


# Para tornar os atributos seguros é necessário estar privado
# Refatorando

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador  # receber o número 400
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência
        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


conta1 = Conta('Augusto', 150.00, 1500.0)
# Name Mangling
print(conta1._Conta__titular)  # não poderia fazer esse acesso
conta1._Conta__titular = 'Jack'
print(conta1.__dict__)

conta1.depositar(200)
print(conta1.__dict__)

conta1.sacar(200)
print(conta1.__dict__)

conta2 = Conta('Januario', 300.0, 2000.0)
conta1.extrato()
conta2.extrato()

conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()