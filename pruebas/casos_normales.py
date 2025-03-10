import sys
import os

sys.path.append(os.path.abspath('..'))
from proyecto_batalla_naval.juego.nave import Nave
from proyecto_batalla_naval.autenticacion.gestion_usuarios import GestionUsuarios
from proyecto_batalla_naval.juego.juego import Juego

def prueba_disparo_acertado():
    juego = Juego(3, 3, colocar_naves_auto=False)  
    juego.tablero.matriz[0][0] = 'N'
    nave = Nave(1)
    nave.posiciones = [(0, 0)]
    juego.tablero.naves.append(nave)
    resultado = juego.disparar(0, 0)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!"]
    print("prueba_disparo_acertado: PASÓ")

def prueba_disparo_agua():
    juego = Juego(3, 3, colocar_naves_auto=False) 
    resultado = juego.disparar(1, 1)
    assert resultado == "Agua."
    print("prueba_disparo_agua: PASÓ")

def prueba_crear_usuario():
    gestion = GestionUsuarios()
    gestion.crear_cuenta("nuevoUsuario", "password123")
    resultado = gestion.iniciar_sesion("nuevoUsuario", "password123")
    assert resultado == True
    print("prueba_crear_usuario: PASÓ")

if __name__ == '__main__':
    prueba_disparo_acertado()
    prueba_disparo_agua()
    prueba_crear_usuario()
