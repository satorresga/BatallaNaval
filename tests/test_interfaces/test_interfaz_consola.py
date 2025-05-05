from unittest.mock import patch, MagicMock
from src.view.interfaz.interfaz_consola import InterfazConsola

class TestInterfazConsola:
    @patch('builtins.input', side_effect=['1', 'testuser', 'Testpass1!', '5'])
    @patch('builtins.print')
    def test_crear_cuenta(self, mock_print, mock_input):
        interfaz = InterfazConsola()
        interfaz.mostrar_menu()
        assert "testuser" in interfaz.gestor_usuarios.usuarios
        
    @patch('builtins.input', side_effect=['2', 'testuser', 'Testpass1!', '1', '0', '0', 'salir', '5'])
    @patch('builtins.print')
    def test_juego_completo(self, mock_print, mock_input):
        interfaz = InterfazConsola()
        interfaz.gestor_usuarios.crear_usuario("testuser", "Testpass1!")
        interfaz.mostrar_menu()
        
        output = " ".join(str(call) for call in mock_print.call_args_list)
        assert "Resultado:" in output
        
    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_salir_sin_login(self, mock_print, mock_input):
        interfaz = InterfazConsola()
        interfaz.mostrar_menu()  # Debería salir sin errores