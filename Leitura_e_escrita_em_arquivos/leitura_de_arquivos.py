"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo, utilizamos a função integrada open().

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso, é caminho para o arquivo a ser lido.
Essa função retornaa um _io.TextIOWrapper e é com ele que trabalhamos.

OBS: Por padrão, a função open() abre o arquivo para leitura.
Este arquivo deve existir, ou então teremos o erro FileNotFoundError
"""

# Exemplo
arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

# para ler o conteúdo de um arquivo, após sua abertura devemos utilizar a função read()
# print(arquivo.read())
# OBS: Python utiliza um recurso para trabalhar com arquivos chamado cursor.
# Esse cursor funciona como o cursor quando estamos escrevendo.
# -> A função read() lê todo o conteúdo do arquivo

ret = arquivo.read()
print(type(ret))
print(ret)
# ret = ret.split('\n') # separar pela quebra de linha
