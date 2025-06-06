# Modulo principal para la logica del programa

from menu import autenticar_usuario
from menu import menu_dispositivos_01


from automatizacion import automatizacion


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
            menu_dispositivos_01(dispositivos)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("La opcion no valida. Intente nuevamente.")

    automatizacion()


if __name__ == "__main__":
    main()
