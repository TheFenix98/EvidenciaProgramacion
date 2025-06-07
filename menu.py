# Aqui dejamos el menu

from usuarios import menu_usuarios, registrar_usuario
from dispositivos import menu_dispositivos_admin, menu_dispositivos_usuarios


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


def menu_dispositivos_01(dispositivos):
    nombre = input("ingrese su nombre de usuario: ")
    if nombre.lower() == "admin":
        print("acceso al menu de administrador")
        menu_dispositivos_admin(dispositivos)
    else:
        print("accediendo a la gestion de dispositivos")
        menu_dispositivos_usuarios(dispositivos)
