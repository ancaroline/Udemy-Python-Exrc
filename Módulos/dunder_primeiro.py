def funcao1():
    print('Geek - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:  # este else é apenas para exemplificar, ele não existe
    print(f'primeiro.py foi importado {__name__}')
