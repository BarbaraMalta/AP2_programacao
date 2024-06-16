import random

from .inimigo import Inimigo

class Esqueleto(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(10, 30)
        self.vida = random.randint(30, 80)
        self.nome = "Esqueleto"
        self.xp = 2
