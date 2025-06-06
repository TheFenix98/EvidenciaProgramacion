# módulo principal
from datetime import datetime, time


def main():
    usuarios = []
    dispositivos = []

    while True:
        print("\n=== Casa Inteligente - Menú Principal ===")
        print("1. Gestionar usuarios")
        print("2. Gestionar dispositivos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios(usuarios)
        elif opcion == "2":
            menu_dispositivos(dispositivos)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

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
            print("Opción no válida. Intente nuevamente.")


def registrar_usuario(lista_usuarios):
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")
    rol = input("Ingrese el rol del usuario (admin/invitado/etc.): ")

    usuario = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }

    lista_usuarios.append(usuario)
    print("Usuario registrado exitosamente.")


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
        "Ingrese el nombre del dusuario que desea buscar: ")

    for usuario in lista_usuarios:
        if usuario["nombre"].lower() == nombre_buscar.lower():
            print(
                f"usuario encontrado:  Nombre: {usuario['nombre']}, Email: {usuario['email']}, Rol: {usuario['rol']}")
            return

    print("usuario no encontrado.")


def eliminar_usuario(lista_usuarios):
    usuario_a_eliminar = input(
        "Ingrese el nombre del usuario que quiere eliminar: ")

    for usuario in lista_usuarios:
        if usuario["nombre"].lower() == usuario_a_eliminar.lower():
            lista_usuarios.remove(usuario)
            print("Usuario eliminado exitosamente.")
            return

    print("Usuario no encontrado.")

# Submenú de gestión de dispositivos


def menu_dispositivos(lista_dispositivos):

    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Eliminar dispositivo")
        print("4. buscar dispositivo")
        print("5. volver a menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_dispositivo(lista_dispositivos)
        elif opcion == "2":
            automatizacion(lista_dispositivos)
            listar_dispositivos(lista_dispositivos)
        elif opcion == "3":
            eliminar_dispositivo(lista_dispositivos)
        elif opcion == "4":
            buscar_dispositivo(lista_dispositivos)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def agregar_dispositivo(lista_dispositivos):
    nombre = input("Ingrese el nombre del dispositivo: ")
    tipo = input(
        "Ingrese el tipo de dispositivo (luz, sensor, cámara, etc.): ")
    ubicacion = input("Ingrese la ubicación del dispositivo: ")
    estado = "encendido"

    dispositivo = {
        "nombre": nombre,
        "tipo": tipo,
        "ubicacion": ubicacion,
        "estado": estado
    }

    lista_dispositivos.append(dispositivo)
    print("Dispositivo agregado exitosamente.")


def listar_dispositivos(lista_dispositivos):
    if not lista_dispositivos:
        print("No hay dispositivos registrados.")
        return

    print("\n--- Lista de Dispositivos ---")
    for i, dispositivo in enumerate(lista_dispositivos, 1):
        print(
            f"{i}. Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")


def eliminar_dispositivo(lista_dispositivos):
    nombre_a_eliminar = input(
        "Ingrese el nombre del dispositivo que quiere eliminar: ")

    for dispositivo in lista_dispositivos:
        if dispositivo["nombre"].lower() == nombre_a_eliminar.lower():
            lista_dispositivos.remove(dispositivo)
            print("Dispositivo eliminado exitosamente.")
            return

    print("Dispositivo no encontrado.")


def buscar_dispositivo(lista_dispositivos):
    nombre_buscar = input(
        "Ingrese el nombre del dispositivo que desea buscar: ")

    for dispositivo in lista_dispositivos:
        if dispositivo["nombre"].lower() == nombre_buscar.lower():
            print(
                f"Dispositivo encontrado: Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
            return

    print("Dispositivo no encontrado.")


def automatizacion(lista_dispositivos):
    horaActual = horaActual = datetime.now().time()
    horaDeApagon = time(23, 00)

    if horaActual >= horaDeApagon:
        for dispositivo in lista_dispositivos:
            dispositivo["estado"] = "apagado"


# ejecución del programa
if __name__ == "__main__":
    main()
