import random

class Inimigo:
    def __init__(self):
        self.forca = random.randint(5, 25)
        self.vida = random.randint(10, 100)
        self.xp = 1
        self.nome = "Monstro"

    def atacar(self):
        """
        Retorna o dano do monstro, igual ao seu atributo de força.
        """
        return self.forca

    def defender(self, dano):
        """
        Reduz o dano causado da vida do monstro.
        """
        self.vida -= dano

    def esta_vivo(self):
        """
        Retorna True se a vida do monstro é maior que zero.
        """
        return self.vida > 0
