import hashlib

class GestionUsuarios:
    """
    Clase para gestionar usuarios, contraseñas y puntajes en el sistema.
    Utiliza un diccionario de clase para almacenar la información de los usuarios.
    """
    
    usuarios = {}  # {'usuario': {'clave': hash, 'puntaje': int}}

    @classmethod
    def crear_usuario(cls, usuario, contrasena):
        """
        Crea un nuevo usuario en el sistema.
        
        Args:
            usuario (str): Nombre de usuario
            contrasena (str): Contraseña del usuario
            
        Raises:
            ValueError: Si el usuario ya existe o datos son inválidos
        """
        if not usuario or not contrasena:
            raise ValueError("Usuario y contraseña no pueden estar vacíos")
        if any(c in usuario for c in '@ '):
            raise ValueError("Usuario no puede contener espacios o @")
        if ' ' in contrasena:
            raise ValueError("Contraseña no puede contener espacios")
        if usuario in cls.usuarios:
            raise ValueError("El usuario ya existe.")
            
        cls.usuarios[usuario] = {
            'clave': cls._encriptar(contrasena),
            'puntaje': 0
        }

    @classmethod
    def validar_usuario(cls, usuario, contrasena):
        """
        Valida las credenciales de un usuario.
        
        Args:
            usuario (str): Nombre de usuario
            contrasena (str): Contraseña a validar
            
        Returns:
            bool: True si las credenciales son válidas, False en caso contrario
        """
        return usuario in cls.usuarios and cls.usuarios[usuario]['clave'] == cls._encriptar(contrasena)

    @classmethod
    def cambiar_contrasena(cls, usuario, nueva_contrasena):
        """
        Cambia la contraseña de un usuario existente.
        
        Args:
            usuario (str): Nombre de usuario
            nueva_contrasena (str): Nueva contraseña
            
        Raises:
            KeyError: Si el usuario no existe
        """
        if usuario not in cls.usuarios:
            raise KeyError("Usuario no existe")
        cls.usuarios[usuario]['clave'] = cls._encriptar(nueva_contrasena)

    @classmethod
    def sumar_puntaje(cls, usuario, puntos):
        """
        Suma puntos al puntaje acumulado de un usuario.
        Si el usuario no existe, lo crea con el puntaje inicial.
        
        Args:
            usuario (str): Nombre de usuario
            puntos (int): Puntos a sumar
        """
        if usuario in cls.usuarios:
            cls.usuarios[usuario]['puntaje'] += puntos
        else:
            cls.usuarios[usuario] = {
                'clave': '',  # Contraseña vacía para usuarios creados automáticamente
                'puntaje': puntos
            }

    @classmethod
    def obtener_puntaje(cls, usuario):
        """
        Obtiene el puntaje acumulado de un usuario.
        
        Args:
            usuario (str): Nombre de usuario
            
        Returns:
            int: Puntaje del usuario, 0 si no existe
        """
        return cls.usuarios.get(usuario, {}).get('puntaje', 0)

    @staticmethod
    def _encriptar(texto):
        """
        Encripta un texto usando SHA-256.
        
        Args:
            texto (str): Texto a encriptar
            
        Returns:
            str: Hash SHA-256 del texto
        """
        return hashlib.sha256(texto.encode()).hexdigest()