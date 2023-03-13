"""nomes: list = ['João', 'Maria']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {3, 4, 5}"""

"""from typing import Dict, List, Tuple, Set

nomes: List[str] = ['João', 'Maria']
versoes: Tuple[int, int, int] = (3, 4, 7)
opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}
valores: Set[int] = {3, 4, 5}"""

# Versão 1 - Sem type hinting

import random

NAIPES = '♠ ♡ ♢ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    # para cada naipe e carta, para carta in cartas, para naipe in naipes
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()