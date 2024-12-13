#Libreria
import matplotlib.pyplot as plt

#Datos
years=[2019,2020,2021,2022]
sales_a=[14,18,23,32]
sales_b=[11,12,26,32]

#Configurar las caracteristicas del grafico
plt.plot(years,sales_a,color='blue',linewidth=3,label='EMPRESA A')
plt.plot(years,sales_b,color='red',linewidth=3,label='EMPRESA B')

#Definir titulo y nombre de ejes
plt.title("DIAGRAMA DE LINEA")
plt.ylabel('Sales')
plt.xlabel('Years')
plt.xticks(years)

#Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()