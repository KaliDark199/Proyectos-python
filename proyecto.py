import tkinter as tk
 

#primero creare la ventana:
ventana  = tk.Tk()
ventana.title("trolear")
label = tk.Label(ventana, text="puto el que lo lea")
label.config(font=("Arial", 50),  fg="white", background="black", )
label2 = tk.Label(ventana, text="yo se que tu ya lo leíste", font=("Arial", 30), fg="white", bg="black")

ventana.config(background="black")
label.pack()
label2.pack()


ventana.mainloop()