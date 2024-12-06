import datetime
from colorama import Fore
import libros
import usuarios
import main
historial_prestamos = []
prestamos_usuario = {}

def prestar_libro():
    libros.mostrar_libro() # Se llama a la función "mostrar_libro" para mostrarle al usuario los libros que se han creado
   
    # Verifica si hay libros en la lista y si no hay nada envia al usuario al menú principal
    if len(libros.crear_libros) == 0:
        main.menu_principal()
 
    isbn = input(Fore.GREEN + "Ingrese el ISBN del libro que desea prestar: ") # Pide introducir el isbn del libro para poder seleccionarlo para el prestamo
   
    # Verifica que el ISBN sean solo números
    if not isbn.isdigit():
        print(Fore.RED + "Error: El ISBN debe contener solo números.")
        return
 
    libro_encontrado = False # Se inicializa una variable que verifica si el ISBN no se encuentra registrado con algún libro
 
    # Bucle para verificar si el libro se encuentra en la lista "crear_libros"
    for libro in libros.crear_libros:
        if libro['ISBN'] == isbn:
            libro_encontrado = True
            id_usuario = input(Fore.GREEN + "Ingrese el ID del usuario que hará el préstamo: ")
            usuario_encontrado = None # Verifica si el ID no coincide con algun usuario registrado  
           
            # Bucle para verificar si el usuario se encuentra registrado en la lista "crear_usuarios"
            for usuario in usuarios.crear_usuarios:
                if usuario['ID'] == id_usuario:
                    usuario_encontrado = usuario
 
            # Arroja un mensaje si el usuario no fue encontrado en el sistema y es enviado al menú principal
            if usuario_encontrado is None:
                print(Fore.RED + "=== Usuario no encontrado ===")
                main.menu_principal()
                return True
           
            # Si el ID del usuario no está registrado en los prestamos, se añadirá en el diccionario
            if id_usuario not in prestamos_usuario:
                prestamos_usuario[id_usuario] = {}  
 
            cantidad_actual = libro['Libros_dispo']  # Cantidad de libros disponibles actualmente en el inventario.
 
            while True:
                try:
                    # Solicita al usuario la cantidad de libros que desea prestar y la convierte a entero.
                    cantidad_prestamo = int(input("Ingrese la cantidad de libros que desea prestar: "))
                   
                    # Verifica si la cantidad ingresada es mayor que 0, en caso contrario, muestra un error y vuelve a solicitar.
                    if cantidad_prestamo <= 0:
                        print(Fore.RED + "La cantidad debe ser mayor que 0.")
                        continue
 
                    # Verifica si la cantidad solicitada es mayor que la disponible en el inventario.
                    if cantidad_prestamo > cantidad_actual:
                        print(Fore.RED + f"Error: No se pueden prestar {cantidad_prestamo}. Solo hay {cantidad_actual} disponibles.")
                        # Llama al menú principal si no es posible prestar la cantidad solicitada.
                        main.menu_principal()
 
                    else:
                        # Si el ISBN ya está registrado en los préstamos del usuario, incrementa la cantidad prestada.
                        if isbn in prestamos_usuario[id_usuario]:
                            prestamos_usuario[id_usuario][isbn] += cantidad_prestamo
                        else:
                            # Si no está registrado, crea una nueva entrada para el usuario con el ISBN y la cantidad prestada.
                            prestamos_usuario[id_usuario][isbn] = cantidad_prestamo
 
                        # Actualiza el inventario restando la cantidad prestada del total de libros disponibles.
                        libro['Libros_dispo'] -= cantidad_prestamo
 
                        # Agrega un registro al historial de préstamos con detalles como ISBN, título, ID del usuario, cantidad prestada y fecha del préstamo.
                        historial_prestamos.append({
                            "ISBN": libro['ISBN'],
                            "Titulo": libro['Titulo'],
                            "ID Usuario": id_usuario,
                            "Cantidad prestamo": cantidad_prestamo,
                            "Fecha de prestamo": datetime.datetime.now()
                        })
 
                        # Confirma al usuario que el préstamo se ha realizado con éxito, mostrando el libro prestado y la cantidad.
                        print(Fore.GREEN + f"Se han prestado {cantidad_prestamo} copias del libro '{libro['Titulo']}' al usuario {id_usuario}.")
                       
                        # Sale del ciclo una vez que se ha realizado el préstamo correctamente.
                        break
 
                except ValueError:
                    # Maneja el error si el usuario ingresa un valor que no es un número entero.
                    print(Fore.RED + "Error: La cantidad debe ser un número entero.")
    pass  # Implementar la función

def mostrar_historial_prestamos():
    # Verificar que se hayan hecho prestamos
    if not historial_prestamos:
        print(Fore.RED + "No hay préstamos registrados.") # Mostramos el mensaje por si no hay ningun prestamo registrado
        return
   
    print(Fore.GREEN + "==== Historial de libros préstados ==== ")
   
    #aca llamamos al diccionario de historial de prestamos en donde guardamos la anterior informacion
    for registro in historial_prestamos:
        print(
            f"ISBN: {registro['ISBN']} - "
            f"Titulo: {registro['Titulo']} - "
            f"ID Usuario: {registro['ID Usuario']} - "
            f"Cantidad Prestada: {registro['Cantidad prestamo']} - "
            f"Fecha de prestamo: {registro['Fecha de prestamo']}"
        )
    pass  # Implementar la función

def menu_prestamos():
    while True:
        print(Fore.CYAN + "== Menú de préstamos de libros ==")
        print("1. Prestar libro")
        print("2. Historial de Préstamos")
        print("3. Regresar al menú principal")
        opcion = input(Fore.YELLOW + "Elige una opción: ")

        if opcion == "1":
            prestar_libro()
        elif opcion == "2":
            mostrar_historial_prestamos()
        elif opcion == "3":
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
