from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
# Tipo de figura
ax = fig.gca(projection='3d')
# Datos
X = np.arange(-4, 4, 0.3)
Y = np.arange(-4, 4, 0.3)
#vectores de coordenadas
X, Y = np.meshgrid(X, Y)
#raiz cuadrada
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Graficamos o trazamos la superficie
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')
# Personalizamos el ejex z
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(8))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))

ax.set_xlabel('EJE X')
ax.set_ylabel('EJE Y')
ax.set_zlabel('EJE Z')

plt.title("GRAFICA 3D - FUNCIONES",font="bold")
plt.show()