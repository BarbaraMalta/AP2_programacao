from .cores import CORES

import pygame

FONTE_TAMANHO = 25
MARGEM = 10
FONTE = "Lucida Console"
LARGURA = 650
ALTURA = 100

LB = (LARGURA - 3 * MARGEM) // 2
AB = 50

class MenuClasse:
    def __init__(self, mensagem):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        self.fonte = pygame.font.SysFont(FONTE, FONTE_TAMANHO)
        self.prompt = mensagem

    @staticmethod
    def selecionou_botao(pos):
        x, y = pos

        if MARGEM <= x <= MARGEM + LB and ALTURA - MARGEM - AB <= y <= ALTURA - MARGEM:
            return "Guerreiro"
        if LARGURA - MARGEM - LB <= x <= LARGURA - MARGEM and ALTURA - MARGEM - AB <= y <= ALTURA - MARGEM:
            return "Tank"

        return ""

    def renderizar(self):
        self.display.fill(CORES.preto)

        # prompt
        texto = self.fonte.render(self.prompt, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

        # botões
        botao = pygame.Rect(MARGEM, ALTURA - MARGEM - AB, LB, AB)
        pygame.draw.rect(self.display, CORES.branco, botao)

        botao = pygame.Rect(LARGURA - MARGEM - LB, ALTURA - MARGEM - AB, LB, AB)
        pygame.draw.rect(self.display, CORES.branco, botao)

        # textos
        texto = self.fonte.render("Guerreiro", True, CORES.verde)
        x = MARGEM + (LB - texto.get_width()) // 2
        y = ALTURA - MARGEM - AB + (AB - texto.get_height()) // 2
        self.display.blit(texto, [x, y])

        texto = self.fonte.render("Tank", True, CORES.verde)
        x = LARGURA - MARGEM - LB + (LB - texto.get_width()) // 2
        y = ALTURA - MARGEM - AB + (AB - texto.get_height()) // 2
        self.display.blit(texto, [x, y])

        pygame.display.update()
