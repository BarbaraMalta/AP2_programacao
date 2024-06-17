from .cores import CORES
from .relogio import Relogio
from ..mecanicas import pocao

import pygame

GRID = 40
TAM_MAPA = 10
LARGURA = GRID * TAM_MAPA + 400
ALTURA = GRID * TAM_MAPA + 150
MARGEM = 10
FONTE = "Lucida Console"

def centralizar_grid(posicao, texto):
    x = posicao[0] * GRID + (GRID - texto.get_width()) // 2
    y = posicao[1] * GRID + (GRID - texto.get_height()) // 2
    return [x + (LARGURA - GRID * TAM_MAPA) // 2, y + (ALTURA - GRID * TAM_MAPA) // 2]

class Tela:
    def _init_(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiros, tesouro, obstaculos, id_jogador, pocao):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiros)
        self.tesouro(tesouro)
        self.mapa(aventureiros, tesouro, obstaculos, pocao)
        self.combate(aventureiros[1 - id_jogador].status)
        self.obstaculos(obstaculos)
        self.turno(id_jogador)
        self.relogio()

        for aventureiro in aventureiros:
            if aventureiro.fim_jogo is not None:
                self.fim_jogo(aventureiro.fim_jogo)

        pygame.display.update()

    def turno(self, id_jogador):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(f"Turno do jog. {id_jogador + 1}", True, CORES.branco)
        self.display.blit(texto, [LARGURA - MARGEM - texto.get_width(), MARGEM * 2 + texto.get_height()])

    def fim_jogo(self, fim_jogo):
        fonte = pygame.font.SysFont(FONTE, GRID * 2)
        mensagem = "Derrota"
        if fim_jogo:
            mensagem = "Vitória"
        texto = fonte.render(mensagem, True, CORES.vermelho, CORES.branco)
        self.display.blit(
            texto,
            [(LARGURA - texto.get_width()) // 2, (ALTURA - texto.get_height()) // 2]
        )

    def relogio(self):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(Relogio.medir_tempo(), True, CORES.branco)
        self.display.blit(texto, [LARGURA - MARGEM - texto.get_width(), MARGEM])

    def combate(self, mensagem):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(mensagem, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def escreve_grid(self, mensagem, posicao):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render(mensagem, True, CORES.branco)
        self.display.blit(texto, centralizar_grid(posicao, texto))

    def obstaculos(self, obstaculos):
        for obstaculo in obstaculos:
            self.escreve_grid("O", obstaculo.posicao)

    def pocao(self, pocao):
        for p in pocao:
            self.escreve_grid("%", p.posicao)

    def aventureiro(self, aventureiros):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        for i, aventureiro in enumerate(aventureiros):
            self.escreve_grid(aventureiro.char, aventureiro.posicao)

            atributos = f"{aventureiro.nome} " \
                        f"nv {aventureiro.nivel} " \
                        f"({aventureiro.experiencia}/{aventureiro.experiencia_necessaria}) " \
                        f"- Vida {aventureiro.vida}/{aventureiro.vida_max} " \
                        f"- Força {aventureiro.forca} " \
                        f"- Defesa {aventureiro.defesa}"
            texto = fonte.render(atributos, True, CORES.branco)
            x = (LARGURA - texto.get_width()) // 2
            y = ALTURA - MARGEM * (2 - i) - texto.get_height() * (2 - i)
            self.display.blit(texto, [x, y])

    def tesouro(self, tesouro):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render("X", True, CORES.vermelho)
        self.display.blit(texto, centralizar_grid(tesouro.posicao, texto))

    def mapa(self, aventureiros, tesouro, obstaculos, pocao):
        for linha in range(10):
            for coluna in range(10):
                posicoes_invalidas = [aventureiros[0].posicao, aventureiros[1].posicao, tesouro.posicao]
                for obstaculo in obstaculos:
                    posicoes_invalidas.append(obstaculo.posicao)
                for p in pocao:
                    posicoes_invalidas.append(p.posicao)
                if [linha, coluna] not in posicoes_invalidas:
                    self.escreve_grid(".", [linha, coluna])
