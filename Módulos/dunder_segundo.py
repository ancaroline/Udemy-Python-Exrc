import dunder_primeiro


def funcao2():
    dunder_primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente.')
else:  # este else é apenas para exemplificar, ele não existe
    print(f'segundo.py foi importado. {__name__}')
