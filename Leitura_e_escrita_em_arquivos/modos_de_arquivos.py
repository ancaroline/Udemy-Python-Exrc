"""
Modos de Abertura de Arquivo
r - open for reading - default
w - open for writing - truncating the file first
'x' - open for exclusive creation, failing if the file already exists
'a' - open for writing, appending to the end of file if it exists
'b' - binary mode
't' - text mode (default)
'+' - open for updating (reading r+ and writing w+)

The default mode is 'r' (open for reading text, a synonym of 'rt').
Modes 'w+' and 'w+b' open and truncate the file.
Modes 'r+' and 'r+b' open the file with no truncation.
"""
# Exemplo 'x'
try:
    with open('frutas.txt.', 'x') as arquivo:  # -> Err:  FileExistsError
        arquivo.write('Teste')
except FileExistsError:
    print('Arquivo já existe')

# 'a'
# Opening in mode 'a' -> append, se o arquivo não existir será criado.
# Caso exista, o novo conteúdo será adicionado ao final.

# O novo conteúdo será adicionado ao final do arquivo SEMPRE
with open('frutas.txt', 'a') as arquivo:
    arquivo.seek(0)  # não é possível controlar o cursor
    arquivo.write('Lista de frutas:\n')

# Exemplo r+ - temos o controle do cursor
with open('frutas.txt', 'r+') as arquivo:
    arquivo.write('Mural de frutas\n')
    arquivo.seek(11)
    arquivo.write('Segundo grupo de frutas: \n')
    arquivo.seek(12)
    arquivo.write('Últimas frutas.\n')