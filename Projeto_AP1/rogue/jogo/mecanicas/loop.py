from . import mecanicas

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.inimigos.chefe import Chefe
from ..personagens.tesouro import Tesouro
from ..personagens.obstaculo import Obstaculos
from ..gui.tela import Tela
from ..gui.input_texto import InputBox
from ..gui.menu_classe import MenuClasse

import pygame

TOTAL_OBSTACULOS = 5

def input_box(id_jogador):
    inputbox = InputBox(f"Informe o nome do aventureiro {id_jogador}:")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return inputbox.texto

            texto = inputbox.tratar_eventos(evento)
            if texto is not None:
                return texto

        inputbox.renderizar()

def selecionar_classe(id_jogador):
    menu = MenuClasse(f"Agora escolha a classe do aventureiro {id_jogador}:")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Aventureiro"

            if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clique = MenuClasse.selecionou_botao(pos)
                if clique:
                    return clique

        menu.renderizar()

def executar():
    tesouro = Tesouro()
    obstaculos = Obstaculos(TOTAL_OBSTACULOS, tesouro)
    aventureiros = [None, None]

    for i in range(2):
        nome = input_box(i + 1)
        classe = selecionar_classe(i + 1)
        match classe:
            case "Aventureiro":
                aventureiro = Aventureiro(nome, i)
            case "Guerreiro":
                aventureiro = Guerreiro(nome, i)
            case "Tank":
                aventureiro = Tank(nome, i)

        aventureiros[i] = aventureiro

    tela = Tela()

    jogo_encerrou = False
    i = 0
    while not jogo_encerrou:
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    return

                if not aventureiros[i].primeiro_movimento:
                    aventureiros[i].status = f"Continue explorando"
                aventureiros[i].primeiro_movimento = False

                direcao = mecanicas.determina_direcao(teclas, i)
                if direcao:
                    resultado_movimento = mecanicas.movimentar(aventureiros[i], direcao, obstaculos)
                    if resultado_movimento == 0:
                        aventureiros[i].fim_jogo = False
                        jogo_encerrou = True
                    else:
                        aventureiros[i].causar_dano_veneno()
                        if not aventureiros[i].esta_vivo():
                            aventureiros[i].status = f"{aventureiros[i]} foi morto por veneno..."
                            aventureiros[i].fim_jogo = False
                            jogo_encerrou = True
                        elif aventureiros[i].posicao == tesouro.posicao:
                            chefe = Chefe()
                            if mecanicas.iniciar_combate(aventureiros[i], chefe):
                                aventureiros[i].status = f"Parabéns! {aventureiros[i]} derrotou {chefe.nome} e encontrou o tesouro!"
                                aventureiros[i].fim_jogo = True
                            else:
                                aventureiros[i].status = f"{aventureiros[i]} foi derrotado pelo {chefe.nome}..."
                                aventureiros[i].fim_jogo=  False

                            jogo_encerrou = True
                        i = 1 - i

        tela.renderizar(aventureiros, tesouro, obstaculos.obstaculos, i)
        pygame.time.Clock().tick(60)
