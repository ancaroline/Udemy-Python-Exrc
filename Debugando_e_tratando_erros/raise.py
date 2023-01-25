"""
Levantando os próprios erros com raise
raise > Lança exceções
É uma palavra reservada, assim como def
Útil para possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:
raise TipoDoErro('Mensagem de erro')
# raise ValueError('Valor incorreto')
"""


# Exemplo

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')

# OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
