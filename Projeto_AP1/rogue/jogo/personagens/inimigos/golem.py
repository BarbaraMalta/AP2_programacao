import random

from .inimigo import Inimigo

class Golem(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(10, 25)
        self.vida = random.randint(40, 120)
        self.nome = "Golem"
        self.xp = 3
