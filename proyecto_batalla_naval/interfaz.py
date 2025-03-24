from .autenticacion.gestion_usuarios import GestionUsuarios
from .juego.juego import Juego

class Interfaz:
    def __init__(self):
        self.gestor_usuarios = GestionUsuarios()
        self.usuario_actual = None  # Guarda el usuario logueado actualmente

    def mostrar_menu(self):
        while True:
            if not self.usuario_actual:
                print("""
                ===== MENÚ PRINCIPAL =====
                1. Crear cuenta
                2. Iniciar sesión
                3. Salir
                """)

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    self.crear_cuenta()
                elif opcion == "2":
                    self.iniciar_sesion()
                elif opcion == "3":
                    print("¡Hasta pronto!")
                    break
                else:
                    print("Opción inválida.")
            else:
                # Ya logueado
                print(f"""
                ===== Bienvenido, {self.usuario_actual}! =====
                1. Jugar
                2. Ver puntajes
                3. Cambiar contraseña
                4. Cerrar sesión
                5. Salir
                """)

                opcion = input("Seleccione una opción: ")

                if opcion == '1':
                    self.iniciar_juego()
                elif opcion == "2":
                    self.ver_puntajes()
                elif opcion == '3':
                    self.cambiar_contrasena()
                elif opcion == '4':
                    self.usuario_actual = None
                    print("Sesión cerrada.")
                elif opcion == '5':
                    print("¡Hasta pronto!")
                    break
                else:
                    print("Opción inválida.")

    def crear_cuenta(self):
        usuario = input("Nuevo usuario: ")
        contraseña = input("Contraseña: ")
        try:
            GestionUsuarios.crear_usuario(usuario, contraseña)
            print("Cuenta creada exitosamente.")
            self.usuario_actual = usuario
        except ValueError as e:
            print("Error:", e)

    def iniciar_sesion(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if GestionUsuarios.validar_usuario(usuario, contraseña):
            self.usuario_actual = usuario
            print(f"Sesión iniciada correctamente. ¡Bienvenido {usuario}!")
        else:
            print("Credenciales incorrectas.")

    def cambiar_contrasena(self):
        nueva = input("Nueva contraseña: ")
        GestionUsuarios.cambiar_contrasena(self.usuario_actual, nueva)
        print("Contraseña actualizada correctamente.")

    def iniciar_juego(self):
        juego = Juego(5, 5, self)  # Pasa la instancia actual como referencia
        while True:
            try:
                entrada_fila = input("Fila (o 'salir'): ")
                if entrada_fila.lower() in ["salir", "q"]:
                    print("\U0001F6AA Saliendo del juego...")
                    break
                entrada_columna = input("Columna (o 'salir'): ")
                if entrada_columna.lower() in ["salir", "q"]:
                    print("\U0001F6AA Saliendo del juego...")
                    break

                fila = int(entrada_fila)
                columna = int(entrada_columna)
                resultado = juego.disparar(fila, columna)
                print("Resultado:", resultado)
                if juego.verificar_estado().startswith("¡Todas"):
                    print(juego.verificar_estado())
                    break
            except ValueError:
                print("Entrada inválida. Ingrese números.")

    def ver_puntajes(self):
        puntaje = GestionUsuarios.obtener_puntaje(self.usuario_actual)
        print(f"Puntaje actual de {self.usuario_actual}: {puntaje}")