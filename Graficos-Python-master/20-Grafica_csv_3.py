import pandas as pd
import matplotlib.pyplot as plt

# Leer las tablas
csv = pd.read_csv('comercial_delta_data_large.csv', sep=',', decimal=',')
dataframe = pd.DataFrame(csv[["NombreCliente", "Genero", "FrecuenciaCompra"]])

# Procesar datos
sexo = dataframe["Genero"].value_counts()
frecuencia_compra = dataframe["FrecuenciaCompra"].value_counts().head()
nombre_cliente = dataframe["NombreCliente"].value_counts().head()

# Imprimir valores
print(frecuencia_compra)

# Configuración de gráficos
plt.figure(figsize=(12, 8))  # Ajustar tamaño de la figura

# Gráfica 1: Distribución por Género
plt.subplot(2, 2, 1)  # 2 filas, 2 columnas, gráfico 1
sexo.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen'])
plt.title("Distribución por Género")
plt.ylabel("")  # Quitar etiqueta del eje Y

# Gráfica 2: Frecuencia de Compra
plt.subplot(2, 2, 2)  # 2 filas, 2 columnas, gráfico 2
frecuencia_compra.plot(kind='bar', color='orange')
plt.title("Frecuencia de Compra")
plt.xlabel("Frecuencia")
plt.ylabel("Cantidad")
plt.xticks(rotation=45, fontsize=9)

# Gráfica 3: Clientes con más compras
plt.subplot(2, 1, 2)  # 2 filas, 1 columna, gráfico 3 (en la fila inferior)
nombre_cliente.plot(kind='bar', color='green')
plt.title("Clientes con Mayor Frecuencia")
plt.xlabel("Clientes")
plt.ylabel("Cantidad")
plt.xticks(rotation=45, fontsize=9)

# Título general
plt.suptitle("COMERCIAL DELTA - Datos", fontsize=16)

# Ajustar diseño para evitar superposiciones
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Mostrar gráficos
plt.show()
