from .tablero import Tablero

class Juego:
    """
    Clase principal que controla la lógica del juego de batalla naval.
    Maneja las interacciones entre el usuario y el tablero.
    """

    def __init__(self, ancho, alto, gestor_usuarios, usuario_actual):
        """
        Inicializa un nuevo juego.

        Args:
            ancho (int): Ancho del tablero
            alto (int): Alto del tablero
            gestor_usuarios (GestionUsuariosORM): Instancia del gestor de usuarios
            usuario_actual (str): Nombre del usuario que juega
        """
        self.tablero = Tablero(ancho, alto)
        self.gestor_usuarios = gestor_usuarios
        self.usuario_actual = usuario_actual
        self.tablero.colocar_naves()

    def disparar(self, fila, columna):
        """
        Realiza un disparo en las coordenadas especificadas.

        Args:
            fila (int): Fila del disparo
            columna (int): Columna del disparo

        Returns:
            str: Resultado del disparo
        """
        resultado = self.tablero.disparar(fila, columna)
        if resultado in ["Impacto confirmado.", "¡Nave hundida!"]:
            self.gestor_usuarios.sumar_puntaje(self.usuario_actual, 10)
        return resultado

    def verificar_estado(self):
        """
        Verifica el estado actual del juego.

        Returns:
            str: Mensaje indicando si el juego ha terminado o no
        """
        return self.tablero.estado_del_juego()

    def obtener_tablero(self):
        """
        Devuelve la representación del tablero para mostrar en la web.

        Returns:
            list[list[str]]: Estado del tablero como lista de listas.
        """
        return self.tablero.representacion()