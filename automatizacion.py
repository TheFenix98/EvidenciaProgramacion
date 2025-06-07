# Le damos automatizacion a los dispositivos

from datetime import datetime, time

def automatizacion(lista_dispositivos):
    print("Informamos a los usuarios que el sistema Smart Home cuenta con un sistema de apagon automatico")
    print("Usted puede configurar el apagon a la hora que usted desee")
    
    horaUsuario= input("ingrese la hora a la que desea configurar seperando horas y minutos con ¨:¨ SIN ESPACIOS")
    partesHora= horaUsuario.split(":")
    hora= int(partesHora[0])
    minutos= int(partesHora[1])
    horaActual = datetime.now().time()
    horaDeApagon = time(hora, minutos)

    if horaActual >= horaDeApagon:
        for dispositivo in lista_dispositivos:
            dispositivo["estado"] = "apagado"