# Versão 2 - Com type hinting
from typing import Dict, List, Tuple, Set
import random

NAIPES = '♠ ♡ ♢ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio: bool = False) -> List[Tuple[str, str]]:
    """Cria um baralho com 52 cartas"""
    baralho: List[Tuple[str, str]] = [(n, c) for c in CARTAS for n in NAIPES]
    # para cada naipe e carta, para carta in cartas, para naipe in naipes
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]]]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas: List[Tuple[str, str]] = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, List[Tuple[str, str]]] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
