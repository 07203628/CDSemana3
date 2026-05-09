import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

print("Primeras filas del dataset:")
print(iris.head())
print("\nInformacion general:")
iris.info()
print("\nEstadisticas descriptivas:")
print(iris.describe(include="all"))

columnas_numericas = iris.select_dtypes(include="number").columns
iris[columnas_numericas].hist(figsize=(10, 8), bins=20, color="tab:blue", edgecolor="black")
plt.suptitle("Histogramas de columnas numericas")
plt.tight_layout()

corr = iris[columnas_numericas].corr()
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Matriz de correlacion")

plt.figure(figsize=(10, 6))
for i, col in enumerate(columnas_numericas, start=1):
    plt.subplot(2, 2, i)
    sns.boxplot(data=iris, x="species", y=col)
    plt.title(f"Boxplot de {col} por especie")
plt.tight_layout()

outliers = {}
for col in columnas_numericas:
    q1 = iris[col].quantile(0.25)
    q3 = iris[col].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers[col] = iris[(iris[col] < limite_inferior) | (iris[col] > limite_superior)][col]

print("\nOutliers detectados por columna:")
for col, serie in outliers.items():
    print(f"{col}: {len(serie)} outliers")

plt.show()
