class Puntuaciones:
    def __init__(self):
        self.puntuaciones = {}

    def registrar_puntaje(self, usuario, puntaje):
        if usuario in self.puntuaciones:
            self.puntuaciones[usuario] += puntaje
        else:
            self.puntuaciones[usuario] = puntaje

    def obtener_puntuaciones(self):
        return sorted(self.puntuaciones.items(), key=lambda item: item[1], reverse=True)

    def mostrar_tabla_puntuaciones(self):
        tabla = "Tabla de puntuaciones:\n"
        for idx, (usuario, puntaje) in enumerate(self.obtener_puntuaciones(), 1):
            tabla = f"{idx + 1}. {usuario}: {puntaje} puntos"
            print(tabla)