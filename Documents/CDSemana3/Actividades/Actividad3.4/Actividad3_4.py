import ssl
from io import StringIO
from pathlib import Path
from urllib.request import urlopen

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def cargar_y_limpiar_titanic():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with urlopen(url, context=context) as response:
        contenido = response.read().decode("utf-8")

    df = pd.read_csv(StringIO(contenido))

    # Limpieza base para visualizacion
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df = df.drop_duplicates().copy()

    return df


def guardar_histograma(df, carpeta_salida):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Age"], bins=30, kde=True, color="#2563eb")
    plt.title("Distribucion de Edad (Titanic)")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    ruta = carpeta_salida / "01_histograma_edad.png"
    plt.savefig(ruta, dpi=150)
    plt.close()

    interpretacion = (
        "Histograma (Edad): la mayor concentracion de pasajeros esta entre 20 y 40 anos, "
        "con menos casos en edades extremas."
    )
    return ruta, interpretacion


def guardar_barras(df, carpeta_salida):
    plt.figure(figsize=(7, 5))
    orden = df["Pclass"].value_counts().index
    sns.countplot(data=df, x="Pclass", order=orden, hue="Pclass", palette="Blues", legend=False)
    plt.title("Cantidad de Pasajeros por Clase")
    plt.xlabel("Clase")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    ruta = carpeta_salida / "02_barras_clase.png"
    plt.savefig(ruta, dpi=150)
    plt.close()

    interpretacion = (
        "Grafico de barras (Pclass): la clase 3 concentra la mayor cantidad de pasajeros, "
        "mientras que la clase 1 es la menos numerosa."
    )
    return ruta, interpretacion


def guardar_dispersion(df, carpeta_salida):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived", palette="Set2", alpha=0.7)
    plt.title("Relacion entre Edad y Tarifa")
    plt.xlabel("Edad")
    plt.ylabel("Tarifa")
    plt.tight_layout()
    ruta = carpeta_salida / "03_dispersion_edad_tarifa.png"
    plt.savefig(ruta, dpi=150)
    plt.close()

    interpretacion = (
        "Diagrama de dispersion (Edad vs Fare): no hay relacion lineal fuerte entre edad y tarifa; "
        "se observan tarifas altas concentradas en pocos casos."
    )
    return ruta, interpretacion


def guardar_heatmap(df, carpeta_salida):
    columnas = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
    corr = df[columnas].corr(numeric_only=True)

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Mapa de Calor de Correlaciones")
    plt.tight_layout()
    ruta = carpeta_salida / "04_heatmap_correlaciones.png"
    plt.savefig(ruta, dpi=150)
    plt.close()

    interpretacion = (
        "Mapa de calor: se observa correlacion negativa moderada entre Pclass y Fare, "
        "y relaciones bajas entre la mayoria de variables numericas."
    )
    return ruta, interpretacion


def guardar_interpretaciones(carpeta_salida, interpretaciones):
    ruta = carpeta_salida / "interpretaciones.txt"
    contenido = []
    for i, texto in enumerate(interpretaciones, start=1):
        contenido.append(f"{i}. {texto}")

    ruta.write_text("\n".join(contenido), encoding="utf-8")
    return ruta


def main():
    carpeta_salida = Path(__file__).resolve().parent / "visualizaciones"
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    df = cargar_y_limpiar_titanic()

    resultados = []

    ruta_hist, int_hist = guardar_histograma(df, carpeta_salida)
    resultados.append((ruta_hist, int_hist))

    ruta_bar, int_bar = guardar_barras(df, carpeta_salida)
    resultados.append((ruta_bar, int_bar))

    ruta_disp, int_disp = guardar_dispersion(df, carpeta_salida)
    resultados.append((ruta_disp, int_disp))

    ruta_heat, int_heat = guardar_heatmap(df, carpeta_salida)
    resultados.append((ruta_heat, int_heat))

    archivo_interpretaciones = guardar_interpretaciones(
        carpeta_salida,
        [texto for _, texto in resultados]
    )

    print("Visualizaciones guardadas:")
    for ruta, texto in resultados:
        print(f"- {ruta.name}")
        print(f"  Interpretacion: {texto}")

    print(f"\nInterpretaciones completas: {archivo_interpretaciones.name}")


if __name__ == "__main__":
    main()
