
import hashlib
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from database.models import init_db, get_session, Usuario, Puntuacion, Partida
from datetime import datetime

class GestionUsuariosORM:
    """Clase para gestión de usuarios con persistencia ORM."""

    def __init__(self):
        self.engine = init_db()
        self.session = get_session(self.engine)

    def crear_usuario(self, usuario, contrasena):
        if not usuario or not contrasena:
            raise ValueError("Usuario y contraseña no pueden estar vacíos")
        if any(c in usuario for c in '@ '):
            raise ValueError("Usuario no puede contener espacios o @")
        if ' ' in contrasena:
            raise ValueError("Contraseña no puede contener espacios")

        nuevo = Usuario(
            nombre_usuario=usuario,
            clave_hash=self._encriptar(contrasena)
        )
        try:
            self.session.add(nuevo)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ValueError("El usuario ya existe.")

    def validar_usuario(self, usuario, contrasena):
        user = self.session.query(Usuario).filter_by(nombre_usuario=usuario).first()
        return user and user.clave_hash == self._encriptar(contrasena)

    def cambiar_contrasena(self, usuario, nueva_contrasena):
        user = self.session.query(Usuario).filter_by(nombre_usuario=usuario).first()
        if not user:
            raise KeyError("Usuario no existe")
        user.clave_hash = self._encriptar(nueva_contrasena)
        self.session.commit()

    def sumar_puntaje(self, usuario, puntos):
        user = self.session.query(Usuario).filter_by(nombre_usuario=usuario).first()
        if not user:
            raise KeyError("Usuario no existe")

        # Crear partida dummy si no existe
        partida = Partida(id_usuario=user.id_usuario, resultado="temporal")
        self.session.add(partida)
        self.session.commit()

        puntuacion = Puntuacion(
            id_usuario=user.id_usuario,
            id_partida=partida.id_partida,
            puntos=puntos
        )
        self.session.add(puntuacion)
        self.session.commit()

    def obtener_puntaje(self, usuario):
        user = self.session.query(Usuario).filter_by(nombre_usuario=usuario).first()
        if not user:
            return 0
        total = self.session.query(func.sum(Puntuacion.puntos)).filter_by(id_usuario=user.id_usuario).scalar()
        return total or 0

    @staticmethod
    def _encriptar(texto):
        return hashlib.sha256(texto.encode()).hexdigest()
