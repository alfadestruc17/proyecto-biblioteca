import colorama
from colorama import Fore

crear_usuarios = []

def crear_usuario():
    while True:
        id_usuario = input(Fore.GREEN + "Ingrese el ID del usuario (últimos 3 dígitos de su documento de identidad): ")
       
        if any(usuario['ID'] == id_usuario for usuario in crear_usuarios): #verificar que no exista ya un usuario registrado con ese ID
            print(Fore.RED + "Error: El ID ya está registrado. Ingrese un ID diferente.")
            continue
       
        if id_usuario.isdigit() and len(id_usuario) == 3:
            break
        else:
            print(Fore.RED + "Error: El ID deben ser los últimos 3 números del documento de identidad. Inténtelo de nuevo.")
 
    while True:
        nombre = input(Fore.GREEN + "Ingrese el nombre del usuario: ")
        if nombre.replace(" ", "").isalpha():  #verificar que solo sean letras lo que ingresa en el nombre
            break
        else:
            print(Fore.RED + "Error: El nombre solo debe contener letras. Inténtelo de nuevo.")
   
    while True:
        rol = input(Fore.GREEN + "Ingrese el rol del usuario: ")
        if rol.replace(" ", "").isalpha():  
            break
        else:
            print(Fore.RED + "Error: El rol solo debe contener letras. Inténtelo de nuevo.")
   
    #guardamos los datos en un diccionario, donde se guardara toda la informacion registrada
    usuario = {
        "ID": id_usuario,
        "nombre": nombre,
        "Rol": rol,
    }
    crear_usuarios.append(usuario)
    print(Fore.RED + "====== USUARIO GUARDADO EXITOSAMENTE =====")
 
 
 
    pass  # Implementar la función

def mostrar_usuario():
        # verificar si existen usuarios registrados
    if not crear_usuarios:
        print(Fore.RED + "=== No hay ningún usuario registrado ==== ")
    else:
        print(Fore.CYAN + "==== Lista de usuarios ====")
        for i, usuario in enumerate(crear_usuarios, 1):
            print(f"{i}. ID: {usuario['ID']} -  NOMBRE: {usuario['nombre']}    - ROL: {usuario['Rol']}")
        print()
    pass  # Implementar la función

def actualizar_usuario():
     # Verifica si hay usuarios registrados
    if len(crear_usuarios) == 0:
        print(Fore.RED + "=== No hay usuarios registrados ===")
        return
 
    # Solicita el ID del usuario que se desea actualizar
    id = input(Fore.GREEN + "Ingrese el ID del usuario que desea actualizar: ")
    usuario_encontrado = False  # Bandera para saber si se encontró el usuario
 
    # Recorre la lista de usuarios para encontrar el ID ingresado
    for usuario in crear_usuarios:
        if usuario['ID'] == id:
            print("=== Usuario encontrado ===")
 
            # Bucle para solicitar un nuevo nombre y validar que solo contenga letras
            while True:
                nuevo_nombre = input(Fore.GREEN + "Nuevo nombre (o Enter para dejar el actual): ").strip()
                if nuevo_nombre == "" or nuevo_nombre.isalpha():  # Permite solo letras o dejar el actual
                    usuario['nombre'] = nuevo_nombre or usuario['nombre']
                    break
                else:
                    print(Fore.RED + "Error: El nombre solo debe contener letras. Inténtelo de nuevo.")
 
            # Bucle para solicitar un nuevo rol y validar que solo contenga letras
            while True:
                nuevo_rol = input(Fore.GREEN + "Nuevo rol (o Enter para dejar el actual): ").strip()
                if nuevo_rol == "" or nuevo_rol.isalpha():  # Permite solo letras o dejar el actual
                    usuario['Rol'] = nuevo_rol or usuario['Rol']
                    break
                else:
                    print(Fore.RED + "Error: El rol solo debe contener letras. Inténtelo de nuevo.")
 
            print(Fore.RED + "====== USUARIO ACTUALIZADO EXITOSAMENTE =====")
            usuario_encontrado = True  # Se marca que el usuario fue encontrado
            break
 
    # Si el ID ingresado no corresponde a ningún usuario, se notifica al usuario
    if not usuario_encontrado:
        print(Fore.RED + "=== Usuario no encontrado ===")
    pass  # Implementar la función

def eliminar_usuario():
     # Verifica si hay usuarios registrados
    if len(crear_usuarios) == 0:
        print(Fore.RED + "=== No hay usuarios registrados ===")
        return  # Sale de la función si no hay usuarios registrados
   
    # Solicita el ID del usuario que se desea eliminar
    id = input(Fore.GREEN + "Ingrese el ID del usuario que desea eliminar: ")
    usuario_encontrado = False  # Bandera para saber si se encontró el usuario
   
    # Recorre la lista de usuarios para buscar el ID ingresado
    for usuario in crear_usuarios:
        if usuario['ID'] == id:
            crear_usuarios.remove(usuario)  # Elimina el usuario si se encuentra
            print(Fore.RED + "====== USUARIO ELIMINADO EXITOSAMENTE =====")
            usuario_encontrado = True  # Cambia la bandera si el usuario es encontrado
            break  # Termina el bucle al encontrar el usuario
   
    # Si no se encuentra el usuario, muestra un mensaje de error
    if not usuario_encontrado:
        print(Fore.RED + "=== Usuario no encontrado === ")
    pass  # Implementar la función

def menu_usuarios():
    while True:
        print(Fore.CYAN + "===== Menú de Usuarios =====")
        print("1. Crear usuario")
        print("2. Mostrar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Regresar al menú principal")
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            mostrar_usuario()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
