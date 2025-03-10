from autenticacion.gestion_usuarios import GestionUsuarios
from juego.juego import Juego
from puntuaciones.puntaje import Puntuaciones

def main():
    gestion_usuarios = GestionUsuarios()
    puntuaciones = Puntuaciones()

    while True:
        print("\n--- Juego Batalla Naval ---")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            usuario = input("Nuevo usuario: ")
            contraseña = input("Contraseña: ")
            try:
                gestion_usuarios.crear_cuenta(usuario, contraseña)
                print("¡Cuenta creada exitosamente!")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            if gestion_usuarios.iniciar_sesion(usuario, contraseña):
                print(f"¡Bienvenido {usuario}!")
                ancho = int(input("Ancho del tablero: "))
                alto = int(input("Alto del tablero: "))
                juego = Juego(ancho, alto)

                while True:
                    fila = int(input("Disparar en fila: "))
                    columna = int(input("Disparar en columna: "))
                    resultado = juego.disparar(fila, columna)
                    print(resultado)

                    if juego.verificar_estado() == "¡Todas las naves hundidas! Juego terminado.":
                        print("Ganaste el juego!")
                        puntuaciones.registrar_puntaje(usuario, 100)
                        break
                
                puntuaciones.mostrar_tabla_puntuaciones()

            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == '3':
            print("Saliendo del juego...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()