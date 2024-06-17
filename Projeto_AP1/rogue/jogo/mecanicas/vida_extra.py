class vida_extra:
    def desenhar_simbolo(self):
        return "$"
    
    def __init__(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0) and not (x == y == 9):
                break

        self.posicao = [x, y]
        self.visível = True
        
    def vida_extra(self, aventureiro):
        if aventureiro["posicao"] == vida_extra:
        aventureiro["vidas_extras"] += 1
        vida_extra.clear()
        print("Você ganhou uma vida extra!")

        self.visível = False    
