import colorama
from colorama import Fore
import main
import prestamos
crear_libros = []
libros_eliminados = []  # Lista que almacenará los libros que han sido eliminados completamente
libros_eliminados_unidad = []  # Lista para registrar eliminaciones de unidades de libros
 
def crear_libro():
    # Bucle para pedir el ISBN y verificar que sea único y numérico
    while True:
        isbn = input(Fore.GREEN + "Ingrese el ISBN del libro (solo números): ")
 
        # Verifica si el ISBN contiene solo dígitos
        if not isbn.isdigit():
            print(Fore.RED + "Error: El ISBN debe contener solo números.")
            continue
 
        # Verifica si el ISBN ya existe en la lista de libros registrados
        isbn_duplicado = False
        for libro in crear_libros:
            if libro['ISBN'] == isbn:
                isbn_duplicado = True
                break
       
        if isbn_duplicado:
            print(Fore.RED + "Error: Este ISBN ya está registrado. Ingrese un ISBN diferente.")
        else:
            break
 
    # Bucle para verificar que el título no esté vacío
    while True:
        nombre_libro = input(Fore.GREEN + "Ingrese el nombre del libro o título: ")
        if nombre_libro.strip() == "":  # Verifica que no esté en blanco
            print(Fore.RED + "Error: El nombre del libro no puede estar en blanco.")
        else:
            break
 
    # Bucle para verificar que el autor no esté vacío
    while True:
        autor = input(Fore.GREEN + "Ingrese el nombre del autor del libro: ")
        if autor.replace(" ", "").isalpha():  #verificar que solo sean letras lo que ingresa en el nombre
            break
        else:
            print(Fore.RED + "Error: El nombre solo debe contener letras. Inténtelo de nuevo.")
 
 
    # Bucle para verificar que la editorial no esté vacía
    while True:
        editorial_libro = input(Fore.GREEN + "Ingrese la editorial del libro: ")
        if editorial_libro.strip() == "":  # Verifica que no esté en blanco
            print(Fore.RED + "Error: La editorial no puede estar en blanco.")
        else:
            break
 
    # Bucle para verificar que la cantidad ingresada sea válida y mayor a 0
    while True:
        try:
            cantidad_libros = int(input(Fore.GREEN + "Ingrese la cantidad de libros que va a registrar (debe ser mayor a 0): "))
            if cantidad_libros < 1:
                print(Fore.RED + "Error: La cantidad debe ser un número mayor o igual a 1.")
            else:
                break
        except ValueError:
            print(Fore.RED + "Error: Por favor ingrese un número válido (sin letras).")
 
    # Asigna la cantidad de libros disponibles
    libros_disponibles = cantidad_libros
 
    # Crea el diccionario del libro con todos los datos proporcionados
    libro = {
        "ISBN": isbn,
        "Titulo": nombre_libro,
        "Autor": autor,
        "Editorial": editorial_libro,
        "Libros_dispo": libros_disponibles,  # Cantidad de libros disponibles
        "cantidad": cantidad_libros  # Cantidad total de libros
    }
 
    # Agrega el libro a la lista de libros registrados
    crear_libros.append(libro)
 
    # Mensaje de confirmación
    print(Fore.RED + "====== LIBRO GUARDADO EXITOSAMENTE =====")
    pass  # Implementar la función

def mostrar_libro():
    if len(crear_libros) == 0: # Verificamos que si existan libros en el sistema
        print(Fore.RED + "=== No hay ningún libro registrado ==== ")
    else:
        print(Fore.CYAN + "==== Lista de libros ====")
        for i, libro in enumerate(crear_libros, 1):
            print(f"{i}. ISBN: {libro['ISBN']} - NOMBRE: {libro['Titulo']}  - AUTOR: {libro['Autor']}  - EDITORIAL: {libro['Editorial']}  - COPIAS: {libro['cantidad']} - ESTADO: {libro['Libros_dispo']} copias disponibles ") # Informacion de los libros que se le muestra al usuario
        print()
    pass  # Implementar la función

