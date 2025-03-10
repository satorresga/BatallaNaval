from random import randint
from .nave import Nave

class Tablero:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.matriz = [['~' for _ in range(ancho)] for _ in range(alto)]
        self.naves = []

    def colocar_naves(self, num_naves=3):
        intentos_maximos = 1000  # ✅ Evita el bucle infinito
        espacio_total = self.ancho * self.alto  # 🔍 Espacios disponibles en el tablero
        num_naves = min(num_naves, max(1, espacio_total // 2))  # 🔥 Ajusta el número de naves

        for _ in range(num_naves):
            nave = Nave(tamaño=min(randint(1, 3), self.alto))  # 🚀 Asegura que la nave quepa en el tablero
            posiciones = []
            intentos = 0  # Contador de intentos para evitar loops infinitos

            while not posiciones and intentos < intentos_maximos:
                intentos += 1  # 🚨 Incrementar el contador en cada intento
                fila = randint(0, len(self.matriz)-1)
                columna = randint(0, len(self.matriz[0])-1)

                posiciones_nave = [(f, columna) for f in range(fila, min(fila + nave.tamaño, len(self.matriz)))]

                posiciones_validas = all(self.matriz[f][columna] == '~' for f, columna in posiciones_nave)

                if posiciones_validas:
                    posiciones = posiciones_nave
                    nave.posiciones = posiciones
                    for f, c in posiciones:
                        self.matriz[f][c] = 'N'

            if intentos >= intentos_maximos:
                raise Exception("No se pudieron colocar todas las naves, tablero muy pequeño.")

            self.naves.append(nave)


    
    
    def disparar(self, fila, columna):
        if fila < 0 or columna < 0 or fila >= len(self.matriz) or columna >= len(self.matriz[0]):
            return "Posición fuera del tablero."

        for nave in self.naves:
            if (fila, columna) in nave.posiciones:
                nave.recibir_impacto((fila, columna))
                self.matriz[fila][columna] = 'X'
                if nave.hundida:
                    return "¡Nave hundida!"
                return "Impacto confirmado."

        return "Agua."
        
    
    def estado_del_juego(self):
        if all(nave.hundida for nave in self.naves):
            return "¡Todas las naves hundidas! Juego terminado."
        return "Aún hay naves en el agua."
