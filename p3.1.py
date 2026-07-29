import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Leer datos
df = pd.read_csv("dataset_clientes.csv")

# Variables
X = df[[
    "Edad",
    "Compras_Mensuales",
    "Gasto_Mensual_MXN",
    "Visitas_Web_Mensuales",
    "Dias_Desde_Ultima_Compra",
    "Tiempo_Sesion_Min",
    "Clicks_Promedio"
]]

X = X.dropna()

# Escalado
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

# Método del codo
inercia = []

for k in range(1, 11):
    modelo = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    modelo.fit(X_escalado)
    inercia.append(modelo.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), inercia, marker="o")
plt.xlabel("Número de clusters")
plt.ylabel("Inercia")
plt.title("Método del Codo")
plt.grid(True)
plt.show()

# Modelo final 
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = modelo.fit_predict(X_escalado)

df_limpio = X.copy()
df_limpio["Cluster"] = clusters

print(df_limpio)

print("\nPromedio por cluster:\n")
print(df_limpio.groupby("Cluster").mean())
    random_state=42,
    n_init=10
)

clusters = modelo.fit_predict(X_escalado)

df_limpio = X.copy()
df_limpio["Cluster"] = clusters

print(df_limpio)

print("\nPromedio por cluster:\n")
print(df_limpio.groupby("Cluster").mean())
