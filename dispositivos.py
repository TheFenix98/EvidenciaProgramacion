# Submenu de gestion de dispositivos

def menu_dispositivos(lista_dispositivos):

    while True:
        print("\n--- Gestion de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Eliminar dispositivo")
        print("4. Buscar dispositivo")
        print("5. volver a menú principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_dispositivo(lista_dispositivos)
        elif opcion == "2":
            listar_dispositivos(lista_dispositivos)
        elif opcion == "3":
            eliminar_dispositivo(lista_dispositivos)
        elif opcion == "4":
            buscar_dispositivo(lista_dispositivos)
        elif opcion == "5":
            break
        else:
            print("La opcion no es valida. Intente nuevamente.")


def agregar_dispositivo(lista_dispositivos):
    nombre = input("Ingresa el nombre del dispositivo: ")
    tipo = input(
        "Ingresa el tipo de dispositivo (luz, sensor, camara, etc.): ")
    ubicacion = input("Ingresa la ubicacion del dispositivo: ")
    estado = "encendido"

    dispositivo = {
        "nombre": nombre,
        "tipo": tipo,
        "ubicacion": ubicacion,
        "estado": estado
    }

    lista_dispositivos.append(dispositivo)
    print("El dispositivo fue agregado exitosamente.")


def listar_dispositivos(lista_dispositivos):
    if not lista_dispositivos:
        print("No hay dispositivos registrados.")
        return

    print("\n--- Lista de Dispositivos ---")
    for i, dispositivo in enumerate(lista_dispositivos, 1):
        print(
            f"{i}. Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicacion: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")


def eliminar_dispositivo(lista_dispositivos):
    nombre_a_eliminar = input(
        "Ingresa el nombre del dispositivo que quiera eliminar: ")

    for dispositivo in lista_dispositivos:
        if dispositivo["nombre"].lower() == nombre_a_eliminar.lower():
            lista_dispositivos.remove(dispositivo)
            print("El dispositivo fue eliminado exitosamente.")
            return

    print("Dispositivo no encontrado.")


def buscar_dispositivo(lista_dispositivos):
    nombre_buscar = input(
        "Ingresa el nombre del dispositivo que desea buscar: ")

    for dispositivo in lista_dispositivos:
        if dispositivo["nombre"].lower() == nombre_buscar.lower():
            print(
                f"Dispositivo encontrado: Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicacion: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
            return

    print("Dispositivo no encontrado.")