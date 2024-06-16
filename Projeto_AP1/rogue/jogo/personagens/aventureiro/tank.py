import random

from .aventureiro import Aventureiro

class Tank(Aventureiro):
    def __init__(self, nome, i):
        super().__init__(nome, i)
        self.vida = random.randint(130, 160)
        self.defesa = random.randint(15, 25)
        self.forca = random.randint(6, 15)
        self.vida_max = self.vida
