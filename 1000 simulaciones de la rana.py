import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import ttk
import time

ventana = tk.Tk()
tv = ttk.Treeview(ventana, columns=("col1","col2","col3"))
# Crear tabla de informacion de las simulaciones
tv.column("#0",width=40)
tv.column("col1",width=80, anchor="center")
tv.column("col2",width=80, anchor="center")
tv.column("col3",width=80, anchor="center")

tv.heading("#0", text="#", anchor="center")
tv.heading("col1", text="Saltos", anchor="center")
tv.heading("col2", text="posicion final", anchor="center")
tv.heading("col3", text="tiempo(Ms)", anchor="center")
iteracion = 0
prosiciones_finales = []

def simular():
    
    inicio = time.time()
    
    posicion_actual = 0
    saltos_realizados = 0
    posiciones_frecuentes = {0: 1}

    for i in range(1000):
        # Generar un número aleatorio entre 0 y 1
        salto = random.randint(0, 1)

        # Si el número es 0, la rana salta hacia atrás
        if salto == 0:
            posicion_actual -= 1
        # Si el número es 1, la rana salta hacia adelante
        else:
            posicion_actual += 1

        # Incrementar el número de saltos realizados
        saltos_realizados += 1

        # Actualizar la frecuencia de las diferentes posiciones alcanzadas por la rana
        if posicion_actual in posiciones_frecuentes:
            posiciones_frecuentes[posicion_actual] += 1
        else:
            posiciones_frecuentes[posicion_actual] = 1

    fin = time.time()
    
    # Añadir las posiciones finales a la lista
    prosiciones_finales.append(posicion_actual)
    
    global iteracion
    iteracion += 1 
    tiempo_ejecucion = (fin - inicio)*1000
    
    tv.insert("","end",text=iteracion, values=("1.000",posicion_actual,tiempo_ejecucion))
    tv.grid(row=2, column=2)

# Cerrar ventana
def cerrar():
    plt.close(fig2)
    ventana.destroy()

# Crear la ventana
ventana.title("Simulación de la rana")
ventana.protocol("WM_DELETE_WINDOW", cerrar)

for i in range(1000):
    simular()

# Crear grafico de posiciones finales de la rana
fig2, ax2 = plt.subplots()
ax2.hist(prosiciones_finales)
ax2.set_xlabel('Posición')
ax2.set_ylabel('Frecuencia')
ax2.set_title('Frecuencia de las posiciones finales de la rana')
    
#mostrar grafica
fig2.set_size_inches(6, 4)
canvas2 = FigureCanvasTkAgg(fig2, master=ventana)
canvas2.draw()
canvas2.get_tk_widget().grid(row=1, column=2)

# Ejecutar la ventana
ventana.mainloop()
