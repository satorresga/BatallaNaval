from sqlalchemy.exc import IntegrityError
from database.models import Usuario
from datetime import datetime
import bcrypt


class GestionUsuariosORM:
    """
    Clase para gestionar usuarios utilizando SQLAlchemy ORM.
    """

    def __init__(self, session):
        """
        Inicializa el gestor con una sesión activa de SQLAlchemy.
        :param session: Sesión de SQLAlchemy para interactuar con la base de datos.
        """
        self.session = session

    def registrar_usuario(self, nombre_usuario, clave):
        """
        Registra un nuevo usuario con nombre y clave encriptada.
        :param nombre_usuario: Nombre único del usuario.
        :param clave: Clave en texto plano.
        :raises ValueError: Si el nombre de usuario ya existe.
        """
        if self.session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first():
            raise ValueError("El nombre de usuario ya existe.")

        hash_clave = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        nuevo_usuario = Usuario(
            nombre_usuario=nombre_usuario,
            clave_hash=hash_clave,
            fecha_creacion=datetime.now()
        )
        self.session.add(nuevo_usuario)

        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ValueError("Error al registrar el usuario.")

    def autenticar_usuario(self, nombre_usuario, clave):
        """
        Verifica si un usuario existe y si la clave es correcta.
        :param nombre_usuario: Nombre del usuario.
        :param clave: Clave en texto plano.
        :return: True si autenticado correctamente, False en caso contrario.
        """
        usuario = self.session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
        if usuario and bcrypt.checkpw(clave.encode('utf-8'), usuario.clave_hash.encode('utf-8')):
            return True
        return False
