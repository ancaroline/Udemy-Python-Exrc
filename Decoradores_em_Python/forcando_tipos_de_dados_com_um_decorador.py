"""
Forçando tipos de dados com um decorador
"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Geek'), int('3')
            return funcao(*novo_args, **kwargs)

        return converte

    return decorador


@forca_tipo(str, int)
def repete_mgs(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_mgs('Geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)


dividir('1', 5)