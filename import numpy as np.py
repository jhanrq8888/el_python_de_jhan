import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(2,1)
amplitud= 10
longOnda= 2
faseInicial= np.pi
frecuencia1=0.2
frecuencia2=0.4
x= np.arange(0,2*np.pi, 0.01)

linea1 = ax [0].plot(x, amplitud*np.sin(faseInicial+x*2*np.pi/longOnda+faseInicial))
linea2 = ax [1].plot(x, amplitud*np.sin(faseInicial+x*2*np.pi/longOnda+faseInicial))

def animacion(i):

    linea1[0].set_ydata(amplitud*np.sin(faseInicial+x*2*np.pi/longOnda+faseInicial+i*2*np.pi*frecuencia1))
    linea2[0].set_ydata(amplitud*np.sin(faseInicial+x*2*np.pi/longOnda+faseInicial+i*2*np.pi*frecuencia2))
    return linea1, linea2

ani = animation.FuncAnimation(fig, animacion, interval=100)
plt.show()