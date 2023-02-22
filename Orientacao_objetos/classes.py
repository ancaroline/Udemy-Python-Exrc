"""
POO - Classes
Em POO, Classes são modelos dos objetos do mundo real sendo representados computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    Atributos > Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se a lâmpada
    é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela etc.

    Métodos (funções) > Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar
    no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum seria o sistema de ligar e desligar.

Para definir uma classe utilizamos: class
Utilizamos 'pass' quando temos um bloco de código que ainda não está implementado

Quando nomeamos nossas classes utilizamos por convenção o nome como inicial maiúsculo.
Se o nome for composto: iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica: Não utilizamos acentuação, caracteres especiais, espaços ou similares para nomes de classes,
atributos, métodos, arquivos etc.

Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
chamamos estes objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()
print(type(lamp))


valor = int('42')  # cast - convertendo a string para o tipo int
print(help(int))  # int é uma classe python (class int(object))
