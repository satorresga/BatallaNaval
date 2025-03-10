import pytest, sys, os
sys.path.append(os.path.abspath('..'))
from random import randint
from proyecto_batalla_naval.juego.juego import Juego

@pytest.mark.parametrize("fila,columna", [(randint(0,9), randint(0,9)) for _ in range(100)])
def test_disparos(fila, columna):
    juego = Juego(10, 10)
    resultado = juego.disparar(fila, columna)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua.", "Posición fuera del tablero."]
