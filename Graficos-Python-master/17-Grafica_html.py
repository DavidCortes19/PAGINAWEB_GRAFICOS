import pandas as pd 
import matplotlib.pyplot as plt

#leer las tablas
tables=pd.read_html('https://www.nbamaniacs.com/palmares-nba/')

print(f'Numero de tablas:{len(tables)}')
datos=(tables[0].head())
print(datos)

dataframe=pd.DataFrame(datos[['Franquicia','Títulos']])
print(dataframe)

dataframe.plot(x="Franquicia",kind="bar",rot=10)
plt.title("TOP 5 - CAMPEONES NBA")
plt.xticks(fontsize=9)
plt.show()
"""
#imprimir tablas
for i in range(len(tables)):
    print(tables[i])
"""

