import pytest
from unittest.mock import MagicMock, patch
from tkinter import Tk
from src.view.interfaz.interfaz_grafica import InterfazGrafica

class TestInterfazGrafica:
    @patch('tkinter.simpledialog.askstring', side_effect=['testuser', 'Testpass1!'])
    def test_crear_cuenta(self, mock_askstring):
        root = Tk()
        root.withdraw()
        interfaz = InterfazGrafica(root)
        interfaz.mostrar_registro()
        assert "testuser" in interfaz.gestor_usuarios.usuarios
        
    @patch('tkinter.simpledialog.askstring', side_effect=['testuser', 'Testpass1!'])
    @patch('tkinter.messagebox.showinfo')
    def test_login_exitoso(self, mock_showinfo, mock_askstring):
        root = Tk()
        root.withdraw()
        interfaz = InterfazGrafica(root)
        interfaz.gestor_usuarios.crear_usuario("testuser", "Testpass1!")
        interfaz.mostrar_login()
        assert interfaz.usuario_actual == "testuser"
        
    @patch('tkinter.messagebox.showerror')
    def test_login_fallido(self, mock_showerror):
        root = Tk()
        root.withdraw()
        interfaz = InterfazGrafica(root)
        interfaz.mostrar_login()  # No hay usuarios creados
        mock_showerror.assert_called()