"""
POO - Métodos
- Métodos (funções): Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema.
Em Python, dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classe
OBS: Os método/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Por mais que possamos criar as nossas próprias funções utilizando dunder não é aconselhado.
Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.
"""

# Métodos de Instância
"""
Método de instância é o método que está dentro da própria classe.
O método dunder init é um método especial chamado de construtor
e a sua função é construir o objeto a partir da classe.
-> Métodos são escritos em letras minúsculas, se for nome composto, as palavras serão separadas com underline"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


"""
# Utilizando o pass lib
from passlib.hash import pbkdf2 sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  -- embaralhamento e tamanho da chave

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
        
    def checa_senha(self):
        if cryp.verify(senha, self.__senha):  -- método da própria ferramenta
            return True
        return False
"""

p1 = Produto('Playstation 4', 'Video Game', 2300)  # precisamos da instância do objeto para fazermos acesso a ele.
print(p1.desconto(10))
print(Produto.desconto(p1, 10))  # estamos passando o self no 'p1' e desconto. Self é o objeto em si.

# Usuario
user1 = Usuario('Carol', 'Aragão', 'carol@gmail.com', '1234')
user2 = Usuario('Sebastian', 'Augusto', 'sebastian@gmail.com', '1234')

print(user1.nome_completo())
print(Usuario.nome_completo(user1))
print(user2.nome_completo())

# Acesso de forma errada de um atributo de classe
"""Senha não criptografada"""
print(f'Senha User 1: {user1._Usuario__senha}')
print(f'Senha User 2: {user2._Usuario__senha}')

"""
Para a senha ficar criptografada é necessário instalar a biblioteca:
                    pip install passlib
                    
# Testando

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere.')
    exit(1)

print('Usuário criado com sucesso!')
senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido.')
else:
    print('Acesso negado.')

print(f'Senha User Criptografada: {user._Usuario__senha'}  -- Acesso errado
"""

# Métodos de Classe
"""
-> Métodos Estáticos
Métodos de classe não estão vinculados em nenhuma instância da classe, mas sim diretamente a ela.
Na declaração dos métodos é utilizado decorator para indicar que o método é de classe e não de instância.
"""


class UsuarioRefatorado:
    contador = 0

    @classmethod  # --> classmethod -> decorator para método de classe que recebe um parâmetro 'cls' (class)
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    @classmethod
    def ver(cls):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRefatorado.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        UsuarioRefatorado.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


user1 = UsuarioRefatorado('Carol', 'Aragão', 'carol@gmail.com', '1234')
UsuarioRefatorado.conta_usuarios()  # Forma correta
user1.conta_usuarios()  # Possível, mas incorreto

"""
QUANDO utilizar um Método de CLASSE ou Método de INSTÂNCIA?
        INSTÂNCIA
        -> Criamos métodos de instância quando esses métodos precisam fazer acesso a atributos de instância.
        CLASSE
        -> Quando não precisa fazer acesso a atributos de instância.
"""


# MÉTODOS PÚBLICOS E MÉTODOS PRIVADOS
# MÉTODOS PRIVADOS:

# Refatorando a classe Usuario

class UsuarioRefatoradoMP:
    contador = 0

    @classmethod  # --> classmethod -> decorator para método de classe que recebe um parâmetro 'cls' (class)
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    @staticmethod  # --> método estático --> não tem acesso à classe e nem a instância.
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRefatoradoMP.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        UsuarioRefatoradoMP.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # MÉTODO PRIVADO: Double underline na frente da variável.
    def __gera_usuario(self):  # --> Só é possível acessar dentro da classe.
        return self.__email.split('@')[0]


user = UsuarioRefatoradoMP('Felicity', 'Jones', 'felicity@gmail.com', '1234')
# print(user._UsuarioRefatoradoMP__gera_usuario())  # --> Acesso de forma ruim


# MÉTODO ESTÁTICO
"""Em Python temos os métodos de classe e métodos estáticos.
--> Utiliza o decorador @staticmethod
--> Não tem acesso à classe e nem a instância.
"""

print(UsuarioRefatoradoMP.contador)
print(UsuarioRefatoradoMP.definicao())
user = UsuarioRefatoradoMP('João', 'Jones', 'joao@gmail.com', '1234')
print(UsuarioRefatoradoMP.contador)
print(UsuarioRefatoradoMP.definicao())

