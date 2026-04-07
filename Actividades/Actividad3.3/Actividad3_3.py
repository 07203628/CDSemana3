import ssl
from io import StringIO
from urllib.request import urlopen

import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Descarga el contenido CSV y lo guarda como texto.
with urlopen(url, context=context) as response:
	contenido = response.read().decode("utf-8")

# Carga el CSV en un DataFrame de pandas.
df = pd.read_csv(StringIO(contenido))

# Muestra el estado inicial del dataset (dimensiones y nulos).
print("=" * 50)
print("ESTADO INICIAL")
print("=" * 50)
print(f"Filas y columnas: {df.shape}")
print("Valores nulos por columna:")
print(df.isnull().sum().to_string())

# Imputa valores faltantes en columnas clave.
df_imputado = df.copy()
df_imputado["Age"] = df_imputado["Age"].fillna(df_imputado["Age"].median())
df_imputado["Embarked"] = df_imputado["Embarked"].fillna(df_imputado["Embarked"].mode()[0])
df_imputado["Cabin"] = df_imputado["Cabin"].fillna("Desconocida")

# Muestra el estado del dataset despues de imputar nulos.
print("\n" + "=" * 50)
print("DESPUES DE IMPUTAR")
print("=" * 50)
print(f"Filas y columnas: {df_imputado.shape}")
print("Valores nulos por columna:")
print(df_imputado.isnull().sum().to_string())

# Crea una version alternativa eliminando filas con nulos para comparar estrategias.
df_eliminado = df.dropna().copy()

# Muestra el estado del dataset al eliminar filas con nulos.
print("\n" + "=" * 50)
print("DESPUES DE ELIMINAR FILAS CON NULOS")
print("=" * 50)
print(f"Filas y columnas: {df_eliminado.shape}")
print("Valores nulos por columna:")
print(df_eliminado.isnull().sum().to_string())

# Elimina registros duplicados en la version imputada.
filas_antes = len(df_imputado)
df_sin_duplicados = df_imputado.drop_duplicates().copy()
filas_despues = len(df_sin_duplicados)

# Reporta cuantas filas duplicadas se eliminaron.
print("\n" + "=" * 50)
print("ELIMINACION DE DUPLICADOS")
print("=" * 50)
print(f"Filas antes de eliminar duplicados: {filas_antes}")
print(f"Filas despues de eliminar duplicados: {filas_despues}")
print(f"Duplicados eliminados: {filas_antes - filas_despues}")

# Convierte tipos de datos a categorias donde aporta eficiencia semantica.
tipos_antes = df_sin_duplicados.dtypes
df_convertido = df_sin_duplicados.copy()

df_convertido["Survived"] = df_convertido["Survived"].astype("category")
df_convertido["Pclass"] = df_convertido["Pclass"].astype("category")
df_convertido["Sex"] = df_convertido["Sex"].astype("category")
df_convertido["Embarked"] = df_convertido["Embarked"].astype("category")

tipos_despues = df_convertido.dtypes

# Muestra comparacion de tipos antes y despues de la conversion.
print("\n" + "=" * 50)
print("CONVERSION DE TIPOS DE DATOS")
print("=" * 50)
print("Tipos antes:")
print(tipos_antes[["Survived", "Pclass", "Sex", "Embarked"]].to_string())
print("\nTipos despues:")
print(tipos_despues[["Survived", "Pclass", "Sex", "Embarked"]].to_string())

# Estandariza nombres de columnas: minusculas, sin espacios extremos y con guion bajo.
columnas_antes = df_convertido.columns.tolist()
df_estandarizado = df_convertido.copy()
df_estandarizado.columns = (
	df_estandarizado.columns
	.str.strip()
	.str.lower()
	.str.replace(" ", "_", regex=False)
)
columnas_despues = df_estandarizado.columns.tolist()

# Muestra nombres de columnas antes y despues del estandarizado.
print("\n" + "=" * 50)
print("ESTANDARIZACION DE NOMBRES DE COLUMNAS")
print("=" * 50)
print("Columnas antes:")
print(columnas_antes)
print("\nColumnas despues:")
print(columnas_despues)

# Crea columnas derivadas para enriquecer el analisis.
df_final = df_estandarizado.copy()
df_final["tamano_familia"] = df_final["sibsp"] + df_final["parch"] + 1
df_final["viaja_solo"] = (df_final["tamano_familia"] == 1).astype(int)
df_final["tarifa_por_persona"] = (df_final["fare"] / df_final["tamano_familia"]).round(2)
df_final["grupo_edad"] = pd.cut(
	df_final["age"],
	bins=[0, 12, 18, 35, 60, 100],
	labels=["nino", "adolescente", "adulto_joven", "adulto", "adulto_mayor"],
	include_lowest=True
)

# Muestra una vista previa de las nuevas columnas creadas.
print("\n" + "=" * 50)
print("NUEVAS COLUMNAS")
print("=" * 50)
print("Columnas agregadas: tamano_familia, viaja_solo, tarifa_por_persona, grupo_edad")
print(df_final[["name", "age", "sibsp", "parch", "fare", "tamano_familia", "viaja_solo", "tarifa_por_persona", "grupo_edad"]].head(10).to_string(index=False))

# Calcula metricas globales para comparar estado inicial vs final.
nulos_iniciales = int(df.isnull().sum().sum())
nulos_finales = int(df_final.isnull().sum().sum())

# Resumen final de cambios aplicados al dataset.
print("\n" + "=" * 50)
print("RESUMEN: ANTES Y DESPUES")
print("=" * 50)
print("ANTES")
print(f"- Dimensiones: {df.shape}")
print(f"- Total de nulos: {nulos_iniciales}")
print(f"- Total de columnas: {len(df.columns)}")

print("\nDESPUES")
print(f"- Dimensiones: {df_final.shape}")
print(f"- Total de nulos: {nulos_finales}")
print(f"- Total de columnas: {len(df_final.columns)}")

