# Le damos automatizacion a los dispositivos

from datetime import datetime, time

hora_apagon_global = None  

def configurar_hora_apagon():
    global hora_apagon_global
    print("Informamos a los usuarios que el sistema Smart Home cuenta con un sistema de apagón automático.")
    print("Usted puede configurar el apagón a la hora que usted desee.")
    
    horaUsuario = input("Ingrese la hora de apagón (formato HH:MM, sin espacios): ")
    partesHora = horaUsuario.strip().split(":")
    hora = int(partesHora[0])
    minutos = int(partesHora[1])
    hora_apagon_global = time(hora, minutos)
    print(f"Hora de apagón configurada: {hora_apagon_global}")

def verificar_y_apagar(dispositivos):
    if hora_apagon_global is None:
        return  

    hora_actual = datetime.now().time()
    if hora_actual >= hora_apagon_global:
        for dispositivo in dispositivos:
            dispositivo["estado"] = "apagado"