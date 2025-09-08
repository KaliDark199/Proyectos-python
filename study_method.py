#se hara una aplicación que me ayudara a concentrarme en mis actividades diarias:
#para que pase sierta cnatidad de tiempo en base a las tareas y el tiempo
import time
#para que me aparezcan las notificaciones
from plyer import notification

#pasos: 
#0. generar a los controlaldores  y el diccionario dondde se almacenara todo
tareas_tiempo = {}
ejecutar = True

#para hacer que suceda varias veces
while ejecutar:

    # 1. Pedir la tarea a realizar
    tareas = input("que tarea vas a realizar?:  ")

    #2. Pedir el tiempo que se va a realizar la tarea
    tiempos = input("Cuaanto tiempo te va a llevar? (hour, minutes, seconds):  ")
    for number, word in tiempos:
            if word == "hours" or word == "hour":
                tiempos = number * 3600
                ejecutar = False
            elif word == "minutes" or word == "minute":
                tiempos = number * 60
                ejecutar = False

            else: 
                ejecutar = False
            
    

    #3. Guardar las tareas y el tiempo en el diccionario
    tareas_tiempo[tareas]=tiempos

    #4. Hacer que esto se repita hasta que el usuario quiera (cuando diga ya es cuando se sale de todo)
    if tareas.lower() == "ya" or tiempos.lower() == "ya":
        ejecutar = False
    else:
        continue

#5. Una vez tengamos las tareas y el tiempo hacer que esta ocurra sierta cantidad de tiempo considerando los descansos oculares de 20 segudos cada 20 minutos:
for tarea, tiempo in tareas_tiempo.items():
    if tiempo.lower() == "ya" or tarea.lower() == "ya":
        continue
    else:
        notification.notify(
            title = "Tarea", 
            message = f"Es hora de {tarea} durante {tiempo} pero agregandole 20 segundos entre 20 minutos para descanso ocular",
            timeout = 10
        )
        while tiempo > 0:
            if tiempo <= 24000:
                time.sleep(int(tiempo))
                tiempo = 0
            elif tiempo > 24000:
                cantidad_de_intervalos = tiempo/24000
                cantidad_adicional = tiempo % 24000
            else:
                pass
            for n in cantidad_de_intervalos:
                time.sleep(int(1200))
                notification.notify(
                    title = "Descanso ocular",
                    message = "toma un descanso de 20 segundos",
                    timeout = 10
                )
                time.sleep(int(20))
                notification.notify(
                    title = f"vuelve a la {tarea}"
                )
                tiempo = tiempo - 2400
        time.sleep(int(tiempo))
        notification.notify(
            title = "FELICIDADES",
            message = "terminaste la tarea sigue descansa 5 minutos"
            timeout =  10
        )
        time.sleep (int(300))







        # tiempos = 
        # cantidad_adicional = tiempo % (20*60)
        # time.sleep(int(1200))



        # notification.notify(
        #     title = "Descanso ocular",
        #     message = "toma un descanso de 20 segundos",
        #     timeout = 10
        # )




