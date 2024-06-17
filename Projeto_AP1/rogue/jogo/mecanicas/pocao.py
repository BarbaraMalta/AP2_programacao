import random

class pocao:
    def desenhar_simbolo(self):
        return "%"
    
    def __init__(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0) and not (x == y == 9):
                break

        self.posicao = [x, y]
        self.visível = True
        
    def aplicar_efeito(self, aventureiro):
        efeito = random.randint(1, 3)
        if efeito == 1:
            aventureiro['vida_max'] *= 2
            aventureiro['vida'] = aventureiro['vida_max']
        elif efeito == 2:
            aventureiro['força'] += 15
        elif efeito == 3:
            aventureiro['defesa'] += 10

        self.visível = False
        
pocao = pocao()
