import random
from ...mecanicas import som

XP_POR_NIVEL = 5

class Aventureiro:
    def _init_(self, nome, i):
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida_max = random.randint(100, 120)
        self.vida = self.vida_max
        self.posicao = [0, 0]
        if i == 1:
            self.posicao = [9, 9]

        self.char = ["@", "#"][i]
        self.nome = nome

        self.nivel = 1
        self.xp = 0

        self.turnos_veneno = 0

        self.primeiro_movimento = True
        self.status = f"Comece a explorar"
        self.fim_jogo = None

    def exportar(self):
        return {
            "forca": self.forca,
            "defesa": self.defesa,
            "vida_max": self.vida_max,
            "vida": self.vida,
            "posicao": self.posicao,
            "char": self.char,
            "nome": self.nome,
            "nivel": self.nivel,
            "xp": self.xp,
            "turnos_veneno": self.turnos_veneno,
            "primeiro_movimento": self.primeiro_movimento,
            "status": self.status,
            "fim_jogo": self.fim_jogo,
            "classe": self._class.name_
        }

    def importar(self, dados):
        self.forca = dados["forca"]
        self.defesa = dados["defesa"]
        self.vida_max = dados["vida_max"]
        self.vida = dados["vida"]
        self.posicao = dados["posicao"]

        self.char = dados["char"]
        self.nome = dados["nome"]

        self.nivel = dados["nivel"]
        self.xp = dados["xp"]

        self.turnos_veneno = dados["turnos_veneno"]

        self.primeiro_movimento = dados["primeiro_movimento"]
        self.status = dados["status"]
        self.fim_jogo = dados["fim_jogo"]

    def iniciar_veneno(self):
        if self.turnos_veneno == 0:
            self.turnos_veneno = random.randint(2, 10)

    def causar_dano_veneno(self):
        if self.turnos_veneno > 0:
            dano = random.randint(5, 10)
            self.defender(dano, usar_defesa=False)
            self.turnos_veneno -= 1
            self.status = f"{self.nome} tomou {dano} de dano de veneno! Turnos restantes: {self.turnos_veneno}"

    def ganhar_xp(self, xp_ganha):
        self.xp += xp_ganha
        if self.xp >= XP_POR_NIVEL * self.nivel:
            self.xp -= XP_POR_NIVEL * self.nivel
            self.ganhar_nivel()

    def ganhar_nivel(self):
        self.nivel += 1
        self.vida_max += 10
        self.vida = self.vida_max
        self.forca += 2
        self.defesa += 2
        print(f"{self.nome} ganhou um nível!")
        som.levelup()

    def calcular_pos_futura(self, direcao):
        x, y = self.posicao
        match direcao:
            case "A":
                x -= 1
            case "W":
                y -= 1
            case "S":
                y += 1
            case "D":
                x += 1

        return [x, y]

    def andar(self, pos_futura, pocao):
        self.posicao = pos_futura
        self.verificar_pocao(pocao)

    def verificar_pocao(self, pocao):
        for p in pocao:
            if self.posicao == p.posicao:
                self.vida = min(self.vida + p.vida, self.vida_max)
                pocao.remove(p)
                self.status = f"{self.nome} encontrou uma poção e recuperou {p.vida} de vida!"

    def atacar(self):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return self.forca + random.randint(1, 6)

    def defender(self, dano, usar_defesa=True):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        if usar_defesa:
            dano -= self.defesa
        if dano > 0:
            self.vida -= dano

    def esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0

    def _str_(self):
        return f"""Aventureiro {self.nome}:
Força:  {self.forca}
Defesa: {self.defesa}
Vida:   {self.vida}
"""
