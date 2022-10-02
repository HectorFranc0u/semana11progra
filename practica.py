from cProfile import label
from PIL import Image, ImageTk
from tkinter import Button, Tk, Label, filedialog

#def mostrar():
 #   imagen = Image.open(r"C:\Users\Franco\Documents\projectos python\semana 10\3.jpg")
  #  imagen.show()

def cargar():
    archivo = filedialog.askopenfilename()
    foto2 = Image.open(archivo)
    reducida2 = foto2.resize((300,300), Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(reducida2)
    lb2.configure(image=render2)
    lb2.image=render2


ventana = Tk()
ventana.geometry("500x500")
imagen2= Image.open(r"C:\Users\Franco\Documents\projectos python\semana 10\2.png")
reducida = imagen2.resize((300,300), Image.Resampling.LANCZOS)
render = ImageTk.PhotoImage(reducida)
lb = Label(ventana, image=render)
bn = imagen2.convert("L")
bn.save("5.jpg")
bn.show()

lb2 = Label(ventana, image="")
btn2= Button(ventana, text="cargar foto", command=cargar)
#boton1 = Button(ventana, text="Mostrar Foto", command= mostrar)
#boton1.pack()
lb.pack()
lb2.pack()
btn2.pack()
ventana.mainloop()