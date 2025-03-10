# gestion_usuarios.py

class GestionUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_cuenta(self, usuario, contraseña):
        if usuario in self.usuarios:
            raise ValueError("El usuario ya existe.")
        self.usuarios[usuario] = {'contraseña': contraseña, 'puntaje': 0}

    def iniciar_sesion(self, usuario, contraseña):
        if usuario in self.usuarios and self.usuarios[usuario]['contraseña'] == contraseña:
            return True
        return False

    def cambiar_contraseña(self, usuario, contraseña_vieja, contraseña_nueva):
        if usuario not in self.usuarios:
            raise ValueError("El usuario no existe.")
        if self.usuarios[usuario]['contraseña'] != contraseña_vieja:
            raise ValueError("Contraseña incorrecta.")
        self.usuarios[usuario]['contraseña'] = contraseña_nueva

    def obtener_puntaje(self, usuario):
        if usuario in self.usuarios:
            return self.usuarios[usuario]['puntaje']
        raise ValueError("El usuario no existe.")

    def actualizar_puntaje(self, usuario, puntos):
        if usuario in self.usuarios:
            self.usuarios[usuario]['puntaje'] += puntos
