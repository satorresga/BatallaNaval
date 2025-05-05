import pytest
from src.autenticacion.gestion_usuarios import GestionUsuarios
from src.juego.juego import Juego
from src.juego.tablero import Tablero
from src.juego.nave import Nave
from src.puntuaciones.puntaje import Puntuaciones

@pytest.fixture(autouse=True)
def limpiar_usuarios():
    """Fixture que limpia los usuarios antes y después de cada prueba."""
    GestionUsuarios.usuarios.clear()
    yield
    GestionUsuarios.usuarios.clear()

@pytest.fixture
def juego_configurado():
    """Fixture que provee un juego configurado para pruebas."""
    GestionUsuarios.crear_usuario("test_player", "test_pass")
    juego = Juego(5, 5, GestionUsuarios, "test_player")
    return juego

@pytest.fixture
def tablero_vacio():
    """Fixture que provee un tablero vacío."""
    return Tablero(5, 5)

@pytest.fixture
def tablero_con_naves():
    """Fixture que provee un tablero con naves colocadas."""
    tablero = Tablero(5, 5)
    tablero.colocar_naves(3)
    return tablero

@pytest.fixture
def nave_pequena():
    """Fixture que provee una nave pequeña."""
    nave = Nave(1)
    nave.posiciones = [(0, 0)]
    return nave

@pytest.fixture
def nave_mediana():
    """Fixture que provee una nave mediana."""
    nave = Nave(2)
    nave.posiciones = [(0, 0), (0, 1)]
    return nave

@pytest.fixture(scope="module")
def puntuaciones():
    """Fixture a nivel de módulo para el sistema de puntuaciones."""
    return Puntuaciones()

def pytest_runtest_makereport(item, call):
    """Hook para agregar información adicional a los reportes de pruebas."""
    if call.when == "call":
        print(f"\nPrueba ejecutada: {item.nodeid}")