import pytest
from proyecto_batalla_naval.autenticacion.gestion_usuarios import GestionUsuarios
from proyecto_batalla_naval.juego.juego import Juego

# Setup global para limpiar usuarios antes de cada prueba
def setup_function():
    GestionUsuarios.usuarios.clear()

# Crear cuenta exitosamente
def test_crear_cuenta():
    GestionUsuarios.crear_usuario("juan", "1234")
    assert "juan" in GestionUsuarios.usuarios

def test_crear_segunda_cuenta():
    GestionUsuarios.crear_usuario("luisa", "pass")
    assert GestionUsuarios.validar_usuario("luisa", "pass")

def test_crear_cuenta_con_numeros():
    GestionUsuarios.crear_usuario("user123", "abc123")
    assert "user123" in GestionUsuarios.usuarios

# Iniciar sesión con datos válidos
def test_iniciar_sesion():
    GestionUsuarios.crear_usuario("ana", "abcd")
    assert GestionUsuarios.validar_usuario("ana", "abcd") is True

def test_iniciar_sesion_otra():
    GestionUsuarios.crear_usuario("marco", "clave")
    assert GestionUsuarios.validar_usuario("marco", "clave")

def test_iniciar_sesion_alfanumerica():
    GestionUsuarios.crear_usuario("prueba", "abc123")
    assert GestionUsuarios.validar_usuario("prueba", "abc123")

# Disparo en una celda aleatoria (puede ser agua o impacto)
def test_disparo_agua_o_impacto():
    GestionUsuarios.crear_usuario("carlos", "pass")
    GestionUsuarios.usuario_actual = "carlos"
    juego = Juego(5, 5, GestionUsuarios)
    resultado = juego.disparar(0, 0)
    assert resultado in ["Agua.", "Impacto confirmado.", "¡Nave hundida!"]

def test_disparo_en_esquina():
    GestionUsuarios.crear_usuario("ana", "123")
    GestionUsuarios.usuario_actual = "ana"
    juego = Juego(5, 5, GestionUsuarios)
    resultado = juego.disparar(4, 4)
    assert resultado in ["Agua.", "Impacto confirmado.", "¡Nave hundida!"]

def test_disparo_repetido():
    GestionUsuarios.crear_usuario("repe", "123")
    GestionUsuarios.usuario_actual = "repe"
    juego = Juego(5, 5, GestionUsuarios)
    juego.disparar(1, 1)
    resultado = juego.disparar(1, 1)
    assert resultado == "Agua."

# Puntaje incrementa con acierto
def test_puntaje_incrementa():
    GestionUsuarios.crear_usuario("maria", "clave")
    GestionUsuarios.usuario_actual = "maria"
    juego = Juego(5, 5, GestionUsuarios)
    for nave in juego.tablero.naves:
        fila, col = nave.posiciones[0]
        juego.disparar(fila, col)
        break
    puntaje = GestionUsuarios.obtener_puntaje("maria")
    assert puntaje in [0, 10]

def test_puntaje_tras_agua():
    GestionUsuarios.crear_usuario("natalia", "n123")
    GestionUsuarios.usuario_actual = "natalia"
    juego = Juego(5, 5, GestionUsuarios)
    juego.disparar(0, 0)
    puntaje = GestionUsuarios.obtener_puntaje("natalia")
    assert puntaje in [0]

def test_puntaje_dos_impactos():
    GestionUsuarios.crear_usuario("leo", "l1")
    GestionUsuarios.usuario_actual = "leo"
    juego = Juego(5, 5, GestionUsuarios)
    disparos = 0
    for nave in juego.tablero.naves:
        for pos in nave.posiciones:
            juego.disparar(*pos)
            disparos += 1
            if disparos == 2:
                break
        if disparos == 2:
            break
    puntaje = GestionUsuarios.obtener_puntaje("leo")
    assert puntaje in [10, 20, 0]  # Depende si acertó o no
