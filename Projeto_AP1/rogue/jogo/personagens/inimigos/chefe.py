import random

from .inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(15, 30)
        self.vida = random.randint(70, 140)
        self.defesa = random.randint(1, 6)
        self.nome = "Chefe"
        self.xp = 5

    def defender(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano
