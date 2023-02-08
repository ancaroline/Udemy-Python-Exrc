"""
Seek e Cursors
seek() -> Utilizada para movimentar um cursor pelo arquivo.
"""
arquivo = open('texto.txt')
print(arquivo.read())
print(arquivo.read())  # virá vazio

# Movimentando o cursor pelo arquivo com a função seek()
# A função recebe um parâmetro que indic onde queremos colocar o cursor.

arquivo.seek(0)
print(arquivo.read())

# é possível limitar o conteúdo que será lido pelo read
arquivo.seek(0)
print(arquivo.read(4))  # será lido apenas 4 caracteres: 'prim'

arquivo.seek(14)  # a partir do caracter 14
print(arquivo.read())

# readline() — função que lê o arquivo linha a linha
arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())

arquivo.seek(0)
ret = arquivo.readline()
print(type(ret))
# transformar em uma lista separando por espaço
print(ret.split(' '))

#  readlines() - cada item em uma lista de strings
arquivo.seek(0)
print(arquivo.readlines())
arquivo.seek(0)
linhas = arquivo.readlines()
print(len(linhas))

"""
OBS: Quando abrimos um arquivo com a função open é criada uma conexão entre
o arquivo no disco do computador e o nosso programa. Essa conexão é chamada de
streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão.
Para isso utilizamos o close.
"""
# Passos para se trabalhar com um arquivo:
# 1 - Abrir o arquivo
arquivo = open('texto.txt')
# 2 - Trabalhar o arquivo
print(arquivo.read())
print(arquivo.closed)  # verifica se o arquivo está aberto ou fechado. True / False
# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)  # True

# Se tentarmos manipular o arquivo após fechado, teremos um ValueError
