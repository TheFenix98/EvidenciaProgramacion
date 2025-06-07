# Aqui dejamos el menu

from usuarios import menu_usuarios, registrar_usuario


def autenticar_usuario(lista_usuarios):
    nombre = input("Ingrese su nombre de usuario: ").strip()

    if nombre.lower() == "admin":
        print("Bienvenido administrador.")
        menu_usuarios(lista_usuarios)
    else:
        print(f"Usuario '{nombre}' no es administrador.")
        respuesta = input(
            "¿Desea registrarse como usuario? (s/n): ").strip().lower()
        if respuesta == "s":
            registrar_usuario(lista_usuarios)
        else:
            print("Acceso denegado.")


def menu_dispositivos(dispositivos):
    print("Gestion de dispositivos no implementada todavia.")
