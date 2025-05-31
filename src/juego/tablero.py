import random

class Tablero:
    """
    Representa el tablero del juego de Batalla Naval.
    """

    def __init__(self, ancho, alto):
        """
        Inicializa el tablero con un ancho y alto definidos.

        :param ancho: Número de columnas del tablero.
        :param alto: Número de filas del tablero.
        """
        self.ancho = ancho
        self.alto = alto
        self.celdas = [[" " for _ in range(ancho)] for _ in range(alto)]
        self.naves = []
        self.colocar_naves()

    def colocar_naves(self, cantidad=3):
        """
        Coloca aleatoriamente una cantidad de naves en el tablero.
        """
        colocadas = 0
        while colocadas < cantidad:
            fila = random.randint(0, self.alto - 1)
            columna = random.randint(0, self.ancho - 1)
            if self.celdas[fila][columna] == " ":
                self.celdas[fila][columna] = "■"
                self.naves.append((fila, columna))
                colocadas += 1

    def disparar(self, fila, columna):
        """
        Procesa un disparo en una coordenada.

        :param fila: Fila del disparo.
        :param columna: Columna del disparo.
        :return: Resultado del disparo.
        """
        if self.celdas[fila][columna] == "■":
            self.celdas[fila][columna] = "X"
            self.naves.remove((fila, columna))
            if not self.naves:
                return "¡Nave hundida! - Has ganado."
            return "Impacto confirmado."
        elif self.celdas[fila][columna] == " ":
            self.celdas[fila][columna] = "O"
            return "Agua."
        else:
            return "Ya disparaste aquí."

    def estado_del_juego(self):
        """
        Verifica si aún quedan naves en el tablero.

        :return: Estado del juego.
        """
        if not self.naves:
            return "¡Has ganado!"
        return "El juego continúa"

    def representacion(self):
        """
        Devuelve una representación visual del tablero.

        :return: Lista de listas con símbolos.
        """
        grid = []
        for fila in self.celdas:
            fila_visual = []
            for celda in fila:
                if celda == "X":
                    fila_visual.append("💥")
                elif celda == "O":
                    fila_visual.append("🌊")
                else:
                    fila_visual.append("⬜")
            grid.append(fila_visual)
        return grid
