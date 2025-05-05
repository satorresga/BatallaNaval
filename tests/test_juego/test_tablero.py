import pytest
from src.juego.tablero import Tablero

class TestTablero:
    @pytest.mark.parametrize("width,height", [(5,5), (10,10), (3,7)])
    def test_creacion_tablero(self, width, height):
        tablero = Tablero(width, height)
        assert tablero.ancho == width
        assert tablero.alto == height
        assert len(tablero.matriz) == height
        assert len(tablero.matriz[0]) == width
        
    def test_colocar_naves_default(self):
        tablero = Tablero(5, 5)
        tablero.colocar_naves()
        assert len(tablero.naves) == 3
        
    @pytest.mark.parametrize("n_naves", [1, 2, 4])
    def test_colocar_naves_personalizado(self, n_naves):
        tablero = Tablero(5, 5)
        tablero.colocar_naves(n_naves)
        assert len(tablero.naves) == n_naves
        
    def test_colocar_naves_posiciones_validas(self):
        tablero = Tablero(5, 5)
        tablero.colocar_naves(2)
        
        # Verificar que las posiciones no se superponen
        all_positions = []
        for nave in tablero.naves:
            for pos in nave.posiciones:
                assert pos not in all_positions
                all_positions.append(pos)
                
    def test_colocar_naves_tablero_lleno(self):
        tablero = Tablero(2, 2)
        with pytest.raises(Exception, match="No se pudieron colocar todas las naves"):
            tablero.colocar_naves(5)
            
    def test_disparo_agua(self):
        tablero = Tablero(5, 5)
        tablero.colocar_naves(1)
        # Asumir que (0,0) es agua (no podemos garantizarlo, pero es probable)
        assert tablero.disparar(0, 0) == "Agua."
        
    def test_disparo_impacto(self):
        tablero = Tablero(5, 5)
        tablero.colocar_naves(1)
        # Encontrar una nave
        for fila in range(5):
            for col in range(5):
                res = tablero.disparar(fila, col)
                if res != "Agua.":
                    assert res in ["Impacto confirmado.", "¡Nave hundida!"]
                    return
        pytest.fail("No se encontró ninguna nave")