import matplotlib.pyplot as plt

#DATA
tiempo_algebra=[1,3,5,7]
notas_algebra=[9,12,14,16]

tiempo_quimica=[2,4,6,9]
notas_quimica=[12,15,13,11]

#Caracteristicas
plt.scatter(tiempo_algebra,notas_algebra,color="black",label="Algebra")
plt.scatter(tiempo_quimica,notas_quimica,color="red",label="Quimica")

#titulo
plt.title("Diagrama de dispersion")
plt.xlabel("Horas de estudio")
plt.ylabel("Notas de estudio")

#Mostar
plt.legend(loc="upper left")

plt.savefig("diagrama_dispersion.png")
plt.grid()
plt.show()