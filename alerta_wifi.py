import os
import tkinter as TK
import time
import threading

window = TK.Tk()
window.title("wifi de 5to C")
window.config(background="black")
label = TK.Label (window, text="No deberías de aberte conecto a  la red de 5to C")
label.config(font=("Arial", 34), fg="red", bg="black")
label.pack()

def apagar_máquina():
    time.sleep(6)
    os.system("shutdown /s /t 1")

hilo1 = threading.Thread(target=apagar_máquina)
hilo1.start()
window.mainloop()