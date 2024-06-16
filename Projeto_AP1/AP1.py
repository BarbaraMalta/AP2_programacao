import random


def aventureiro_andar(aventureiro, direcao):
        movimento = direcao.upper()
        if movimento == "W" and aventureiro["posicao"][1] > 0:
            aventureiro["posicao"][1] -= 1
            return True
        elif movimento == "A" and aventureiro["posicao"][0] > 0:
            aventureiro["posicao"][0] -= 1
            return True
        elif movimento == "S" and aventureiro["posicao"][1] < 9:
            aventureiro["posicao"][1] += 1
            return True
        elif movimento == "D" and aventureiro["posicao"][0] < 9:
            aventureiro["posicao"][0] += 1
            return True
        return False

def aventureiro_atacar(aventureiro):
        return aventureiro["forca"] + random.randint(1, 6)

def aventureiro_defender(aventureiro, dano):
        dano_recebido = max(dano - aventureiro["defesa"], 0)
        aventureiro["vida"] -= dano_recebido
        aventureiro["vida"] = max(aventureiro["vida"], 0)



def ver_atributos_aventureiro(aventureiro):
        print(f"Atributos do {aventureiro['nome']}:")
        print(f"Força: {aventureiro['forca']}")
        print(f"Defesa: {aventureiro['defesa']}")
        print(f"Vida: {aventureiro['vida']}")

def aventureiro_esta_vivo(aventureiro):
        return aventureiro["vida"] > 0

  
def novo_monstro():
        print("Um novo monstro apareceu!")
        return {
            "forca": random.randint(5, 25),
            "vida": random.randint(10, 100)
        }

def monstro_atacar(monstro):
    return random.randint(5, 25)

def monstro_defender(monstro, dano):
    monstro["vida"] -= dano


def monstro_esta_vivo(monstro):
        return monstro["vida"] > 0

  
def desenhar(aventureiro, tesouro):
        for y in range(10):
            for x in range(10):
                if [x, y] == aventureiro["posicao"]:
                    print("@", end=" ")
                elif [x, y] == tesouro:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()

  
def iniciar_combate(aventureiro, monstro):
        while True:
            dano_aventureiro = aventureiro_atacar(aventureiro)
            monstro_defender(monstro, dano_aventureiro)
            print(f"Você causou {dano_aventureiro} de dano ao monstro!")
            print(f"Vida atual do monstro: {monstro['vida']}")
            if not monstro_esta_vivo(monstro):
                print("Você derrotou o monstro!")
                return True

            dano_monstro = monstro_atacar(monstro)
            aventureiro_defender(aventureiro, dano_monstro)
            print(f"O monstro causou {dano_monstro} de dano a você!")
            print(f"Sua vida atual: {aventureiro['vida']}")
            if not aventureiro_esta_vivo(aventureiro):
                print("Você foi derrotado pelo monstro...")
                return False

   
def movimentar(aventureiro, direcao):
        if not aventureiro_andar(aventureiro, direcao):
            return True

        efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
        if efeito == "monstro":
            monstro = novo_monstro()
            return iniciar_combate(aventureiro, monstro)

        return True

def gerar_tesouro():
        tesouro = [random.randint(1, 9), random.randint(1, 9)]
        while tesouro == [0, 0]:
            tesouro = [random.randint(1, 9), random.randint(1, 9)]
        return tesouro

def main():
        aventureiro = {
            "forca": random.randint(10, 18),
            "defesa": random.randint(10, 18),
            "vida": random.randint(100, 120),
            "posicao": [0, 0]
        }

        tesouro = gerar_tesouro()

        aventureiro["nome"] = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
        print(f"Saudações, {aventureiro['nome']}! Boa sorte!")

        desenhar(aventureiro, tesouro)

        while True:
            op = input("Insira o seu comando: ").upper()
            if op == "Q":
                print("Já correndo?")
                break
            elif op == "T":
                ver_atributos_aventureiro(aventureiro)
            elif op in ["W", "A", "S", "D"]:
                if movimentar(aventureiro, op):
                    desenhar(aventureiro, tesouro)
                else:
                    print("Game Over...")
                    break
            else:
                print(f"{aventureiro['nome']}, não conheço essa opção! Tente novamente!")

            if aventureiro["posicao"] == tesouro:
                print(f"Parabéns, {aventureiro['nome']}! Você encontrou o tesouro!")
                break

if __name__ == "__main__":
        main()