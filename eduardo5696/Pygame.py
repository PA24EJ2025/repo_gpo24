from tkinter import Tk, Canvas  
from PIL import Image, ImageTk
import os


imagen_ruta = r"C:\Users\Salas\Desktop\206768345.png"  

if not os.path.exists(imagen_ruta):
    raise FileNotFoundError(f"No se encontró la imagen en: {imagen_ruta}")


ventana = Tk()
ventana.title("Mover imagen con flechas")


canvas = Canvas(ventana, width=800, height=600)
canvas.pack()


imagen = Image.open(imagen_ruta)
imagen_tk = ImageTk.PhotoImage(imagen)


imagen_id = canvas.create_image(100, 100, anchor="nw", image=imagen_tk)


def mover_imagen(event):
    if event.keysym == "Up":
        canvas.move(imagen_id, 0, -10)
    elif event.keysym == "Down":
        canvas.move(imagen_id, 0, 10)
    elif event.keysym == "Left":
        canvas.move(imagen_id, -10, 0)
    elif event.keysym == "Right":
        canvas.move(imagen_id, 10, 0)


ventana.bind("<KeyPress-Up>", mover_imagen)
ventana.bind("<KeyPress-Down>", mover_imagen)
ventana.bind("<KeyPress-Left>", mover_imagen)
ventana.bind("<KeyPress-Right>", mover_imagen)


canvas.focus_set()


ventana.mainloop()
