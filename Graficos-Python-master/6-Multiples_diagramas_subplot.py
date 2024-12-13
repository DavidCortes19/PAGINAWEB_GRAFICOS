import matplotlib.pyplot as plt
#------plot 1:
dolares = [7000, 6500 , 7400 , 8500]
years = [2019, 2020, 2021, 2022]

#2 filas,2 columna 
plt.subplot(2, 2, 1)
plt.plot(years,dolares,linewidth=3)
plt.xticks(years)
plt.ylabel("Dolares")
plt.title("Ventas Anuales",fontsize=12)

#plt.grid()

#------plot 2:
productos=["Cuadernos","Lapiceros","Reglas","Hojas","Folders","Otros"]
cantidad=[5000,10000,6000,8000,3000,2000]

#2 filas,2columna,pisicion 
plt.subplot(2, 2, 2)
plt.pie(cantidad,labels=productos,autopct='%1.0f%%')
plt.title("Productos mas vendidos",fontsize=12)

#------plot 3:
#DATA
tiempo_algebra=[1,3,5,7]
notas_algebra=[9,12,14,16]

tiempo_quimica=[2,4,6,9]
notas_quimica=[12,15,13,11]

#Caracteristicas
plt.subplot(2, 2, 3)
plt.scatter(tiempo_algebra,notas_algebra,color="black",label="Algebra")
plt.scatter(tiempo_quimica,notas_quimica,color="red",label="Quimica")

#titulo
plt.title("Diagrama de dispersion",fontsize=12)
plt.xlabel("Horas de estudio")
plt.ylabel("Notas de estudio")

#------plot4:
#Ventas al año
sales_a=[2,3.5,4.5,5.2,3,7,5.5]
sales_b=[1,2.3,3.1,4.5,2,4.2,4.3]
years=[2015,2016,2018,2019,2020,2021,2022]

plt.subplot(2,2,4)
plt.fill_between(years,sales_a,label="EMPRESA A",color="green")
plt.fill_between(years,sales_b,label="EMPRESA B",color="blue")
plt.title("Diagrama de areas", fontsize=12)

plt.legend(loc="upper left")

"----------------------------------------------------------------"
plt.suptitle("MULTIPLES DIAGRAMAS",fontsize=18)
plt.show()