import random

class Armadilha:
    def __init__(self):
        self.efeito = random.choices(
            ["morte", "veneno", "vida", "força", "defesa"],
            [0.02, 0.2, 0.5, 0.125, 0.125]
        )[0]

    def aplicar_efeito(self, aventureiro):
        match self.efeito:
            case "morte":
                aventureiro.status = f"{aventureiro.nome} pisou numa armadilha e morreu..."
                aventureiro.fim_jogo = False
                aventureiro.defender(aventureiro.vida, usar_defesa=False)
            case "vida":
                dano = random.randint(5, 25)
                aventureiro.defender(dano, usar_defesa=False)
                aventureiro.status = f"{aventureiro.nome} pisou numa armadilha e levou {dano} de dano!"
            case "força":
                aventureiro.forca -= 1
                aventureiro.status = f"{aventureiro.nome} pisou numa armadilha e perdeu 1 de força!"
            case "defesa":
                aventureiro.defesa -= 1
                aventureiro.status = f"{aventureiro.nome} pisou numa armadilha e perdeu 1 de defesa!"
            case "veneno":
                aventureiro.iniciar_veneno()
                aventureiro.status = f"{aventureiro.nome} pisou numa armadilha e ficou envenenado!"
