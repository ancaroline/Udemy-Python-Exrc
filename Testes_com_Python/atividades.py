def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'pois só se vive uma vez.'

    return f'Estou comendo {comida}, {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Estou atrasado, acordei tarde.'
    else:
        return f'Continuo cansado por dormir apenas {num_horas} horas.'