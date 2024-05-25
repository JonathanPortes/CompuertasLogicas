from puerta import Puerta

class PuertaOR(Puerta):
    def calcular_salida(self):
        if any(self.entradas):
            return 1
        else:
            return 0
