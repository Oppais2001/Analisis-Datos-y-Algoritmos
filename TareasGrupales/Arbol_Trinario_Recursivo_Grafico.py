import tkinter as tk
from Arbol_Trinario_Recursivo import*

# Crear la ventana principal
ventana = tk.Tk()
ventana.state('zoomed')
ventana.title("Árbol Trinario Recursivo")
ventana.update()
ancho = ventana.winfo_width()
alto = ventana.winfo_height()
print(ancho, alto)
vh = alto / 10
vw = ancho / 10


class Aplicacion:
    def __init__(self, ventana):

        self.arbol = ArbolTrinarioRecursivo()

        self.etiqueta = tk.Label(ventana, text="Ingresa un valor:",font=("Bahnschrift", 25))
        self.etiqueta.place(x = 680, y = 10)

        self.caja_texto = tk.Entry(ventana, width=10, font=("Bahnschrift", 20))
        self.caja_texto.place(x = 720, y = 60)

        self.boton_insertar = tk.Button(ventana, text="Insertar", command=self.insertar_numero, bg="red", fg="white",font=("Bahnschrift", 12))
        self.boton_insertar.place(x = 720, y = 110)

        self.boton_insertar = tk.Button(ventana, text="Eliminar", command=self.eliminar_numero, bg="blue", fg="white",font=("Bahnschrift", 12))
        self.boton_insertar.place(x = 800, y = 110)

        self.canvas = tk.Canvas(ventana, width=ancho, height=alto)
        self.canvas.place(x = 25, y = 150)


    def insertar_numero(self):
        try:
            numero = int(self.caja_texto.get())
            self.arbol.insertar(numero)
            self.dibujar_arbol()
        except ValueError:
            print("Error: Ingrese un número válido.")

    def eliminar_numero(self):
        try:
            numero = int(self.caja_texto.get())
            self.arbol._eliminar_valor(numero, self.arbol.raiz)
            print(self.arbol.__str__())
            self.dibujar_arbol()
        except ValueError:
            print("Error: Ingrese un número válido.")

    def dibujar_arbol(self):
        self.canvas.delete("all")
        self.dibujar_nodo(self.arbol.raiz, ancho/2, 50, 150)

    def dibujar_nodo(self, nodo, x, y, espacio):
        if nodo:
            # Dibujar el nodo
            self.canvas.create_oval(x-(vh/5), y-(vh/5), x+(vh/5), y+(vh/5), fill="white")
            self.canvas.create_text(x, y, text=str(nodo.valor), font=("Helvetica", 15))
            # Dibujar las líneas hacia los hijos
            if nodo.izquierda:
                self.canvas.create_line(x-(vh/5), y+(vh/12), x-espacio, y+(vh/3))
                self.dibujar_nodo(nodo.izquierda, x-espacio, y+(vh/3), espacio*0.8)
            if nodo.medio:
                self.canvas.create_line(x, y+(vh/5), x, y+(vh/2))
                self.dibujar_nodo(nodo.medio, x, y+(vh/2), espacio*0.8)
            if nodo.derecha:
                self.canvas.create_line(x+(vh/5), y+(vh/12), x+espacio, y+(vh/3))
                self.dibujar_nodo(nodo.derecha, x+espacio, y+(vh/3), espacio*0.8)

# Crear la aplicación
app = Aplicacion(ventana)

# Ejecutar la aplicación
ventana.mainloop()