def actualizar_libro():
    # Se mostrará un mensaje al usuario en caso de que no hayan libros registrados en la lista "crear_libros"
    if len(crear_libros) == 0:
        print(Fore.RED + "=== No hay libros registrados ===")
        return
 
    mostrar_libro() # Se llama a la función "mostrar_libro" para mostrarle al usuario los libros que se han creado
   
    isbn = input(Fore.GREEN + "Ingrese el ISBN del libro que desea actualizar: ")
    libro_encontrado = False # Se inicializa una variable que verifica si el ISBN no se encuentra registrado con algún libro
 
    # Bucle para verificar si el libro se encuentra registrado en la lista "crear_libros"
    for libro in crear_libros:
        if libro['ISBN'] == isbn:
            print("=== Libro encontrado ===")  # Si el ISBN concuerda con alguno creado, se mostrará un mensaje indicando que el libro fue encontrado y dará paso a actualizar
 
            libro['Titulo'] = input(Fore.GREEN + "Nuevo título (o Enter para dejar el actual): ") or libro['Titulo']
           
            while True:
                nuevo_autor = str(input(Fore.GREEN + "Nuevo autor (o Enter para dejar el actual): ") or libro['Autor']) # Se crea una nueva variable para el nuevo autor
                libro['Autor'] = nuevo_autor # Se le asigna a la variable de autor la variable anterior, para que al momente de actualizarse, este tome el valor de la variable "nuevo_autor"
                if nuevo_autor.replace(" ", "").isalpha():  #verificar que solo sean letras lo que ingresa en el nombre
                    break
                else:
                    print(Fore.RED + "Error: El nombre solo debe contener letras. Inténtelo de nuevo.")
               
            libro['Editorial'] = input(Fore.GREEN + "Nueva editorial (o Enter para dejar la actual): ") or libro['Editorial']
 
            while True:
                nueva_cantidad = input(Fore.GREEN + "Nueva cantidad de libros (o enter para dejar la cantidad actual): ") or libro['cantidad']
                try: # Se utiliza el try para manejar las excepciones
                    nueva_cantidad = int(nueva_cantidad)  # Se crea una nueva variable para detenerminar la nueva cantidad de copias que tiene cada libro
 
                    # Verifica que la nueva cantidad ingresada sea mayor o igual a 0
                    if nueva_cantidad >= 0:
                        libro['cantidad'] = nueva_cantidad  # Se da un nuevo valor a la cantidad de copias, siendo la variable "nueva_cantidad" su nuevo valor cuando se actualiza
                        break
                    else:
                        print(Fore.RED + "La cantidad no puede ser menor a 0.")
                except ValueError:
                    print(Fore.RED + "Por favor, ingrese un número válido.")
           
            cantidad_prestamos = sum(p['Cantidad prestamo'] for p in prestamos.historial_prestamos if p['ISBN'] == libro['ISBN']) # Se realiza la suma de la cantidad de prestamos relacionadas con el ISBN en especifico, y se da una nueva variable llamada "p" que hace referencia a "prestamos"
            libro['Libros_dispo'] = libro['cantidad'] - cantidad_prestamos # Se actualiza la cantidad de libros disponibles, restando la cantidad de copias totales menos la variable "cantidad_prestamos"
 
            if libro['Libros_dispo'] < 0:  
                libro['Libros_dispo'] = 0 # Si la cantidad de libros disponibles resulta ser menor que 0, la nueva cantidad pasará a ser 0
 
            print(Fore.RED + "====== LIBRO ACTUALIZADO EXITOSAMENTE =====")
            libro_encontrado = True
            break
 
 
    if not libro_encontrado:
        print(Fore.RED + "=== Libro no encontrado ===")
    pass  # Implementar la función


def seleccionar_motivo():
    print(Fore.CYAN + " ===== Seleccione el motivo de eliminación =====")
    print("1. Desgaste")
    print("2. Obsoleto")
    print("3. Duplicación")
    print("4. Condiciones de conservación")
    opcion = input(Fore.YELLOW + "Seleccione una opción: ") # Aqui el usuario escoge la opción  

    motivos = {
        "1": "Desgaste",
        "2": "Obsoleto",                # Se crea una nueva lista    
        "3": "Duplicación",
        "4": "Condiciones de conservación"
    }
   
    return motivos.get(opcion, "Motivo no especificado") # Si se escoje una opción errónea aparece este mensaje
 

