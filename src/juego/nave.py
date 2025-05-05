class Nave:
    """
    Clase que representa una nave en el juego de batalla naval.
    """
    
    def __init__(self, tamaño):
        """
        Inicializa una nueva nave.
        
        Args:
            tamaño (int): Tamaño de la nave (número de casillas que ocupa)
        """
        self.tamaño = tamaño
        self.posiciones = []
        self.hundida = False

    def recibir_impacto(self, posicion):
        """
        Registra un impacto en la nave.
        
        Args:
            posicion (tuple): Coordenadas (fila, columna) del impacto
            
        Returns:
            bool: True si el impacto fue en una posición válida, False en caso contrario
        """
        if posicion in self.posiciones:
            self.posiciones.remove(posicion)
            if not self.posiciones:
                self.hundida = True
            return True
        return False