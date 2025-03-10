import sys, os

sys.path.append(os.path.abspath('..'))
sys.path.append('../proyecto_batalla_naval')

from proyecto_batalla_naval.autenticacion.gestion_usuarios import GestionUsuarios
from proyecto_batalla_naval.juego.juego import Juego

def prueba_disparo_fuera_tablero():
    juego = Juego(3, 3)
    resultado = juego.disparar(5, 5)
    assert resultado == "Posición fuera del tablero."
    print("prueba_disparo_fuera_tablero: PASÓ")

def prueba_crear_cuenta_existente():
    gestion = GestionUsuarios()
    gestion.crear_cuenta("usuarioExistente", "password123")
    try:
        gestion.crear_cuenta("usuarioExistente", "otraPass")
    except ValueError as e:
        assert str(e) == "El usuario ya existe."
        print("prueba_crear_cuenta_existente: PASÓ")

def prueba_inicio_sesion_incorrecto():
    gestion = GestionUsuarios()
    gestion.crear_cuenta("usuarioPrueba", "password123")
    resultado = gestion.iniciar_sesion("usuarioPrueba", "contraseñaIncorrecta")
    assert resultado == False
    print("prueba_inicio_sesion_incorrecto: PASÓ")

if __name__ == '__main__':
    prueba_disparo_fuera_tablero()
    prueba_crear_cuenta_existente()
    prueba_inicio_sesion_incorrecto()