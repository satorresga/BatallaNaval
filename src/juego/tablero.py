from random import randint
from .nave import Nave

class Tablero:
    """
    Clase que representa el tablero de juego, con métodos para colocar naves y realizar disparos.
    """
    
    def __init__(self, ancho, alto):
        """
        Inicializa un nuevo tablero.
        
        Args:
            ancho (int): Ancho del tablero
            alto (int): Alto del tablero
        """
        self.ancho = ancho
        self.alto = alto
        self.matriz = [['~' for _ in range(ancho)] for _ in range(alto)]
        self.naves = []

    def colocar_naves(self, num_naves=3):
        """
        Coloca naves aleatoriamente en el tablero.
        
        Args:
            num_naves (int): Número de naves a colocar (default: 3)
            
        Raises:
            Exception: Si el tablero es demasiado pequeño para colocar las naves
        """
        espacio_total = self.ancho * self.alto
        if num_naves > espacio_total:
            raise Exception("No se pudieron colocar todas las naves, tablero muy pequeño.")

        for _ in range(num_naves):
            tamaño = min(randint(1, 3), self.alto)
            nave = Nave(tamaño)
            posiciones = []
            intentos = 0
            max_intentos = 100

            while not posiciones and intentos < max_intentos:
                intentos += 1
                fila = randint(0, self.alto - 1)
                columna = randint(0, self.ancho - 1)
                direccion = randint(0, 1)  # 0: vertical, 1: horizontal

                posiciones_nave = []
                if direccion == 0:  # Vertical
                    if fila + tamaño <= self.alto:
                        posiciones_nave = [(fila + i, columna) for i in range(tamaño)]
                else:  # Horizontal
                    if columna + tamaño <= self.ancho:
                        posiciones_nave = [(fila, columna + i) for i in range(tamaño)]

                if posiciones_nave and all(self.matriz[f][c] == '~' for f, c in posiciones_nave):
                    posiciones = posiciones_nave
                    nave.posiciones = posiciones
                    for f, c in posiciones:
                        self.matriz[f][c] = 'N'

            if intentos >= max_intentos:
                continue  # Saltar esta nave si no se pudo colocar

            self.naves.append(nave)

    def disparar(self, fila, columna):
        """
        Realiza un disparo en las coordenadas especificadas.
        
        Args:
            fila (int): Fila del disparo
            columna (int): Columna del disparo
            
        Returns:
            str: Resultado del disparo ("Impacto confirmado", "¡Nave hundida!", "Agua", etc.)
        """
        if fila < 0 or columna < 0 or fila >= self.alto or columna >= self.ancho:
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
        """
        Verifica el estado del juego.
        
        Returns:
            str: Mensaje indicando si todas las naves han sido hundidas
        """
        if all(nave.hundida for nave in self.naves):
            return "¡Todas las naves hundidas! Juego terminado."
        return "Aún hay naves en el agua."