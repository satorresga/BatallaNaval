import tkinter as tk
from src.view.interfaz.interfaz_grafica import InterfazGrafica

def main():
    """Función principal para la aplicación gráfica."""
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()