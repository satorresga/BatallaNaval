import pytest
from src.juego.nave import Nave

class TestNave:
    @pytest.mark.parametrize("size", [1, 2, 3])
    def test_creacion_nave(self, size):
        nave = Nave(size)
        assert nave.tamaño == size
        assert not nave.hundida
        assert nave.posiciones == []
        
    def test_recibir_impacto_valido(self):
        nave = Nave(2)
        nave.posiciones = [(0,0), (0,1)]
        assert nave.recibir_impacto((0,0)) is True
        assert not nave.hundida
        assert nave.posiciones == [(0,1)]
        
    def test_recibir_impacto_hundir(self):
        nave = Nave(1)
        nave.posiciones = [(0,0)]
        assert nave.recibir_impacto((0,0)) is True
        assert nave.hundida
        assert nave.posiciones == []
        
    def test_recibir_impacto_invalido(self):
        nave = Nave(2)
        nave.posiciones = [(0,0), (0,1)]
        assert nave.recibir_impacto((1,1)) is False
        assert not nave.hundida
        assert nave.posiciones == [(0,0), (0,1)]