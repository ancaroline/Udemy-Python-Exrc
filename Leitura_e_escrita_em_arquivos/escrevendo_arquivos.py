"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

"""
# Exemplo de escrita - modo 'w'
# Ao abrir um arquivo para escrita, o arquivo é criado no sistemaa operacional.

with open('escrevendo_arquivos.txt', 'w') as arquivo:  # a função write() recebe uma string como parâmetro
    arquivo.write('Primeira linha.\n')  # caso não for string, dará TypeError
    arquivo.write('Segunda linha.\n')
    arquivo.write('Terceira linha.\n')

"""
Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado.
Caso já exista, o anterior será apagado e um novo será criado. Dessa forma,
todo o conteúdo no arquivo anterior é perdido.
"""

# Forma tradicional de escrita em arquivo. Não Pythônica.
arquivo = open('escrevendo_arquivos2.txt', 'w')
arquivo.write('primeira linha.\n')
arquivo.close()

with open('escrevendo1000.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)

# Recebendo dados do usuário e escrevendo no arquivo
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
