import random

from .armadilha import Armadilha

from jogo.personagens.inimigos.aranha import Aranha
from jogo.personagens.inimigos.esqueleto import Esqueleto
from jogo.personagens.inimigos.golem import Golem

import pygame

def iniciar_combate(aventureiro, monstro):
    """
    Executa um loop infinito, que possui as seguintes etapas:
    - Calcula o dano causado pelo aventureiro
    - Monstro faz a sua defesa
    - Exibe na tela o dano causado pelo aventureiro e a vida atual do monstro
    - Se o monstro não está mais vivo, retorna True
    - Calcula o dano causado pelo monstro
    - Aventureiro faz sua defesa
    - Exibe na tela o dano causado pelo monstro e a vida atual do aventureiro
    - Se o aventureiro não está mais vivo, retorna False
    """
    while True:
        dano = aventureiro.atacar()
        monstro.defender(dano)
        if not monstro.esta_vivo():
            aventureiro.status = f"{monstro.nome} foi derrotado!"
            aventureiro.ganhar_xp(monstro.xp)
            return True

        dano = monstro.atacar()
        aventureiro.defender(dano)
        if not aventureiro.esta_vivo():
            aventureiro.status = f"{aventureiro.nome} foi derrotado!"
            return False

def determina_direcao(teclas, i):
    if i == 0:
        teclas_validas = {
            pygame.K_a: "A",
            pygame.K_w: "W",
            pygame.K_s: "S",
            pygame.K_d: "D"
        }
    else:
        teclas_validas = {
            pygame.K_LEFT: "A",
            pygame.K_UP: "W",
            pygame.K_DOWN: "S",
            pygame.K_RIGHT: "D"
        }

    for tecla, direcao in teclas_validas.items():
        if teclas[tecla]:
            return direcao

    return ""

def movimentar(aventureiro, direcao, obstaculos):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a o método andar do objeto aventureiro e analisa o seu resultado.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Retorna 0 se o aventureiro morreu.
    Retorna 1 se o aventureiro venceu um combate.
    Retorna 2 se nada aconteceu.
    """
    pos_futura = aventureiro.calcular_pos_futura(direcao)
    if obstaculos.verificar_posicao(pos_futura):
        aventureiro.andar(pos_futura)
    else:
        return 2

    evento = random.choices(["armadilha", "nada", "monstro"], [0.2, 0.4, 0.4])[0]
    if evento == "armadilha":
        Armadilha().aplicar_efeito(aventureiro)
        if not aventureiro.esta_vivo():
            return 0
    elif evento == "monstro":
        inimigo = random.choices([Aranha, Esqueleto, Golem], [5, 2, 1])[0]()
        return int(iniciar_combate(aventureiro, inimigo))

    return 2
