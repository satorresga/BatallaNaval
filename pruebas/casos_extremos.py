import sys, os

#sys.path.append('../proyecto_batalla_naval')
sys.path.append(os.path.abspath('..'))
from proyecto_batalla_naval.juego.nave import Nave
from proyecto_batalla_naval.autenticacion.gestion_usuarios import GestionUsuarios
from proyecto_batalla_naval.juego.juego import Juego

def prueba_disparo_borde_tablero():
    juego = Juego(3, 3)
    resultado = juego.disparar(0, 2)  
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!", "Agua."]
    print("prueba_disparo_borde_tablero: PASÓ")

def prueba_tablero_minimo():
    juego = Juego(1, 1, colocar_naves_auto=False)  
    nave = Nave(1)
    nave.posiciones = [(0, 0)]
    juego.tablero.naves.append(nave)
    juego.tablero.matriz[0][0] = 'N'

    resultado = juego.disparar(0, 0)
    assert resultado in ["Impacto confirmado.", "¡Nave hundida!"]
    print("prueba_tablero_minimo: PASÓ")

if __name__ == '__main__':
    prueba_disparo_borde_tablero()
    prueba_tablero_minimo()