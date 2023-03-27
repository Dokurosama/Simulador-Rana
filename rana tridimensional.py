import random
import math
import time
import tkinter as tk
import matplotlib.pyplot as plt

tiempos=[]
resultados = []

# Función que simula una caminata aleatoria
def caminata_aleatoria():
    x = 0
    y = 0
    z = 0
    saltos = 0
    inicio = time.time()
    while (x, y, z) != (45,23,17):
        direccion = random.choice(['+y', '-y', '+x', '-x','+z','-z'])
        if direccion == '+y':
            y += 1
        elif direccion == '-y':
            y -= 1
        elif direccion == '+x':
            x += 1
        elif direccion == '-x':
            x -= 1
        elif direccion == '+z':
            z += 1
        else:
            z -= 1
        saltos += 1
        if(time.time()-inicio>0.001):
            print(x,",",y,",",z)
            return 0
    print("llegue a las coordenadas")
    tiempos.append(time.time()-inicio)
    resultados.append(saltos)
    return saltos

num_simulaciones = 2
saltos_totales = 0

while len(tiempos)!=num_simulaciones:
    saltos_totales += caminata_aleatoria()
    

saltos_promedio = saltos_totales / num_simulaciones
tiempo_promedio = sum(tiempos) / len(tiempos)

# Crear ventana
ventana = tk.Tk()
ventana.title("Resultados de la simulación")

# Etiquetas con los resultados
etiqueta_saltos = tk.Label(ventana, text=f"La cantidad de saltos promedio para llegar a la coordenada (45,23,17) es: {saltos_promedio}")
etiqueta_saltos.pack()

etiqueta_tiempo = tk.Label(ventana, text=f"El tiempo promedio que le tomó a la simulación es: {tiempo_promedio}")
etiqueta_tiempo.pack()

etiqueta_resultados = tk.Label(ventana, text=f"Resultados de las simulaciones: {resultados}")
etiqueta_resultados.pack()

plt.hist(resultados)
plt.title("Grafica de numero de saltos para llegar a las coordenadas")
plt.xlabel("Numero de saltos")
plt.ylabel("Frecuencia")
plt.show()

ventana.mainloop()