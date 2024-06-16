import time

from jogo.mecanicas import loop
from jogo.gui.relogio import relogio

import pygame

def iniciar():
    pygame.init()
    relogio.iniciar()

def encerrar():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar()
    loop.executar()
    time.sleep(2)
    encerrar()

if __name__ == "__main__":
    main()
