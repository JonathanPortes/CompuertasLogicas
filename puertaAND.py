from puerta import Puerta

class PuertaAND(Puerta):
    def calcular_salida(self):
        if all(self.entradas):
            return 1
        else:
            return 0
