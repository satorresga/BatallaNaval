import hashlib

class GestionUsuarios:
    usuarios = {}  # Clase compartida para todos los usuarios {'usuario': {'clave': hash, 'puntaje': int}}

    @classmethod
    def crear_usuario(cls, usuario, contrasena):
        if usuario in cls.usuarios:
            raise ValueError("El usuario ya existe.")
        cls.usuarios[usuario] = {
            'clave': cls._encriptar(contrasena),
            'puntaje': 0
        }

    @classmethod
    def validar_usuario(cls, usuario, contrasena):
        return usuario in cls.usuarios and cls.usuarios[usuario]['clave'] == cls._encriptar(contrasena)

    @classmethod
    def cambiar_contrasena(cls, usuario, nueva_contrasena):
        if usuario in cls.usuarios:
            cls.usuarios[usuario]['clave'] = cls._encriptar(nueva_contrasena)

    @classmethod
    def sumar_puntaje(cls, usuario, puntos):
        if usuario in cls.usuarios:
            cls.usuarios[usuario]['puntaje'] += puntos

    @classmethod
    def obtener_puntaje(cls, usuario):
        return cls.usuarios.get(usuario, {}).get('puntaje', 0)

    @staticmethod
    def _encriptar(texto):
        return hashlib.sha256(texto.encode()).hexdigest()