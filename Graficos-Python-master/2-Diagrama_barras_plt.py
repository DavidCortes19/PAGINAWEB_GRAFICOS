#Libreria
import matplotlib.pyplot as plt

#Datos lenguajes de progrmacion mayor demandad 2022
porcentajes = [14,12,11,10,8]
lenguajes = ["Python", "C","Java", "C++", "C#"]

#configurar las cararteriticas de la grafica
#plt.barh(lenguajes, porcentajes, align="center",color="black",label="ENCUESTAS 2022 - BARRAS")
plt.bar(lenguajes,porcentajes,label="ENCUESTAS 2022",width=0.4,color="green")
#plt.plot(lenguajes,porcentajes,label="ENCUESTAS 2022 - LINEA", linewidth=0.5,color="blue")

#configurar el titulo de la grafica
plt.title("DIAGRAMA DE BARRAS")
plt.xlabel("Lenguajes de progrmacion")
plt.ylabel("Porcentajes")
#Mostrar la grafica
plt.legend()

#Guardar automatico
plt.savefig("diagrama_barras.png")

plt.show()