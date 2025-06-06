# Submenú de gestión de usuarios


def menu_usuarios(lista_usuarios):

    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Registrar nuevo usuario")
        print("2. Listar usuarios")
        print("3. buscar usuario")
        print("4. Eliminar usuario")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(lista_usuarios)
        elif opcion == "2":
            listar_usuarios(lista_usuarios)
        elif opcion == "3":
            buscar_usuarios(lista_usuarios)
        elif opcion == "4":
            eliminar_usuario(lista_usuarios)
        elif opcion == "5":
            break
        else:
            print("La opcion no es valida. Intente nuevamente.")


def registrar_usuario(lista_usuarios):
    nombre = input("Ingresa el nombre del usuario: ")
    email = input("Ingresa el email del usuario: ")
    rol = input("Ingresa el rol del usuario (admin/invitado/etc.): ")

    usuario = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }

    lista_usuarios.append(usuario)
    print("El usuario fue registrado exitosamente.")


def listar_usuarios(lista_usuarios):
    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n--- Lista de Usuarios ---")
    for i, usuario in enumerate(lista_usuarios, 1):
        print(
            f"{i}. Nombre: {usuario['nombre']}, Email: {usuario['email']}, Rol: {usuario['rol']}")


def buscar_usuarios(lista_usuarios):
    nombre_buscar = input(
        "Ingresa el nombre del usuario que desea buscar: ")

    for usuario in lista_usuarios:
        if usuario["nombre"].lower() == nombre_buscar.lower():
            print(
                f"usuario encontrado:  Nombre: {usuario['nombre']}, Email: {usuario['email']}, Rol: {usuario['rol']}")
            return

    print("usuario no encontrado.")


def eliminar_usuario(lista_usuarios):
    usuario_a_eliminar = input(
        "Ingresa el nombre del usuario que quiera eliminar: ")

    for usuario in lista_usuarios:
        if usuario["nombre"].lower() == usuario_a_eliminar.lower():
            lista_usuarios.remove(usuario)
            print("El usuario fue eliminado exitosamente.")
            return

    print("El usuario no fue encontrado.")