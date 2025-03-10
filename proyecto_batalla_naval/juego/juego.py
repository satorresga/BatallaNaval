from .tablero import Tablero  


class Juego:
    def __init__(self, ancho, alto, colocar_naves_auto=True):
        self.tablero = Tablero(ancho, alto)
        if colocar_naves_auto:
            self.tablero.colocar_naves()

    def disparar(self, fila, columna):
        return self.tablero.disparar(fila, columna)

    def verificar_estado(self):
        return self.tablero.estado_del_juego()