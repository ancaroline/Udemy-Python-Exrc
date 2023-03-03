"""
POO - Métodos Mágicos -> são todos os métodos que utilizam dunder.

— dunder init
— dunder repr → Representação do objeto. Para o desenvolvedor e não para usuários finais.
— dunder str → Fazer a representação do objeto para os usuários finais.
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # Fazer a representação do nosso objeto / sobrescrevendo
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):  # Fazer a representação do objeto para os usuários finais.
        return self.titulo

    """O __str__ será representado primeiro, não é questão de ordem,
        é questão de preferência. Logo, o repr seria inútil junto com o str"""

    def __len__(self):
        return self.paginas  # eu defini que quero as paginas como tamanho
        # return len(self.titulo) # se quisesse o tamanho do titulo

    # Deletando
    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória.')

    # Adicionando objetos
    def __add__(self, other):  # retornando uma string com self(livro1) e other(livro2)
        return f'{self} - {other}'  # concatenando títulos

    # Fazendo operação de str com inteiro
    def __mul__(self, other):  # sempre o other deve ser do tipo inteiro
        if isinstance(other, int):
            msg = ''  # se for int, cria uma variável do tipo str
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Casquinha de ovo', 'João Augusto', 45)
livro2 = Livro('Nevou em Londres', 'João Assis', 116)
print(livro1)  # Sem o __repr__ mostraria o endereço de memória
print(livro2)

# Tentando o Len
print(len(livro1))  # não tem len
# porém, tem como usar o dunder que irá retornar o número de páginas do livro como tamanho

print(livro1 + livro2)  # quando utilizamos o +, estamos usando o método '__add__'

print(livro1 * 3)  # estamos utilizando o método '__mul__'