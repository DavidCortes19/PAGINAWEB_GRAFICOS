import matplotlib.pyplot as plt

#Encuesta 200 
#DATA
pet=["Dog","Cat","Rabbit","Parrot","Fish"]
valores=[80,65,25,18,12]

#PLOT
plt.pie(valores,labels=pet,explode=(0.1,0,0,0,0),autopct='%1.1f%%')

#title
plt.title("Diagrama de sectores",fontsize=20)

plt.savefig("diagrama_sectores.png")

#Display
plt.show()