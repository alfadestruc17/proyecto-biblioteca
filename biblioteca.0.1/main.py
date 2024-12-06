import sys
from colorama import Fore
import usuarios
import libros
import prestamos
import devoluciones
def menu_principal():
    while True:
        print(Fore.CYAN + "===== Bienvenido al sistema de Biblioteca =====")
        print("1. Usuarios")
        print("2. Libros")
        print("3. Prestar Libro")
        print("4. Devolver libro")
        print("5. Salir")
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")

        if opcion == "1":
            usuarios.menu_usuarios()  # Muestra el menú de gestión de usuarios
        elif opcion == "2":
            libros.menu_libros()  # Muestra el menú de gestión de libros
        elif opcion == "3":
            prestamos.menu_prestamos()  # Muestra el menú de préstamos de libros
        elif opcion == "4":
            devoluciones.elegir_opcion()  # Llama a la función para devolver libros
        elif opcion == "5":
            print(Fore.CYAN + "==== Gracias por visitar la biblioteca ====")
            sys.exit(0)  # Cierra el programa
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
