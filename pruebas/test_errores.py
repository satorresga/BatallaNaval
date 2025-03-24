import pytest
from proyecto_batalla_naval.autenticacion.gestion_usuarios import GestionUsuarios
from proyecto_batalla_naval.juego.juego import Juego

# Reiniciar usuarios antes de cada prueba de error
def setup_function():
    GestionUsuarios.usuarios.clear()

# Crear usuario duplicado
def test_usuario_duplicado():
    GestionUsuarios.crear_usuario("admin", "123")
    with pytest.raises(ValueError):
        GestionUsuarios.crear_usuario("admin", "otra")

# Iniciar sesión con contraseña incorrecta
def test_sesion_contraseña_incorrecta():
    GestionUsuarios.crear_usuario("lucia", "clave123")
    assert GestionUsuarios.validar_usuario("lucia", "clave_mal") is False

# Iniciar sesión con usuario inexistente
def test_usuario_inexistente():
    assert GestionUsuarios.validar_usuario("no_existe", "cualquier") is False

# Disparar fuera del tablero (negativo y fuera de rango)
@pytest.mark.parametrize("fila,columna", [(-1, 0), (0, -1), (10, 10), (999, 999)])
def test_disparo_fuera_tablero(fila, columna):
    GestionUsuarios.crear_usuario("fuera", "borde")
    GestionUsuarios.usuario_actual = "fuera"
    juego = Juego(5, 5, GestionUsuarios)
    resultado = juego.disparar(fila, columna)
    assert resultado == "Posición fuera del tablero."

# Cambiar contraseña sin haber iniciado sesión (usuario no logueado)
def test_cambiar_contraseña_sin_login():
    GestionUsuarios.crear_usuario("pepe", "abc")
    GestionUsuarios.usuario_actual = None
    GestionUsuarios.cambiar_contrasena("pepe", "nueva")  # Debe cambiar directamente al usuario
    assert GestionUsuarios.validar_usuario("pepe", "nueva") is True
