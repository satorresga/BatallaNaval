from src.puntuaciones.puntaje import Puntuaciones

class TestPuntuaciones:
    def test_registrar_puntaje_nuevo(self):
        punt = Puntuaciones()
        punt.registrar_puntaje("user1", 10)
        assert punt.puntuaciones["user1"] == 10
        
    def test_registrar_puntaje_existente(self):
        punt = Puntuaciones()
        punt.registrar_puntaje("user2", 5)
        punt.registrar_puntaje("user2", 3)
        assert punt.puntuaciones["user2"] == 8
        
    def test_obtener_puntuaciones_orden(self):
        punt = Puntuaciones()
        punt.registrar_puntaje("low", 1)
        punt.registrar_puntaje("high", 10)
        punt.registrar_puntaje("mid", 5)
        
        result = punt.obtener_puntuaciones()
        assert result == [("high", 10), ("mid", 5), ("low", 1)]
        
    def test_mostrar_tabla_puntuaciones(self, capsys):
        punt = Puntuaciones()
        punt.registrar_puntaje("user3", 7)
        punt.mostrar_tabla_puntuaciones()
        
        captured = capsys.readouterr()
        assert "user3: 7 puntos" in captured.out
        
    def test_puntuaciones_vacias(self):
        punt = Puntuaciones()
        assert punt.obtener_puntuaciones() == []
        
    def test_multiple_users(self):
        punt = Puntuaciones()
        punt.registrar_puntaje("a", 1)
        punt.registrar_puntaje("b", 2)
        punt.registrar_puntaje("c", 3)
        
        assert len(punt.obtener_puntuaciones()) == 3