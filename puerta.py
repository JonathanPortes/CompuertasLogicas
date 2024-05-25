class Puerta:
    def __init__(self, entradas):
        self.entradas = entradas

    def calcular_salida(self):
        raise NotImplementedError("La subclase debe implementar el método abstracto")