def cantidad_a_eliminar():
    mostrar_libro()  # Se llama esta función que imprime la lista de libros para ver que hay en la colección
    isbn = input(Fore.GREEN + "Ingrese el ISBN del libro del que desea eliminar copias: ")
 
    if not isbn.isdigit():  # aqui se verifica que el isbn contenga solo num
        print(Fore.RED + "Error: El ISBN debe contener solo números. Inténtelo de nuevo.")
        return
 
    libro_encontrado = False  # Se inicializa libro_encontrado en False para rastrear si el libro fue encontrado en la colección.
 # Se busca que el libro , en la función crear_libros
    for libro in crear_libros:  
        if libro['ISBN'] == isbn:
            libro_encontrado = True  
            cantidad_actual = libro['cantidad']    # Si el isbn es igual a el isbn encuentra el libro y se da la cantidad actual de este libro actual
           # Se solicita la cantidad de copias que desea eliminar
            while True:
                try:  # Se utiliza un bloque try/except para manejar la entrada del usuario.          
                    cantidad_a_eliminar = int(input("Ingrese la cantidad que desea eliminar: ")) # Ingresar numeros enteros
                    if cantidad_a_eliminar <= 0:  
                        print(Fore.RED + "Error: La cantidad debe ser mayor que 0.") # Si la cantidad es menor a cero sale un ERROR
                        continue
                    if cantidad_a_eliminar > cantidad_actual:    # Si la cantidad de libros es mayor a la actual saldrá ERROR y muestra cuantas hay en el sistema
                        print(Fore.RED + f"Error: No se puede eliminar {cantidad_a_eliminar}. Solo hay {cantidad_actual} disponibles.")
                    else: # Si la cantidad es válida de llama la función seleccionar motivo
                        motivo = seleccionar_motivo()  
                        libro['cantidad'] -= cantidad_a_eliminar  # Se reduce la cantidad de libro libro['cantidad'], La cantidad disponible también se actualiza.
                        libro['Libros_dispo'] = libro['cantidad']
                        print(Fore.GREEN + f"====== Se han eliminado {cantidad_a_eliminar} copias del libro por motivo: {motivo} ======") # Se imprime un mensaje de éxito con la cantidad eliminada y el motivo.  
                       
                   
                    libros_eliminados_unidad.append({
                    'ISBN': libro['ISBN'],                      # Se agrega un registro de la eliminación a la lista libros_eliminados_unidad.
                    'Titulo': libro['Titulo'],
                    'cantidad_eliminada': cantidad_a_eliminar
 
                    })  
                    if libro['cantidad'] == 0:  
                        libro['disponible'] = False     # Si la cantidad del libro llega a 0, se marca el libro como no disponible (libro['disponible']= false)
                    break  
                except ValueError:  
                    print(Fore.RED + "Error: La cantidad debe ser un número entero.")
           
            break  
   
    if not libro_encontrado:  
        print(Fore.RED + "=== Libro no encontrado === ")
   
    main.menu_principal()

def M_eliminar_libro():
    # Si crear_libros es igual a cero da el mensaje.
    if len(crear_libros) == 0:
        print(Fore.RED + "=== No hay libros registrados ===")
        return
    # Se pregunta que desea eliminar cantidad o el libro completo.
    print(Fore.CYAN + "=== ¿Qué desea eliminar? ===")
    print("1. Cantidad de libros")
    print("2. Libro completo")
    print("3. Regresar")
    opcion = input(Fore.YELLOW + "Seleccione una opción: ")
   # Cantidad_a_eliminar() para eliminar copias.
    if opcion == "1":
        cantidad_a_eliminar()  
   # Eliminar_libro() para eliminar un libro completo.
    elif opcion == "2":
        eliminar_libro()
    elif opcion == "3":
   # Se regresa al menú de libros.  
        menu_libros()  
   
    else:
        print(Fore.RED + "Opción no válida. Intente de nuevo.") # Si se coloca otro número o otra opción da este mensaje
 
    pass  # Implementar la función
