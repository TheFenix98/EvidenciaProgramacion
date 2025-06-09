# Modulo principal para la logica del programa


from menu import autenticar_rol_usuario
from log_in import log_in
from automatizacion import configurar_hora_apagon

def main():
    usuarios = []
    dispositivos = []

    print("Bienvenido a la casa inteligente del 'grupo 6'")

    infoUsuario = log_in()

    while True:
        print("\n=== Casa Inteligente - Menú Principal ===")
        print("1. Gestionar usuarios")
        print("2. Gestionar dispositivos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "3":
            print("Saliendo del programa.")
            break

        autenticar_rol_usuario(infoUsuario, usuarios, dispositivos, opcion)

if __name__ == "__main__":
    main()
