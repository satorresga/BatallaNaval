class Puntuaciones:
    """
    Clase para gestionar y mostrar las puntuaciones de los jugadores.
    """
    
    def __init__(self):
        """Inicializa el sistema de puntuaciones."""
        self.puntuaciones = {}

    def registrar_puntaje(self, usuario, puntaje):
        """
        Registra o actualiza el puntaje de un usuario.
        
        Args:
            usuario (str): Nombre de usuario
            puntaje (int): Puntos a registrar
        """
        if usuario in self.puntuaciones:
            self.puntuaciones[usuario] += puntaje
        else:
            self.puntuaciones[usuario] = puntaje

    def obtener_puntuaciones(self):
        """
        Obtiene todas las puntuaciones ordenadas.
        
        Returns:
            list: Lista de tuplas (usuario, puntaje) ordenadas por puntaje descendente
        """
        return sorted(self.puntuaciones.items(), key=lambda item: item[1], reverse=True)

    def mostrar_tabla_puntuaciones(self):
        """Muestra por consola la tabla de puntuaciones ordenada."""
        print("Tabla de puntuaciones:")
        for idx, (usuario, puntaje) in enumerate(self.obtener_puntuaciones(), 1):
            print(f"{idx}. {usuario}: {puntaje} puntos")