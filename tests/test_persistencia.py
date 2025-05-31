
import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from database.models import init_db, get_session, Base, Usuario, Partida, Puntuacion

class TestPersistencia:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.engine = init_db()
        self.session = get_session(self.engine)
        # Limpiar las tablas antes de cada test
        for table in reversed(Base.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.session.commit()

    def test_crear_usuario(self):
        user = Usuario(nombre_usuario="testuser", clave_hash="hash123")
        self.session.add(user)
        self.session.commit()

        retrieved = self.session.query(Usuario).filter_by(nombre_usuario="testuser").first()
        assert retrieved is not None
        assert retrieved.clave_hash == "hash123"

    def test_usuario_unico(self):
        user1 = Usuario(nombre_usuario="testuser", clave_hash="hash123")
        self.session.add(user1)
        self.session.commit()

        user2 = Usuario(nombre_usuario="testuser", clave_hash="hash456")
        self.session.add(user2)
        with pytest.raises(IntegrityError):
            self.session.commit()

    def test_relacion_usuario_partida(self):
        user = Usuario(nombre_usuario="testuser", clave_hash="hash123")
        game = Partida(usuario=user, resultado="victoria")
        self.session.add_all([user, game])
        self.session.commit()

        partida = self.session.query(Partida).first()
        assert partida.usuario.nombre_usuario == "testuser"

    def test_puntuacion_total(self):
        user = Usuario(nombre_usuario="testuser", clave_hash="hash123")
        game = Partida(usuario=user)
        score1 = Puntuacion(usuario=user, partida=game, puntos=10)
        score2 = Puntuacion(usuario=user, partida=game, puntos=20)
        self.session.add_all([user, game, score1, score2])
        self.session.commit()

        total = self.session.query(func.sum(Puntuacion.puntos)).filter_by(id_usuario=user.id_usuario).scalar()
        assert total == 30
