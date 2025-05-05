import pytest
from src.autenticacion.gestion_usuarios import GestionUsuarios
from src.juego.juego import Juego

class TestJuego:
    @pytest.fixture(autouse=True)
    def setup(self):
        GestionUsuarios.usuarios.clear()
        GestionUsuarios.crear_usuario("player", "pass")
        self.juego = Juego(5, 5, GestionUsuarios, "player")
    
    @pytest.mark.parametrize("fila,columna", [
        (-1, 0), (0, -1), (5, 0), (0, 5),
        (100, 100), (-10, -10)
    ])
    def test_disparo_fuera_limites(self, fila, columna):
        assert self.juego.disparar(fila, columna) == "Posición fuera del tablero."
        
    def test_disparo_en_agua(self):
        # Buscar una celda sin nave
        for fila in range(5):
            for col in range(5):
                resultado = self.juego.disparar(fila, col)
                if resultado == "Agua.":
                    assert resultado == "Agua."
                    return
        pytest.fail("No se encontró ninguna celda con agua.")
        
    def test_disparo_impacto_nave(self):
        # Encontrar una nave
        for fila in range(5):
            for col in range(5):
                res = self.juego.disparar(fila, col)
                if res != "Agua.":
                    assert res in ["Impacto confirmado.", "¡Nave hundida!"]
                    return
        pytest.fail("No se encontró ninguna nave")
        
    def test_disparo_hundir_nave(self):
        for fila in range(5):
            for col in range(5):
                res = self.juego.disparar(fila, col)
                if res == "¡Nave hundida!":
                    assert True
                    return
        pytest.fail("No se hundió ninguna nave completa")
         
    
    def test_estado_juego_incompleto(self):
        assert self.juego.verificar_estado() == "Aún hay naves en el agua."
        
    def test_estado_juego_completo(self):
        # Hundir todas las naves
        for fila in range(5):
            for col in range(5):
                self.juego.disparar(fila, col)
        assert self.juego.verificar_estado() == "¡Todas las naves hundidas! Juego terminado."
    
    def test_puntaje_impacto(self):
        initial_score = GestionUsuarios.obtener_puntaje("player")
        # Encontrar un impacto
        for fila in range(5):
            for col in range(5):
                if self.juego.disparar(fila, col) != "Agua.":
                    assert GestionUsuarios.obtener_puntaje("player") == initial_score + 10
                    return
        pytest.fail("No se encontró impacto para probar puntaje")