# Le damos automatizacion a los dispositivos

from datetime import datetime, time

def automatizacion(lista_dispositivos):
    horaActual = datetime.now().time()
    horaDeApagon = time(23, 00)

    if horaActual >= horaDeApagon:
        for dispositivo in lista_dispositivos:
            dispositivo["estado"] = "apagado"