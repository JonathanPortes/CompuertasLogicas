from puerta import Puerta

class PuertaNOT(Puerta):
    def calcular_salida(self):
        if len(self.entradas) != 1:
            raise ValueError("La compuerta NOT requiere exactamente 1 entrada")
        return 1 if not self.entradas[0] else 0
