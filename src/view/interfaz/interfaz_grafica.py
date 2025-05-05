import tkinter as tk
from tkinter import messagebox, simpledialog
from src.autenticacion.gestion_usuarios import GestionUsuarios
from src.juego.juego import Juego

class InterfazGrafica:
    """Clase que implementa la interfaz gráfica del juego usando Tkinter."""
    
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica.
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Batalla Naval")
        self.gestor_usuarios = GestionUsuarios()
        self.usuario_actual = None
        self.juego = None
        
        # Configuración de la ventana
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Mostrar pantalla de inicio
        self.mostrar_pantalla_inicio()

    def mostrar_pantalla_inicio(self):
        """Muestra la pantalla de inicio (login/registro)."""
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="BATALLA NAVAL", font=("Arial", 24)).pack(pady=20)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        if not self.usuario_actual:
            # Usuario no logueado
            tk.Button(frame_botones, text="Iniciar Sesión", command=self.mostrar_login, 
                     width=15).pack(side=tk.LEFT, padx=10)
            tk.Button(frame_botones, text="Crear Cuenta", command=self.mostrar_registro,
                     width=15).pack(side=tk.LEFT, padx=10)
        else:
            # Usuario logueado
            tk.Label(self.root, text=f"Bienvenido, {self.usuario_actual}!", 
                    font=("Arial", 14)).pack(pady=10)
            
            frame_opciones = tk.Frame(self.root)
            frame_opciones.pack(pady=20)
            
            tk.Button(frame_opciones, text="Jugar", command=self.iniciar_juego,
                     width=15).pack(pady=5)
            tk.Button(frame_opciones, text="Ver Puntaje", command=self.ver_puntaje,
                     width=15).pack(pady=5)
            tk.Button(frame_opciones, text="Cambiar Contraseña", command=self.cambiar_contrasena,
                     width=15).pack(pady=5)
            tk.Button(frame_opciones, text="Cerrar Sesión", command=self.cerrar_sesion,
                     width=15).pack(pady=5)
        
        tk.Button(self.root, text="Salir", command=self.root.quit,
                 width=10).pack(pady=20)

    def mostrar_login(self):
        """Muestra el diálogo de inicio de sesión."""
        usuario = simpledialog.askstring("Iniciar Sesión", "Usuario:")
        if usuario:
            contrasena = simpledialog.askstring("Iniciar Sesión", "Contraseña:", show='*')
            if contrasena and self.gestor_usuarios.validar_usuario(usuario, contrasena):
                self.usuario_actual = usuario
                messagebox.showinfo("Éxito", f"Bienvenido, {usuario}!")
                self.mostrar_pantalla_inicio()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")

    def mostrar_registro(self):
        """Muestra el diálogo de registro de nuevo usuario."""
        usuario = simpledialog.askstring("Crear Cuenta", "Nuevo usuario:")
        if usuario:
            contrasena = simpledialog.askstring("Crear Cuenta", "Contraseña:", show='*')
            if contrasena:
                try:
                    self.gestor_usuarios.crear_usuario(usuario, contrasena)
                    self.usuario_actual = usuario
                    messagebox.showinfo("Éxito", "Cuenta creada exitosamente!")
                    self.mostrar_pantalla_inicio()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))

    def cambiar_contrasena(self):
        """Maneja el cambio de contraseña."""
        if self.usuario_actual:
            nueva = simpledialog.askstring("Cambiar Contraseña", "Nueva contraseña:", show='*')
            if nueva:
                try:
                    self.gestor_usuarios.cambiar_contrasena(self.usuario_actual, nueva)
                    messagebox.showinfo("Éxito", "Contraseña actualizada correctamente")
                    self.mostrar_pantalla_inicio()
                except KeyError:
                    messagebox.showerror("Error", "Usuario no existe")

    def ver_puntaje(self):
        """Muestra el puntaje del usuario actual."""
        if self.usuario_actual:
            puntaje = self.gestor_usuarios.obtener_puntaje(self.usuario_actual)
            messagebox.showinfo("Puntaje", f"Tu puntaje actual es: {puntaje}")

    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual."""
        self.usuario_actual = None
        self.mostrar_pantalla_inicio()

    def iniciar_juego(self):
        """Inicia una nueva partida del juego."""
        if not self.usuario_actual:
            return
            
        self.limpiar_pantalla()
        
        self.juego = Juego(5, 5, self.gestor_usuarios, self.usuario_actual)
        
        tk.Label(self.root, text="BATALLA NAVAL", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.root, text=f"Jugador: {self.usuario_actual}", font=("Arial", 12)).pack()
        
        # Frame para el tablero
        frame_tablero = tk.Frame(self.root)
        frame_tablero.pack(pady=20)
        
        # Crear botones para el tablero
        self.botones_tablero = []
        for fila in range(5):
            fila_botones = []
            for columna in range(5):
                btn = tk.Button(frame_tablero, text="~", width=4, height=2,
                               command=lambda f=fila, c=columna: self.realizar_disparo(f, c))
                btn.grid(row=fila, column=columna, padx=2, pady=2)
                fila_botones.append(btn)
            self.botones_tablero.append(fila_botones)
        
        # Botón para salir del juego
        tk.Button(self.root, text="Salir del Juego", command=self.mostrar_pantalla_inicio,
                 width=15).pack(pady=10)

    def realizar_disparo(self, fila, columna):
        """Realiza un disparo en las coordenadas especificadas."""
        if not self.juego:
            return
            
        resultado = self.juego.disparar(fila, columna)
        
        # Actualizar el botón según el resultado
        if resultado == "Agua.":
            self.botones_tablero[fila][columna].config(text="O", bg="lightblue")
        elif resultado == "Impacto confirmado.":
            self.botones_tablero[fila][columna].config(text="X", bg="red")
        elif resultado == "¡Nave hundida!":
            self.botones_tablero[fila][columna].config(text="X", bg="darkred")
        
        # Mostrar resultado
        messagebox.showinfo("Resultado", resultado)
        
        # Verificar si el juego terminó
        if self.juego.verificar_estado().startswith("¡Todas"):
            messagebox.showinfo("Fin del Juego", self.juego.verificar_estado())
            self.mostrar_pantalla_inicio()

    def limpiar_pantalla(self):
        """Limpia todos los widgets de la pantalla."""
        for widget in self.root.winfo_children():
            widget.destroy()