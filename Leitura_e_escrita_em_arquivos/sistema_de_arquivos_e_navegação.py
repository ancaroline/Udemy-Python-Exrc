"""
Sistema de Arquivos e Navegação
Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do módulo os.
os -> Operating System
"""
# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('C:\\workspace\\ws-python'))  # Absoluto True
print(os.path.isabs('workspace\\ws-python'))  # Relativo False

# Podemos identificar o sistema operacionaal com o módulo os
print(os.name)  # poxix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname()) -- Linux

import sys

print(sys.platform)

"""
O os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual
e o segundo, o diretório que será juntado ao atual.
"""
print(os.getcwd())
res = os.path.join(os.getcwd(), 'udemy')
os.chdir(res)
print(os.getcwd())

# Podemos listas os arquivos e diretórios com o listdir()
print(os.listdir())
print(os.listdir('C:\\'))
# quantos arquivos?
print(len(os.listdir()))


scanner = os.scandir()
# Podemos listar os arquivos e diretórios com mais detalhes com scandir()
print(list(os.scandir()))  # precisa converter para uma lista, pois gera um iterator

arquivos = list(scanner)
print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].inode())  # Identificador
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um file? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name())  # Nome do arquivo
print(arquivos[0].path())  # Caminho até o arquivo
print(arquivos[0].stat())  # Resultados estatísticos

# OBS: Quando utilizamos a função scandir() nós precisaremos fechá-la, assim quando abrimos um file

scanner.close()