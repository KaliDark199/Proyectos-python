import tkinter as tk
import os
import threading
import time   
from plyer import notification


#primero creamos la ventana
window = tk.Tk()
window.title("bloqueo de páginas web y aplicaciones")
window.geometry("460x460")

#asignamos un "controlador"
ejecutar = True

#obtenemos las respuestas de la ventana creada:
def obtener_respuestas_páginas_web():
    respuesta_web = texto_páginas_web.get("1.0", tk.END).strip()
    respuesta_web_separadas = respuesta_web.split()
    return respuesta_web_separadas

def obtener_respuestas_aplicaciones():
    respuesta_app = texto_aplicaciones.get("1.0", tk.END).strip()
    respuestas_app_separadas = respuesta_app.split()
    return respuestas_app_separadas

#obtenemos el tiempo que la persona desea estar concentrada en sus trabajos:
def obtener_tiempo():
    respuesta_tiempo = tiempo_deseado.get()
    respuesta_tiempo = int(respuesta_tiempo)
    return respuesta_tiempo
    

# en este punto haremos la función para bloquear páginas web
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


#analizar los elementos que ya hay en el host_path y ver si agregamos o no hacemos nada:

def copia_del_host(host_path):
    with open (host_path, 'r') as f:
        contenido = f.read()
        return contenido


contenido_inicial = copia_del_host(host_path)

#función que devuelve todo a su lugar o estado principal:
def reiniciar():
    with open (host_path, "w") as f:
        f.write(contenido_inicial)

def bloq_page():
    while ejecutar:
            while page_web not in obtener_respuestas_aplicaciones():
                with open (host_path, "r+") as f:
                    content = f.read()
                    f.seek(0,2)
                    for page_web in obtener_respuestas_páginas_web():
                        if page_web not in content:
                            f.write( f"\n{redirect} {page_web}")
                            return controlador
                        else:
                            return controlador
    
    reiniciar()

#Aquía haremos el bloqueador de aplicaciones
def bloq_apps():
    while ejecutar:
        for app in obtener_respuestas_aplicaciones():
            os.system(f"taskkill /f /im {app}.exe >nul 2>&1")
        time.sleep(2)

#En esta parte haremos la confirmación de que las dos primeras dos funciones se ejecutaron

# en está parte está el momento en la cuál apareze la primera notificación  mi app
def notificar_inicio():
        notification.notify(
            title = "Iniciación",
            message = "Durante este tiempo no podrás usar las aplicaciones y páginas web eligidas",
            )   

def notificar_final():
    notification.notify(
        title = "Finalización",
        message = "A terminado la cantidad de tiempo que elegiste para concentrarte, así que relajate toma aguita  y se feliz :)",
    )



#en esta parte realizaremos el cronometro:

def cronometro(respuesta_tiempo):
    obtener_tiempo()
    global ejecutar
    notificar_inicio()
    time.sleep(respuesta_tiempo * 60)
    ejecutar = False
    notificar_final()

    

#activamos la ventana y también le damos la opción para poder obtener los datos:

texto_páginas_web = tk.Text(window, height=20, width=50)
texto_páginas_web.pack(padx=10, pady=5)

texto_aplicaciones = tk.Text(window, height=20, width=50)
texto_aplicaciones.pack(padx=10, pady=10)


boton_enviar_web = tk.Button(window, text="enviar las páginas web",
                         command= obtener_respuestas_páginas_web)
boton_enviar_web.pack(padx=10, pady=5)

boton_enviar_apps = tk.Button(window, text="enviar las apps", command=obtener_respuestas_aplicaciones)

tiempo_deseado = tk.Entry(window)
boton_enviar_tiempo = tk.Button(window, text="enviar el tiempo deseado", 
                                command=obtener_tiempo)

#en este punto activamos todos los hilos a usar:
threading1 = threading.Thread(target=bloq_page, daemon=True)
threading2 = threading.Thread(target=bloq_apps, daemon=True)
threading3 = threading.Thread(target=cronometro, args = (obtener_tiempo(), ))
threading1.start()
threading2.start()
threading3.start()


window.mainloop()

# threading1.join()
# threading2.join()
# threading3.join()