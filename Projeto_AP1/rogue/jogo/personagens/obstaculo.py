import random

class Obstaculo:
    def __init__(self, tesouro):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0) and not (x == y == 9) and [x, y] != tesouro.posicao:
                break

        self.posicao = [x, y]

class Obstaculos:
    def __init__(self, total_obstaculos, tesouro):
        self.obstaculos = []
        for _ in range(total_obstaculos):
            self.adicionar_obstaculo(tesouro)

    def adicionar_obstaculo(self, tesouro):
        while True:
            obs = Obstaculo(tesouro)
            if obs.posicao not in [obstaculo.posicao for obstaculo in self.obstaculos]:
                break

        self.obstaculos.append(obs)

    def verificar_posicao(self, pos_futura):
        """
        Retorna False caso tenha batido em um obstáculo, e True caso contrário.
        """
        for obstaculo in self.obstaculos:
            if pos_futura == obstaculo.posicao:
                return False

        if pos_futura[0] == -1 or pos_futura[0] == 10 or pos_futura[1] == -1 or pos_futura[1] == 10:
            return False

        return True
