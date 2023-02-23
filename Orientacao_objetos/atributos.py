"""
Atributos
Representam as características do objeto.
Ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto.

Dividimos os atributos em 3 grupos:
    Atributos de instância;
    Atributos de classe;
    Atributos Dinâmicos;

-- Atributos de instância: São atributos declarados dentro do método construtor.
-- OBS: Método construtor: É um método especial utilizado para a construção do objeto.
Como seria em Java:
public class Lampada(){
    private int voltagem;  -- visível apenas na classe declarada
    public String cor;  -- visível em todo o projeto
    protected Boolean ligada = false;  -- visível apenas no pacote que esta classe se encontra

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
    # método
    public int getVoltagem(){
        return this.voltagem;
    }
}
"""
"""
Em Python:
Por convenção: TODO ATRIBUTO de uma classe é público, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se duplo underscore ( __ ) no início do seu nome. 
Isso também é conhecido também como Name Mangling.
"""


# Atributos de instância em Python:
# Atributos Privados
class Lampada:

    def __init__(self, voltagem, cor):  # método construtor  # self -> objeto que está executando o método
        self.__voltagem = voltagem  # private é o duplo underscore
        self.__cor = cor
        self.__ligada = False

    # método
    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


# Atributos Públicos
class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


# Atributos Públicos
"""class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor"""


# ps4 = Produto()  # método init sendo executado
# Atributos Públicos
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


"""self.senha = senha
O objeto Usuario no atributo senha vai receber senha."""

# Atributos Públicos e Atributos Privados
"""Quando estamos utilizando atributos de instância,
eles podem ser públicos ou privados
-> Publicos ou Privados = Visibilidade dos atributos
-> Atributo Privado: Pode ser acessado dentro da própria classe que foi declarado.
-> Atributo Público: Pode ser acessado por todo o programa"""


# Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


"""OBS: Isto é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos
acesso aos atributos sinalizados como privados fora da classe"""


# Exemplo:

class Login:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    # fazendo acesso ao atributo privado na classe
    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


user = Login('user@gmail.com', '1234')
print(user.email)
# print(user.__senha)  # AttributeError
print(dir(user))
print(user._Login__senha)  # Temos acesso. Mas não deveríamos ter esse acesso. --> Name Mangling
user.mostra_senha()

# O que significa atributos de instância?
"""
Significa, que ao criarmos instâncias/objetos de uma classe, 
todas as instâncias terão estes atributos.
"""
user1 = Login('user1@gmail.com', '34242')
user2 = Login('user2@gmail.com', '64643')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe
"""
Atributos de instância -> Os atributos que terão seus próprios valores de
acordo com a instância criada. Cada instância terá seus próprios valores.

        p1 = Produto('PlayStation 4', 'Video Game', 2300)
        p2 = Produto('Xbox S', 'Video Game', 4500)

Atributos de classe -> Atributos que são declarados diretamente na classe,
ou seja, fora do construtor. Geralmente já inicializamos um valor e este
valor é compartilhado entre todas as instâncias da classe. 
Ou seja, ao invés de cada instância da classe ter seus próprios valores
como é o caso dos seus atributos de instância, com os atributos de classe
todas as instâncias terão o mesmo valor para este atributo.
"""


# Refatorando a classe Produto
class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto # Em java, estes atributos são chamados de atributos estáticos
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

        Produto.contador = self.id  # Quando finalizar a criação do objeto. O contador terá o valor do id.
        # O contador é atributo de classe, por isso: nome_da_classe.nome_do_atributo


p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.
print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

"""Atributos de classe são chamados de Atributos Estáticos em Java."""

# Atributos Dinâmicos
"""Atributo de instância que pode ser criado em tempo de execução.
OBS -> O atributo dinâmico será EXCLUSIVO da instância que o criou."""

p3 = Produto('Arroz', 'Mercearia', 5.99)
# Criando um atributo dinâmico:
p3.peso = '5kg'  # Note que na classe Produto não existe o atributo peso.
print(f'Produto: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}') --> Erro

# Deletando atributos
print(p2.__dict__)
print(p3.__dict__)
print(Produto.__dict__)

# Deletando
del p3.peso
del p3.valor
del p3.descricao

print(p2.__dict__)
print(p3.__dict__)
