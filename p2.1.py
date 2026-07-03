import pandas as pd

# Leer el archivo CSV
datos = pd.read_csv("estudiantes.csv")

# Columnas a analizar
columnas = ["Edad", "Tareas", "Horas_Estudio", "Calificacion_Final"]

for columna in columnas:
    print(f"\n--- {columna} ---")
    print("Rango:", datos[columna].max() - datos[columna].min())
    print("Varianza:", datos[columna].var())
    print("Desviación estándar:", datos[columna].std())