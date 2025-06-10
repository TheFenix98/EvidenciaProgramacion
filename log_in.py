from base_datos_usuarios import usuarios_creados

def log_in():
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    infoUsuario = {"nombre": nombre, "contraseña": contraseña}  # Definir infoUsuario antes de return

    print(f"Bienvenido {nombre}")
    return infoUsuario


def log_in():
    acceso = "denegado"
    while acceso == "denegado":
        usuario_ingresado = input("ingrese su nombre de usuario: ")
        contraseña_ingresada = input("ingrese su contraseña: ")
        lista_de_usuarios = usuarios_creados()
        for user in lista_de_usuarios:
            if user["usuario"] == usuario_ingresado and user["clave"] == contraseña_ingresada:
                print(f"bienvenido {usuario_ingresado}")
            acceso = "permitido"
            return user
    if acceso == "denegado":
        print("usuario y/o contraseña incorrecta, vuelva a intentar")
