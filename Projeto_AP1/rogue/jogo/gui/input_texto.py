from .cores import CORES

import pygame

FONTE_TAMANHO = 25
MARGEM = 10
FONTE = "Lucida Console"
LARGURA = 650
ALTURA = 100
RECT_ALTURA = FONTE_TAMANHO + 2 * MARGEM
RECT_LARGURA = LARGURA - 2 * MARGEM
ESPESSURA_INPUTBOX = 2

class InputBox:
    def __init__(self, mensagem):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        self.fonte = pygame.font.SysFont(FONTE, FONTE_TAMANHO)
        self.rect = pygame.Rect(
            MARGEM,
            ALTURA - MARGEM - RECT_ALTURA,
            RECT_LARGURA,
            RECT_ALTURA
        )
        self.prompt = mensagem
        self.texto = ""

    def tratar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return self.texto
            elif evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            else:
                if len(self.texto) < 20:
                    self.texto += evento.unicode

        return None

    def renderizar(self):
        self.display.fill(CORES.preto)
        texto_prompt = self.fonte.render(self.prompt, True, CORES.branco)
        texto_input = self.fonte.render(self.texto, True, CORES.branco)

        pygame.draw.rect(self.display, CORES.branco, self.rect, ESPESSURA_INPUTBOX)
        self.display.blit(texto_prompt, [MARGEM, MARGEM])
        self.display.blit(
            texto_input,
            [MARGEM * 2, ALTURA - MARGEM * 2 - texto_input.get_height()]
        )

        pygame.display.update()

