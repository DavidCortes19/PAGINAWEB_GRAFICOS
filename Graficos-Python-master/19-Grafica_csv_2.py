import pandas as pd 
import matplotlib.pyplot as plt

#https://www.datosabiertos.gob.pe/group/datos-abiertos-de-covid-19
#leer las tablas
csv=pd.read_csv('diagnostico_cardiaco_extendido.csv',sep=',',decimal=',')
dataframe=pd.DataFrame(csv[["Género","Hábitos Alimenticios","Colesterol (mg/dl)"]])
sexo=dataframe["Hábitos Alimenticios"].value_counts()
departamento=dataframe["Colesterol (mg/dl)"].value_counts().head()
print(departamento)
"----------Grafica 1---------"
plt.subplot(1, 2, 1)
sexo.plot(kind='pie',autopct='%1.01f%%')
plt.title("Hábitos Alimenticios")
"----------Grafica 2---------"
plt.subplot(1, 2, 2)
departamento.plot(kind='bar',rot=20)
plt.title("Colesterol (mg/dl)")
plt.xticks(fontsize=9)

plt.suptitle("DIAGNOSTICO CARDIACO")
plt.show()



