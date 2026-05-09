import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="tab:blue", label="sin(x)")
plt.title("Grafico de linea")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.figure(figsize=(8, 4))
plt.scatter(x, y, color="tab:orange", s=20, alpha=0.8, label="puntos")
plt.title("Grafico de dispersion")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True, alpha=0.3)

datos_hist = np.random.normal(loc=0, scale=1, size=1000)
plt.figure(figsize=(8, 4))
plt.hist(datos_hist, bins=30, color="tab:green", edgecolor="black", alpha=0.8)
plt.title("Histograma")
plt.xlabel("valor")
plt.ylabel("frecuencia")

categorias = ["A", "B", "C", "D"]
valores = [15, 22, 13, 27]
plt.figure(figsize=(8, 4))
plt.bar(categorias, valores, color=["#4e79a7", "#f28e2b", "#59a14f", "#e15759"])
plt.title("Grafico de barras")
plt.xlabel("categoria")
plt.ylabel("valor")

plt.tight_layout()
plt.show()
