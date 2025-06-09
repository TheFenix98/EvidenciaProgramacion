# Aqui dejamos el menu

from usuarios import menu_usuarios, registrar_usuario
from dispositivos import menu_dispositivos_admin, menu_dispositivos_usuarios
from log_in import log_in
# esto interpreta que el usuario tiene que tener como nombre "admin",
# y lo que nosostros queremos es que busque que rol tiene el usuario,
# y a partir de eso te tire los menus correspondientes a cada rol.

def autenticar_rol_usuario(infoUsuario, lista_usuarios, lista_dispositivos, opcion):
    if opcion == "1":
        if infoUsuario["rol"] == "admin":
            menu_usuarios(lista_usuarios)
        else:
            print("Acceso denegado: solo los administradores pueden gestionar usuarios.")
    elif opcion == "2":
        if infoUsuario["rol"] == "admin":
            menu_dispositivos_admin(lista_dispositivos)
        else:
            menu_dispositivos_usuarios(lista_dispositivos)
    else:
        print("Opción no válida en autenticación.")

