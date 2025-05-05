from src.autenticacion.gestion_usuarios import GestionUsuarios
from src.juego.juego import Juego

class InterfazConsola:
    """
    Clase que maneja la interfaz de usuario por consola del juego Batalla Naval.
    """
    
    def __init__(self):
        """Inicializa la interfaz con un gestor de usuarios."""
        self.gestor_usuarios = GestionUsuarios()
        self.usuario_actual = None

    def mostrar_menu(self):
        """Muestra el menú principal y maneja las interacciones del usuario."""
        while True:
            self.mostrar_encabezado()
            
            if not self.usuario_actual:
                opciones = {
                    "1": ("Crear cuenta", self.crear_cuenta),
                    "2": ("Iniciar sesión", self.iniciar_sesion),
                    "3": ("Salir", self.salir)
                }
            else:
                opciones = {
                    "1": ("Jugar", self.iniciar_juego),
                    "2": ("Ver puntajes", self.ver_puntajes),
                    "3": ("Cambiar contraseña", self.cambiar_contrasena),
                    "4": ("Cerrar sesión", self.cerrar_sesion),
                    "5": ("Salir", self.salir)
                }
            
            self.mostrar_opciones(opciones)
            opcion = input("Seleccione una opción: ")
            
            if opcion in opciones:
                opciones[opcion][1]()
                if opcion in ["3", "5"]:  # Opciones de salida
                    break
            else:
                print("Opción inválida.")

    def mostrar_encabezado(self):
        """Muestra el encabezado del menú según el estado de autenticación."""
        if not self.usuario_actual:
            print("\n===== MENÚ PRINCIPAL =====")
        else:
            print(f"\n===== Bienvenido, {self.usuario_actual}! =====")

    def mostrar_opciones(self, opciones):
        """Muestra las opciones disponibles."""
        for key, value in opciones.items():
            print(f"{key}. {value[0]}")

    def crear_cuenta(self):
        """Maneja el proceso de creación de una nueva cuenta."""
        usuario = input("Nuevo usuario: ")
        contraseña = input("Contraseña: ")
        try:
            self.gestor_usuarios.crear_usuario(usuario, contraseña)
            self.usuario_actual = usuario
            print("Cuenta creada exitosamente.")
        except ValueError as e:
            print("Error:", e)

    def iniciar_sesion(self):
        """Maneja el proceso de inicio de sesión."""
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if self.gestor_usuarios.validar_usuario(usuario, contraseña):
            self.usuario_actual = usuario
            print(f"Sesión iniciada correctamente. ¡Bienvenido {usuario}!")
        else:
            print("Credenciales incorrectas.")

    def cambiar_contrasena(self):
        """Permite al usuario cambiar su contraseña."""
        nueva = input("Nueva contraseña: ")
        try:
            self.gestor_usuarios.cambiar_contrasena(self.usuario_actual, nueva)
            print("Contraseña actualizada correctamente.")
        except KeyError:
            print("Error: Usuario no existe")

    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual."""
        self.usuario_actual = None
        print("Sesión cerrada.")

    def iniciar_juego(self):
        """Inicia y maneja una partida de batalla naval."""
        juego = Juego(5, 5, self.gestor_usuarios, self.usuario_actual)
        
        print("\n=== BATALLA NAVAL ===")
        print("Ingresa coordenadas para disparar (0-4) o 'salir' para terminar")
        
        while True:
            try:
                entrada_fila = input("Fila (0-4): ")
                if entrada_fila.lower() in ["salir", "q"]:
                    print("Saliendo del juego...")
                    break
                
                entrada_columna = input("Columna (0-4): ")
                if entrada_columna.lower() in ["salir", "q"]:
                    print("Saliendo del juego...")
                    break

                fila = int(entrada_fila)
                columna = int(entrada_columna)
                
                if not (0 <= fila < 5 and 0 <= columna < 5):
                    print("Coordenadas deben estar entre 0 y 4")
                    continue
                
                resultado = juego.disparar(fila, columna)
                print("Resultado:", resultado)
                
                if juego.verificar_estado().startswith("¡Todas"):
                    print(juego.verificar_estado())
                    break
                    
            except ValueError:
                print("Entrada inválida. Ingrese números entre 0 y 4.")

    def ver_puntajes(self):
        """Muestra el puntaje del usuario actual."""
        puntaje = self.gestor_usuarios.obtener_puntaje(self.usuario_actual)
        print(f"Puntaje actual de {self.usuario_actual}: {puntaje}")

    def salir(self):
        """Finaliza la aplicación."""
        print("¡Hasta pronto!")