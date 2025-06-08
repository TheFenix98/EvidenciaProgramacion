from base_datos_usuarios import ususarios_creados


def log_in():
    acceso = "denegado"
    while acceso == "denegado":
        usuario_ingresado = input("ingraese su nombre de usuario: ")
        contraseña_ingresada = input("ingrese una contraseña: ")
        lista_de_usuarios = ususarios_creados()
        for user in lista_de_usuarios:
            if user["usuario"] == usuario_ingresado and user["clave"] == contraseña_ingresada:
                print(f"bienveneido {usuario_ingresado}")
                acceso = "permitido"
                break
        if acceso == "denegado":
            print("usuario y/o contraseña incorrecta, vuelva a intentar")
