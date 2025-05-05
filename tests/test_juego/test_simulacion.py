import pytest
from src.autenticacion.gestion_usuarios import GestionUsuarios
from src.juego.juego import Juego
from random import randint

class TestSimulacionJuego:
    @pytest.fixture(autouse=True)
    def setup(self):
        GestionUsuarios.usuarios.clear()
        GestionUsuarios.crear_usuario("simuser", "clave")
        GestionUsuarios.usuario_actual = "simuser"
        self.juego = Juego(10, 10, GestionUsuarios, "simuser")

    def test_simulacion_partida_completa(self):
        for fila in range(10):
            for col in range(10):
                self.juego.disparar(fila, col)
        assert self.juego.verificar_estado() == "¡Todas las naves hundidas! Juego terminado."

    def test_simulacion_puntaje_total(self):
        impactos = 0
        for fila in range(10):
            for col in range(10):
                resultado = self.juego.disparar(fila, col)
                if resultado in ["Impacto confirmado.", "¡Nave hundida!"]:
                    impactos += 1
                if impactos >= 2:
                    break
            if impactos >= 2:
                break
        puntaje = GestionUsuarios.obtener_puntaje("simuser")
        assert puntaje >= 20

    def test_juego_no_suma_puntaje_doble(self):
        fila, col = 2, 2
        resultado1 = self.juego.disparar(fila, col)
        puntaje1 = GestionUsuarios.obtener_puntaje("simuser")
        resultado2 = self.juego.disparar(fila, col)
        puntaje2 = GestionUsuarios.obtener_puntaje("simuser")
        assert resultado2 == "Agua."
        assert puntaje2 == puntaje1

    def test_simulacion_varios_usuarios(self):
        GestionUsuarios.crear_usuario("otro", "123")
        juego2 = Juego(10, 10, GestionUsuarios, "otro")
        juego2.disparar(0, 0)
        GestionUsuarios.sumar_puntaje("otro", 5)
        assert GestionUsuarios.obtener_puntaje("simuser") >= 0
        assert GestionUsuarios.obtener_puntaje("otro") == 5

    @pytest.mark.parametrize("fila, columna", [(randint(0, 9), randint(0, 9)) for _ in range(100)])
    def test_100_disparos_simulados(self, fila, columna):
        resultado = self.juego.disparar(fila, columna)
        assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua.", "Posición fuera del tablero."]
