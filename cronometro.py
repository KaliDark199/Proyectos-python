import time
import pygame
from plyer import notification


pygame.init()
pygame.mixer.init()
musica = pygame.mixer.Sound("musica1.mp3")

time_elegido = int(input("elige la cantidad de tiempo que deseas que tenga el cronometro: "))
tiempo = time_elegido * 60

def cronometro(tiempo, time_elegido):

    notification.notify (
    title = "comienza el tiempo",
    message = f"tienes {time_elegido} minutos para hacer tus actividades",
    timeout = 20,
    )
    
    time.sleep(tiempo)
    notification.notify(
        title = "Es momento de empezar la siguiente actividad ",
        message = f"han pasado ya los {time_elegido} minutos",
        timeout= 20,
    )
    musica.play()

cronometro(tiempo, time_elegido)

respuesta = str(input("poner si si desea que se detenga la música: "))

if respuesta.lower() == "si":  
    musica.stop()
    print("música detenida")
else: 
    return "bien por ti"



    

