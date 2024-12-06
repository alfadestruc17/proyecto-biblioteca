from colorama import Fore
import datetime
historial_devoluciones = []  
import libros
import prestamos
import main




def devolver_libro():
    libros.mostrar_libro() # Llamamos la función de mostrar libros
    if len(libros.crear_libros) == 0: # Verificamos que si hayan libros registrados
        main.menu_principal()
    isbn = input(Fore.GREEN + "Ingrese el ISBN del libro que desea devolver: ")
 
    if not isbn.isdigit(): # Comprobamos que solo sean dijitos
        print(Fore.RED + "Error: El ISBN debe contener solo números.")
        return
 
    id_usuario = input("Ingrese el ID del usuario que devuelve el libro: ")
 
    if id_usuario not in prestamos.prestamos_usuario or isbn not in prestamos.prestamos_usuario[id_usuario]: # Comprobamos que si exista un usuario en el sistema
        print(Fore.RED + "Error: ID de usuario no registrado o no se ha prestado este libro a este usuario.")
        return
 
    libro_encontrado = False
   
    # Busca el libro en la lista de libros registrados.
    for libro in libros.crear_libros:
        if libro['ISBN'] == isbn:
            libro_encontrado = True
 
            cantidad_prestada = prestamos.prestamos_usuario[id_usuario][isbn] # Actualiza la cantidad de libros prestados en el registro del usuario.
 
            # Le mostramos al usuario que escoja el motivo por el cual va a devolver el libro
            print("Seleccione el motivo de la devolución:")
            print("1. Libro equivocado")
            print("2. Fin del tiempo de préstamo")
            motivo = input(Fore.YELLOW + "Ingrese el número de la opción: ")
           
            if motivo == "1":
                motivo = "Libro equivocado"
            elif motivo == "2":
                motivo = "Fin del tiempo de préstamo"
            else:
                print(Fore.RED + "Opción inválida. Devolución cancelada.")
                return
 
            # Bucle creado para validar las cantidades que se van a devolver
            while True:
                try:
                    cantidad_a_devolver = int(input(f"Ingrese la cantidad que desea devolver (prestados: {cantidad_prestada}): "))
                    if cantidad_a_devolver <= 0:
                        print(Fore.RED + "Error: La cantidad debe ser mayor que 0.")
                    elif cantidad_a_devolver > cantidad_prestada:
                        print(Fore.RED + f"Error: No puede devolver más de lo prestado ({cantidad_prestada} copias prestadas).")
                    else:
 
                        libro['Libros_dispo'] += cantidad_a_devolver
 
                        prestamos.prestamos_usuario[id_usuario][isbn] -= cantidad_a_devolver
 
                        if prestamos.prestamos_usuario[id_usuario][isbn] == 0:
                            del prestamos.prestamos_usuario[id_usuario][isbn]
                       
                        historial_devoluciones.append({ # Guardamos la informacion en un diccionario la cual nos servira para el historial de devoluciones
                            "ISBN": libro['ISBN'],
                            "Titulo": libro['Titulo'],
                            "ID Usuario": id_usuario,
                            "Cantidad Devuelta": cantidad_a_devolver,
                            "Motivo": motivo,
                            "Fecha de Devolución": datetime.datetime.now()
                        })
 
                        print(Fore.GREEN + f"Se han devuelto {cantidad_a_devolver} copias del libro '{libro['Titulo']}' por el usuario {id_usuario}.") # le mostramos al usuario o al admin las cantidades, el nombre del libro y el usuario que lo devolvio
                        break
                except ValueError: # Manejamos la excepcion por si registra alguna con decimales
                    print(Fore.RED + "Error: La cantidad debe ser un número entero.")
            break  
 
    if not libro_encontrado:
        print(Fore.RED + "=== Libro no encontrado ===")
 

def mostrar_historial_devoluciones():
    if not historial_devoluciones:
        print(Fore.RED + "No hay devoluciones registradas.")
        return
 
    print(Fore.GREEN + "==== Historial de libros devueltos ==== ")
 
    for registro in historial_devoluciones:
        print(
            f"ISBN: {registro['ISBN']} - "
            f"Titulo: {registro['Titulo']} - "
            f"ID Usuario: {registro['ID Usuario']} - "
            f"Cantidad Devuelta: {registro['Cantidad Devuelta']} - "
            f"Motivo: {registro['Motivo']} - "
            f"Fecha de Devolución: {registro['Fecha de Devolución']}"
        )


def elegir_opcion():
    while True: # Bucle para que se muestre siempre hasta que elijan una opción
        print(Fore.CYAN + "== Menú de devolucion de libro ==")
        print("1. Devolver libro")
        print("2. Historial de devolucion")
        print("3. Regresar al menú principal")
        opcion = input(Fore.YELLOW +"Elige una opción: ")
 
        if opcion == "1":
            devolver_libro()
        elif opcion == "2":
            mostrar_historial_devoluciones()
        elif opcion == "3":
            main.menu_principal()
            break
        else:
            print("Opción no válida")