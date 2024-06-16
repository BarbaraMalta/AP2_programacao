import random

from .aventureiro import Aventureiro

class Guerreiro(Aventureiro):
    def __init__(self, nome, i):
        super().__init__(nome, i)
        self.vida = random.randint(90, 110)
        self.defesa = random.randint(9, 17)
        self.forca = random.randint(15, 25)
        self.vida_max = self.vida
