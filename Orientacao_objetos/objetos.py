"""
POO - Objetos
⇾ São instâncias da classe, ou seja,
após o mapeamento do objeto do mundo real para a sua representação computacional,
devemos poder criar quantos objetos forem necessários.
Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo
definido na classe.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instanciar um objeto do tipo lâmpada
"""Para instanciar um objeto, eu tenho que informar os parâmetros
que ele aguarda que eu passe no construtor
Neste caso tenho que passar: 
            def __init__(self, cor, voltagem, luminosidade):
Lembrando: O self é o próprio objeto."""

# Instâncias/Objetos do tipo Lampada
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
# Instâncias/Objetos do tipo ContaCorrente
cc1 = ContaCorrente(5000, 20000)
# Instâncias/Objetos do tipo Usuario
user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123')

# Podemos criar variáveis
nome = 'Angelina'
sobrenome = 'Augusto'
email = 'angel@gmail.com'
senha = '1234'
user = Usuario(nome, sobrenome, email, senha)
print(user)  # -- endereço de memória

cli1 = Cliente('João Gomes', '123.456.789-99')
cc = ContaCorrente(5000, 10000, cli1)
cc.mostra_cliente()