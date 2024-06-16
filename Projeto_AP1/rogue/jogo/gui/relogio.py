import time

class Relogio:
    def iniciar(self):
        self.inicio = time.time()

    def medir_tempo(self):
        tempo_decorrido = time.time() - self.inicio
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido - minutos * 60)
        return f"{str(minutos).rjust(2, '0')}:{str(segundos).rjust(2, '0')}"

relogio = Relogio()


relogio = Relogio()
relogio.iniciar()

# Simula a passagem de tempo
time.sleep(5)

print(relogio.medir_tempo())