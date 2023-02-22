"""
Programação Orientada a Objetos — POO
— POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real para modelos computacionais
— Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.
Paradigmas de programação -> metodologia. Como você vai pensar em desenvolver o seu software?
Principais elementos da POO:
Classe > Modelo do objeto do mundo real sendo representado computacionalmente;
Atributo > Características do objeto;
Método > Comportamento do objeto (funções);
Construtor > Método especial utilizado para criar os objetos a partir de uma classe;
Objeto > Instância da classe.
"""
# A partir do momento que estamos criando a nossa própria classe:
# Nós estamos definindo o nosso próprio tipo de dado

numero = 10
print(numero)
print(type(numero))


class Produto:
    pass


ps4 = Produto()  # construtor padrão; ps4 é um objeto da classe produto;
print(ps4)  # endereço de memória
print(type(ps4))
