#se hara una aplicación que me ayudara a concentrarme en mis actividades diarias:
#para que pase sierta cnatidad de tiempo en base a las tareas y el tiempo
import time
#para que me aparezcan las notificaciones
from plyer import notification
import pygame



#pasos: 
#0. generar a los controlaldores  y el diccionario dondde se almacenara todo así como las funciones principales y incializamos pygame para la música 
tareas_tiempo = {}
ejecutar = True

pygame.init()
pygame.mixer.init()
music = pygame.mixer.music.load("música.mp3")

def convertir_a_segundos(number, word):
    number = int(number)
    word = str(word).lower()
    if word == "hours" or word == "hour":
        tiempos = number * 3600
        return tiempos
    elif word == "minutes" or word == "minute":
        tiempos = number * 60
        return tiempos
    else: 
        tiempos = number 
        return tiempos



#para hacer que suceda varias veces
while ejecutar:

    # 1. Pedir la tarea a realizar
    tareas = input("que tarea vas a realizar?:  ")

    #2. Pedir el tiempo que se va a realizar la tarea
    tiempos = input("Cuaanto tiempo te va a llevar? (hour, minutes, seconds):  ").strip()
   
    #3. Hacer que esto se repita hasta que el usuario quiera (cuando diga ya es cuando se sale de todo)

    if tareas.lower() == "ya" or tiempos.lower() == "ya":
            break
    else:
        pass
                

    tiempos = tiempos.split()
    number, word = tiempos
    tiempos = convertir_a_segundos(number, word)


    #4. Guardar las tareas y el tiempo en el diccionario
    tareas_tiempo[tareas]=tiempos



#haremos la función para transformar a laptops de 20 minutes 


# 5. Una vez tengamos las tareas y el tiempo hacer que esta ocurra sierta cantidad de tiempo considerando los descansos oculares de 20 segudos cada 20 minutos:
for tareas, tiempo in tareas_tiempo.items():
    notification.notify(
         title = f"Comenzemos con la tarea: {tareas}",
         message = f"tienes un tiempo de {tiempo} segundos para realizar esta tareas",
         timeout = 15,
    )
    match tiempo:
         case 0:
              pass
         case _ if tiempo < 1200:
              notification.notify(
                   title = f"Comenzemos con la tarea: {tareas}",
                   message = f"tienes un total de {tiempo} segundos para realizar esta tarea",
                   timeout = 15,
              )
              time.sleep(int(tiempo))
         case 1200:
              notification.notify(
                   title = f"Comenzemos con la tarea: {tareas}",
                   message = f"tienes un total de {tiempo} segundos para realizar esta tarea",
                   timeout = 15,
              )
              time.sleep(int(tiempo))
              notification.notify(
                   title = "Descanso",
                   message = "toma un descanso de 5 minutos",
                   timeout = 15,
              )
              time.sleep(int(300))
         case _ if tiempo > 1200:
                cantidad_de_intervalos = tiempo /1200
                cantidad_adicional = tiempo % 1200
                for n in range (int(cantidad_de_intervalos)):
                    time.sleep(int(1200))
                    notification.notify(
                        title= f"Empieza a hacer: {tareas}",
                        message = f"tienes un total de {cantidad_de_intervalos} intervalos de 20 minutos para realizar esta tarea",
                        timeout= 15,
                       )
                    time.sleep(int(1200))
                    notification.notify(
                        title = "Descanso ocular",
                        message  = "toma un descanso de 20 segundos para descansar la vista",
                        timeout = 15,
                    )
                    time.sleep(int(20))
                    music.play()
                    music.fadeout(5000)
                    notification.notify(
                        title = f"vuelve a la tarea: {tareas}",
                        message = f"te queda {cantidad_de_intervalos- n+1} de intervalos de 20 minutos"
                     )
                    music.play()
                    music.fadeout(5000)
                notification.notify(
                     title = "Felicidades",
                     message= f"felicidad solamente te faltan {cantidad_adicional} segundos para terminar la tarea",
                     timeout = 15,
                )
                time.slep(int(cantidad_adicional))
                notification.notify(
                     title = "Felicidades",
                     message = f"terminaste la tarea {tareas}, descansa 5 minutos",
                     timeout = 15,
                )
                time.sleep(int(300))







