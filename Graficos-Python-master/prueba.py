import pandas as pd 
import matplotlib.pyplot as plt

csv=pd.read_csv('fallecidos_covid.csv',sep=';')
dataframe=pd.DataFrame(csv[{"FECHA_FALLECIMIENTO","SEXO","DEPARTAMENTO"}])
sexo=dataframe["SEXO"].value_counts()
departamento=dataframe["DEPARTAMENTO"].value_counts().head()
print(departamento)

#Grafica 1
plt.subplot(1,2,1)
sexo.plot(kind="pie",autopct='%1.01f%%')
plt.title("SEXO")

#Grafica 2
plt.subplot(1,2,2)
departamento.plot(kind="bar",rot=20)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.title("DEPARTAMENTO")


plt.suptitle("GRAFICA COVID 19 - FALLECIDOS")
plt.show()