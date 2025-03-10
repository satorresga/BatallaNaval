class Nave:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.posiciones = []
        self.hundida = False

    def recibir_impacto(self, posicion):
        if posicion in self.posiciones:
            self.posiciones.remove(posicion)
            if not self.posiciones:
                self.hundida = True
            return True
        return False