# Función para elimianr libro completamente del sistema
def eliminar_libro():
   
    # Muestra la lista de libros registrados en el sistema
    mostrar_libro()
   
    # Solicita al usuario ingresar el ISBN del libro que desea eliminar
    isbn = input(Fore.GREEN + "Ingrese el ISBN del libro que desea eliminar: ")
    libro_encontrado = False  # Variable para marcar si el libro fue encontrado o no
   
    # Bucle que itera sobre la lista de libros para buscar el libro con el ISBN ingresado
    for libro in crear_libros:
        if libro['ISBN'] == isbn:  # Si el ISBN coincide con el del libro
            motivo = seleccionar_motivo()  # Llama a una función para seleccionar el motivo de eliminación
           
            # Agrega el libro eliminado a la lista de 'libros_eliminados' para llevar un historial
            libros_eliminados.append(libro)
 
            # Remueve el libro de la lista 'crear_libros' (libros disponibles en el sistema)
            crear_libros.remove(libro)
           
            # Muestra un mensaje confirmando la eliminación del libro e incluye el motivo de la eliminación
            print(Fore.RED + f"====== LIBRO ELIMINADO EXITOSAMENTE por motivo: {motivo} =====")
            libro_encontrado = True  # Marca que el libro fue encontrado y eliminado
            break  
   
    # Si no se encontró el libro con el ISBN proporcionado, muestra un mensaje de error
    if not libro_encontrado:
        print(Fore.RED + "=== Libro no encontrado ===")

def mostrar_libros_ell():
    # Verifica si la lista de libros está vacía, en caso de que no hay libros eliminados.
    if len(crear_libros) == 0:
        print(Fore.RED + "=== No hay libros eliminados ===")
        return  # Sale de la función si no hay libros eliminados.
 
    # Muestra el menú para que el usuario seleccione qué desea ver.
    print(Fore.CYAN + "=== ¿Qué desea ver? ===")
    print("1. Mostrar unidades de libros eliminados")
    print("2. Mostrar libros eliminados completamente")
    print("3. Regresar")
   
    # Solicita al usuario que elija una opción del menú.
    opcion = input(Fore.YELLOW + "Seleccione una opción: ")
 
    # Evalúa la opción ingresada por el usuario.
    if opcion == "1":
        mostrar_unidades_eliminadas()  # Llama a la función para mostrar unidades eliminadas.
    elif opcion == "2":
        mostrar_libros_eliminados()  # Llama a la función para mostrar libros eliminados completamente.
    elif opcion == "3":
        menu_libros()  # Regresa al menú principal de libros.
    else:
        # Si la opción ingresada no es válida, muestra un mensaje de error y pide intentar de nuevo.
        print(Fore.RED + "Opción no válida. Intente de nuevo.")
 
    pass  # Implementar la función

def mostrar_libros_eliminados():
    # Verifica si hay libros en la lista de libros eliminados
    if not libros_eliminados:
        print(Fore.RED + "==== No hay libros eliminados ====")
    else:
        # Muestra la lista de libros eliminados con detalles
        print(Fore.CYAN + "==== Lista de libros eliminados ====")
        for i, libro in enumerate(libros_eliminados, 1):
            print(f"{i}. ISBN: {libro['ISBN']} - NOMBRE: {libro['Titulo']} - AUTOR: {libro['Autor']} - EDITORIAL: {libro['Editorial']} - Copias Eliminadas: {libro['cantidad']}")
 
# Función para mostrar la cantidad de copias eliminadas del sistema
def mostrar_unidades_eliminadas():
    # Verifica si hay unidades eliminadas de algún libro
    if not libros_eliminados_unidad:
        print(Fore.RED + "=== No hay unidades de libros eliminadas ===")
    else:
        # Muestra la lista de unidades eliminadas con detalles
        print(Fore.CYAN + "==== Unidades de libros eliminadas ====")
        for i, eliminacion in enumerate(libros_eliminados_unidad, 1):
            print(Fore.GREEN + f"{i}. ISBN: {eliminacion['ISBN']} - Título: {eliminacion['Titulo']} - Cantidad eliminada: {eliminacion['cantidad_eliminada']}")
       
        # Calcula el total de unidades eliminadas sumando las cantidades eliminadas en cada registro
        total_eliminadas = sum([eliminacion['cantidad_eliminada'] for eliminacion in libros_eliminados_unidad])
        print(Fore.GREEN + f"Total de unidades eliminadas: {total_eliminadas}")
 
def menu_libros():
    while True:
        print(Fore.CYAN + "===== Menú de Libros =====")
        print("1. Crear libro")
        print("2. Mostrar libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Ver historial de eliminaciones")
        print("6. Regresar al menú principal")
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            mostrar_libro()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            M_eliminar_libro()
        elif opcion == "5":
            mostrar_libros_ell()
        elif opcion == "6":
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
