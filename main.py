# Modulo principal para la logica del programa

from menu import autenticar_usuario
from menu import menu_dispositivos_01
from log_in import log_in
from automatizacion import configurar_hora_apagon


print("Bienvenido a la casa intelignete del 'grupo 6'")

log_in()


def main():
    usuarios = []
    dispositivos = []

    while True:
        print("\n=== Casa Inteligente - Menu Principal ===")
        print("1. Gestionar usuarios")
        print("2. Gestionar dispositivos")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            autenticar_usuario(usuarios)
        elif opcion == "2":
            configurar_hora_apagon()
            menu_dispositivos_01(dispositivos)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("La opcion no valida. Intente nuevamente.")
    



if __name__ == "__main__":
    main()
