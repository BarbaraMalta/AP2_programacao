import random

from .inimigo import Inimigo

class Aranha(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(5, 15)
        self.vida = random.randint(10, 50)
        self.nome = "Aranha"
