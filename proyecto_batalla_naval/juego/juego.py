from .tablero import Tablero

class Juego:
    def __init__(self, ancho, alto, usuario):
        self.tablero = Tablero(ancho, alto)
        self.usuario = usuario  # Relación agregada
        self.tablero.colocar_naves()

    def disparar(self, fila, columna):
        resultado = self.tablero.disparar(fila, columna)
        if resultado in ["Impacto confirmado.", "¡Nave hundida!"]:
            self.usuario.sumar_puntaje(self.usuario.usuario_actual, 10)

        return resultado

    def verificar_estado(self):
        return self.tablero.estado_del_juego()