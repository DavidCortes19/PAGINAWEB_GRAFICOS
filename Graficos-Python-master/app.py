import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Asegúrate de que los directorios 'static' y 'uploads' existan
os.makedirs("static", exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    graph_exists = False  # Inicialmente no existen gráficos
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            # Procesar el archivo y generar gráficos
            generate_graphs(filepath)
            graph_exists = check_graphs()  # Verifica si los gráficos fueron generados correctamente
    return render_template("index.html", graph_exists=graph_exists)

def generate_graphs(filepath):
    # Leer el archivo CSV
    df = pd.read_csv(filepath)

    # Generación del gráfico de distribución por género
    gender_dist = df['Genero'].value_counts(normalize=True) * 100
    plt.figure(figsize=(6, 6))
    gender_dist.plot(kind='pie', autopct='%1.1f%%', colors=['#85C1AE', '#85B0D4'], startangle=90)
    plt.title('Distribución por Género')
    plt.ylabel('')
    gender_graph_path = "static/gender_distribution.png"
    plt.savefig(gender_graph_path)
    plt.close()

    # Generación del gráfico de frecuencia de compra
    purchase_freq = df['FrecuenciaCompra'].value_counts()
    plt.figure(figsize=(8, 6))
    purchase_freq.plot(kind='bar', color='orange')
    plt.title('Frecuencia de Compra')
    plt.xlabel('Frecuencia')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    purchase_graph_path = "static/purchase_frequency.png"
    plt.savefig(purchase_graph_path)
    plt.close()

    # Generación del gráfico de clientes con mayor frecuencia
    top_clients = df['NombreCliente'].value_counts().head(5)
    plt.figure(figsize=(8, 6))
    top_clients.plot(kind='bar', color='green')
    plt.title('Clientes con Mayor Frecuencia')
    plt.xlabel('Clientes')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    clients_graph_path = "static/top_clients.png"
    plt.savefig(clients_graph_path)
    plt.close()

def check_graphs():
    # Verifica si todos los gráficos han sido generados
    return os.path.exists("static/gender_distribution.png") and \
           os.path.exists("static/purchase_frequency.png") and \
           os.path.exists("static/top_clients.png")

if __name__ == "__main__":
    app.run(debug=True)
