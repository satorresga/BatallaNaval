import pytest
from src.autenticacion.gestion_usuarios import GestionUsuarios

class TestGestionUsuarios:
    """Pruebas para la clase GestionUsuarios"""
    
    def test_sumar_puntaje_positivo(self):
        """Test: Suma de puntos positivos"""
        GestionUsuarios.crear_usuario("user1", "pass")
        
        # Primer suma
        GestionUsuarios.sumar_puntaje("user1", 10)
        assert GestionUsuarios.obtener_puntaje("user1") == 10
        
        # Segunda suma (acumulativo)
        GestionUsuarios.sumar_puntaje("user1", 5)
        assert GestionUsuarios.obtener_puntaje("user1") == 15

    def test_sumar_puntaje_negativo(self):
        """Test: Suma de puntos negativos"""
        GestionUsuarios.crear_usuario("user2", "pass")
        
        # Suma inicial
        GestionUsuarios.sumar_puntaje("user2", 15)
        assert GestionUsuarios.obtener_puntaje("user2") == 15
        
        # Resta de puntos
        GestionUsuarios.sumar_puntaje("user2", -3)
        assert GestionUsuarios.obtener_puntaje("user2") == 12

    def test_sumar_puntaje_usuario_nuevo(self):
        """Test: Suma de puntos a usuario no existente"""
        # Usuario no existe previamente
        assert "user3" not in GestionUsuarios.usuarios
        
        # Sumar puntos crea el usuario
        GestionUsuarios.sumar_puntaje("user3", 8)
        assert GestionUsuarios.obtener_puntaje("user3") == 8