"""
Definindo funções:
-> Pequenas partes do código que executam uma tarefa específica;
-> Pode ou não receber entradas de dados e retornar uma saída de dados;
-> Muito úteis para executar procedimentos similares por repetidas vezes;
OBS: se você escrever uma função que realiza várias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções:
print, len, max, min, count...
"""
# Exemplo de utilização de funções:
cores = ['verde', 'amarela', 'azul', 'branco']

# Utilizando a função integrada (Built-int) do Python print()
print(cores)
# DRY - DON'T REPEAT YOURSELF
"""
Como definir funções?

def nome_da_funcao(parameters_de_entrada):
    bloco_da_funcao

Onde: nome da função -> SEMPRE com letras minúsculas
Se for nome composto, underline (Snake Case)
parameters de entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula
bloco da função -> corpo da função ou implementação. Onde o processamento acontece.
Pode ter ou não retorno da função
OBS: Para definir uma função, utilizamos a palavra reservada 'def', informando ao python que
estamos definindo uma função. Também abrimos o bloco de código com o ' : '
"""


# Definindo a primeira função
def diz_oi():
    print('oi!')


"""
OBS: 
1 - Dentro das nossas funções podemos utilizar outras funções
2 - Nossa função só executa 1 tarefa
3 - Esta função não recebe nenhum parâmetro de entrada
4 - Esta função não retorna nada
"""

# Utilizando funções — Chamada
diz_oi()  # Necessário utilizar os parênteses


# Exemplos 2
def cantar_parabens():
    print('Parabéns')
    print('Nesta data querida')
    print('Muitas felicidades')


for n in range(5):
    cantar_parabens()

# Podemos criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens
canta()
