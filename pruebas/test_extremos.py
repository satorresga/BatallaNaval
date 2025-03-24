import pytest
from random import randint
from proyecto_batalla_naval.autenticacion.gestion_usuarios import GestionUsuarios
from proyecto_batalla_naval.juego.juego import Juego
import time

# Reiniciar usuarios antes de cada prueba extrema
def setup_function():
    GestionUsuarios.usuarios.clear()

# 📏 Tablero mínimo (1x1)
def test_tablero_minimo():
    GestionUsuarios.crear_usuario("min", "1")
    GestionUsuarios.usuario_actual = "min"
    juego = Juego(1, 1, GestionUsuarios)
    resultado = juego.disparar(0, 0)
    assert resultado in ["Agua.", "Impacto confirmado.", "¡Nave hundida!"]

# 📏 Tablero gigante (1000x1000)
def test_tablero_gigante():
    GestionUsuarios.crear_usuario("max", "1000")
    GestionUsuarios.usuario_actual = "max"
    juego = Juego(1000, 1000, GestionUsuarios)
    resultado = juego.disparar(999, 999)
    assert resultado in ["Agua.", "Impacto confirmado.", "¡Nave hundida!"]

# 🔄 Prueba con 1000 disparos aleatorios en tablero grande
def test_disparos_masivos():
    GestionUsuarios.crear_usuario("masivo", "123")
    GestionUsuarios.usuario_actual = "masivo"
    juego = Juego(50, 50, GestionUsuarios)
    for _ in range(1000):
        fila = randint(0, 49)
        columna = randint(0, 49)
        resultado = juego.disparar(fila, columna)
        assert resultado in ["Agua.", "Impacto confirmado.", "¡Nave hundida!", "Posición fuera del tablero."]

# ⚡ Prueba de rendimiento (máximo 1 segundo)
def test_rendimiento_100_disparos():
    GestionUsuarios.crear_usuario("fast", "go")
    GestionUsuarios.usuario_actual = "fast"
    juego = Juego(20, 20, GestionUsuarios)
    disparos = [(randint(0, 19), randint(0, 19)) for _ in range(100)]

    start = time.time()
    for fila, col in disparos:
        juego.disparar(fila, col)
    end = time.time()

    assert (end - start) < 1.0
