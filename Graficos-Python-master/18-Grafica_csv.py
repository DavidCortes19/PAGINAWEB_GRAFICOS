import pandas as pd
import matplotlib.pyplot as plt

# Leer las tablas
csv = pd.read_csv('fallecidos_covid.csv', sep=';', decimal=',')
dataframe = pd.DataFrame(csv[["FECHA_FALLECIMIENTO", "SEXO", "DEPARTAMENTO"]])

# Procesar datos
sexo = dataframe["SEXO"].value_counts()
departamento = dataframe["DEPARTAMENTO"].value_counts().head()
fecha_fallecimiento = dataframe["FECHA_FALLECIMIENTO"].value_counts().head()

# Imprimir valores de departamentos
print(departamento)

# Configuración de gráficos
plt.figure(figsize=(12, 8))  # Ajustar tamaño de la figura

# Gráfica 1: Distribución por SEXO
plt.subplot(2, 2, 1)  # 2 filas, 2 columnas, gráfico 1
sexo.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Distribución por Sexo")
plt.ylabel("")  # Quitar etiqueta del eje Y

# Gráfica 2: Departamentos con más fallecidos
plt.subplot(2, 2, 2)  # 2 filas, 2 columnas, gráfico 2
departamento.plot(kind='bar', color='orange')
plt.title("Departamentos con Más Fallecidos")
plt.xlabel("Departamento")
plt.ylabel("Cantidad de Fallecidos")
plt.xticks(rotation=45, fontsize=9)

# Gráfica 3: Frecuencia de fechas de fallecimiento
plt.subplot(2, 1, 2)  # 2 filas, 1 columna, gráfico 3 (en la fila inferior)
fecha_fallecimiento.plot(kind='bar', color='green')
plt.title("Fechas con Mayor Número de Fallecidos")
plt.xlabel("Fecha de Fallecimiento")
plt.ylabel("Cantidad")
plt.xticks(rotation=45, fontsize=9)

# Título general
plt.suptitle("COVID-19 - Fallecidos en Perú", fontsize=16)

# Mostrar gráficos
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar diseño para evitar superposiciones
plt.show()
