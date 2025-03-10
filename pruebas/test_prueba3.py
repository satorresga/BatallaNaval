import pytest, sys, os
from random import randint, choice
from time import time  # Para medir el rendimiento

sys.path.append(os.path.abspath('..'))

from proyecto_batalla_naval.juego.juego import Juego

# 🚀 Pruebas normales (500 disparos aleatorios en tablero 10x10)
@pytest.mark.parametrize("fila,columna", [(randint(0,9), randint(0,9)) for _ in range(500)])
def test_disparos(fila, columna):
    juego = Juego(10, 10)
    resultado = juego.disparar(fila, columna)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua.", "Posición fuera del tablero."]

# 🔥 Pruebas de estrés (10,000 disparos en tablero grande 100x100)
@pytest.mark.parametrize("fila,columna", [(randint(0,99), randint(0,99)) for _ in range(10000)])
def test_disparos_masivos(fila, columna):
    juego = Juego(100, 100)
    resultado = juego.disparar(fila, columna)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua.", "Posición fuera del tablero."]

# ❌ Pruebas de errores (disparos fuera del tablero, valores absurdos)
@pytest.mark.parametrize("fila,columna", [
    (-10, 0), (0, -10), (100, 100), (500, 500), (1000, 0), (0, 1000), (-999, -999)
])
def test_disparos_fuera_limites(fila, columna):
    juego = Juego(50, 50)
    resultado = juego.disparar(fila, columna)
    assert resultado == "Posición fuera del tablero."

# 🔄 Pruebas con disparos repetidos en la misma celda con nave
def test_disparos_repetidos_sobre_nave():
    juego = Juego(10, 10)
    fila, columna = 5, 5

    # ✅ Crear una nave en esa posición y agregarla al juego
    nave = juego.tablero.naves[0]  # Tomamos la primera nave del tablero
    nave.posiciones = [(fila, columna)]  # La colocamos en (5,5)

    resultado1 = juego.disparar(fila, columna)  # Primer disparo
    resultado2 = juego.disparar(fila, columna)  # Segundo disparo en el mismo lugar

    assert resultado1 in ["Impacto confirmado.", "¡Nave hundida!"]
    assert resultado2 == "Agua."  # Un disparo repetido en el mismo lugar debe ser "Agua."

# 🔄 Pruebas con disparos en secuencia sobre el mismo juego
def test_disparos_secuencia():
    juego = Juego(10, 10)
    disparos = [(randint(0, 9), randint(0, 9)) for _ in range(20)]
    
    for fila, columna in disparos:
        resultado = juego.disparar(fila, columna)
        assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua."]

# 📏 Pruebas con tableros extremos (1x1, 2x2, 100x1000, 1000x1000)
@pytest.mark.parametrize("ancho,alto", [(1, 1), (2, 2), (100, 1000), (1000, 1000)])
def test_tamanos_extremos(ancho, alto):
    juego = Juego(ancho, alto)
    assert len(juego.tablero.matriz) == alto
    assert len(juego.tablero.matriz[0]) == ancho

# ⚡ Prueba de velocidad en 100 disparos
def test_rendimiento_disparos():
    juego = Juego(20, 20)
    disparos = [(randint(0, 19), randint(0, 19)) for _ in range(100)]
    
    start_time = time()
    for fila, columna in disparos:
        juego.disparar(fila, columna)
    end_time = time()

    tiempo_total = end_time - start_time
    print(f"\nTiempo total de 100 disparos: {tiempo_total:.4f} segundos")
    assert tiempo_total < 1.0  # Debe ejecutarse en menos de 1 segundo
