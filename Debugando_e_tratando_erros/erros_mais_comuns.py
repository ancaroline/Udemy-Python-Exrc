"""
Erros mais comuns
- SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe.
    Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.
    Exemplos:
    1. Faltam os parênteses
    def funcao:
        print('Geek')
    2. Não pode atribuir valor em palavras reservadas
    None = 1
    3. Return deve ser posto dentro de uma função
    return

- NameError -> Ocorre quando uma variável ou função não foi definida.

- TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado
    Exemplos:
    1. print(len(5))
    2. print('Geek' + [])

- IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro
    tipo de dado indexado utilizando um índice inválido.
    Exemplos:
    1. lista = ['Geek']
        print(lista[2])

- ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe
    um argumento com tipo correto, mas valor inapropriado.
    Exemplos:
    1. print(int('Geek')

- KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
    Exemplos:
    1.
    dic = {'python': 'university'}
    print(dic['geek'])

- AttributeError -> Ocorre quando uma variável não tem um atributo/função
    Exemplos:
    1.
    tupla = (11, 2, 3, 2)
    print(tupla.sort()) # o sort é da lista e não da tupla

- IndentationError -> Ocorre quando não respeitamos aa indentação do Python (4 espaços)

OBS: Exceptions e Erros são sinônimos na programação 
"""
