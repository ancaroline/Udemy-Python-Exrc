"""
O bloco with é utilizado para criar um contexto de trabalho onde
os recursos utilizados são fechados após o bloco with.
"""
# o bloco with - Forma pythonica de manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())

# não precisa fazer o fechamento do arquivo
print(arquivo.closed)