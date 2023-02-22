"""
Sistemas de Arquivos - Manipulação
"""
import os

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Diretório
# Path relativos
print(os.path.exists('workspace'))

# Path absoluto
print(os.path.exists('/Udemy-Python-Exrc/Colecoes'))

# Criando e fechando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()
# Forma 2
open('arquivo-teste2.txt', 'a').close()
# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass
# Melhor forma
# Funciona no Linux:
# os.mknod('arquivo-teste4.txt')
# os.mknod('path absoluto/arquivo.txt')
# Se o arquivo já existir -> FileExistsError

# Criar diretórios - únicos (um a um)
os.mkdir('templates')
# os.mkdir('path absoluto\templates')
# Se o diretório já existir -> FileExistsError
# se não tivermos permissão para criar diretórios, teremos PermissionError

# Criando árvore de diretórios
os.makedirs('templates1/test1/test2')

# se os diretórios existirem, ignore
os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios
os.rename('templates1', 'template3')  # se o diretório não existir -> FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos OSError
os.raname('templates1/test1/test2/test3.txt', 'templates1/test1/test2/arquivo.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção.
# Ao deletarmos um file ou dir, eles não vão para a lixeira. Eles somem.

# Removendo um arquivo
os.remove('arquivo-teste3.txt')
# No Windows, se tentar deletar um file aberto/em uso, ocorrerá um erro.
# Caso o arquivo não exista, teremos o FileNotFoundErrors
"""Se informar um dir ao inveés de um arquivo, teremos um IsADirectoryError"""

# Removendo diretórios VAZIOS
os.rmdir('templates')  # se tiver qualquer conteúdo, teremos: OSError
# Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de arquivos
for arquivo in os.scandir('templates4'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios
os.removedirs('templates5/test1')
"""
Se algum dos diretórios contiver arquivos ou outros diretórios,
o processo para.
"""
# send2trash

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

"""Criamos um dir temporario, abrindo e dentro dele criando um file
para escrevermos um texto. No final usamos um input só para 
mantermos os arquivos temporários vivos dentro do bloco with."""
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek\n')
    input()

# OBS: Possivelmente, o código acima não irá funcionar se tiver utilizando Windows.

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek\n')  # convertendo string em binário
    tmp.seek(0)
    print(tmp.read())

# sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# sem o bloco with
arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek\n')
print(arquivo.name)
input()
arquivo.close()
