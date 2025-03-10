import pytest, sys, os
from random import randint

sys.path.append(os.path.abspath('..'))

from proyecto_batalla_naval.juego.juego import Juego

# 🚀 Pruebas normales (100 disparos aleatorios)
@pytest.mark.parametrize("fila,columna", [(randint(0,9), randint(0,9)) for _ in range(100)])
def test_disparos(fila, columna):
    juego = Juego(10, 10)
    resultado = juego.disparar(fila, columna)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua.", "Posición fuera del tablero."]

# 🔥 Pruebas de estrés (1000 disparos en tablero grande)
@pytest.mark.parametrize("fila,columna", [(randint(0,49), randint(0,49)) for _ in range(1000)])
def test_disparos_masivos(fila, columna):
    juego = Juego(50, 50)
    resultado = juego.disparar(fila, columna)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua.", "Posición fuera del tablero."]

# ❌ Pruebas de errores (disparos fuera del tablero)
@pytest.mark.parametrize("fila,columna", [
    (-1, 0), (0, -1), (10, 10), (50, 50), (100, 0), (0, 100)
])
def test_disparos_fuera_limites(fila, columna):
    juego = Juego(10, 10)
    resultado = juego.disparar(fila, columna)
    assert resultado == "Posición fuera del tablero."

# 🔄 Pruebas con disparos repetidos
def test_disparos_repetidos():
    juego = Juego(10, 10)
    fila, columna = 2, 3
    resultado1 = juego.disparar(fila, columna)
    resultado2 = juego.disparar(fila, columna)
    assert resultado1 in ["Impacto confirmado.", "¡Nave hundida!", "Agua."]
    assert resultado2 == "Agua."

# 📏 Pruebas con tableros extremos
@pytest.mark.parametrize("ancho,alto", [(1, 1), (100, 100)])
def test_tamanos_extremos(ancho, alto):
    juego = Juego(ancho, alto)
    assert len(juego.tablero.matriz) == alto
    assert len(juego.tablero.matriz[0]) == ancho
