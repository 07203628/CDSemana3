import pandas as pd
import numpy as np

data = {
    "nombre": ["Ana", "Luis", "Maria", "Carlos", "Sofia", "Ana"],
    "edad": [20, 22, 19, 21, np.nan, 20],
    "carrera": ["Ing", "Ing", "Lic", "Ing", "Lic", "Ing"],
    "promedio": [8.5, 9.0, 7.8, np.nan, 9.5, 8.5],
}

df = pd.DataFrame(data)

edad_media = df["edad"].mean()
promedio_media = df["promedio"].mean()
df_filled = df.copy()
df_filled["edad"] = df_filled["edad"].fillna(edad_media)
df_filled["promedio"] = df_filled["promedio"].fillna(promedio_media)

df_sin_duplicados = df_filled.drop_duplicates()

df_sin_duplicados["categoria_promedio"] = df_sin_duplicados["promedio"].apply(
    lambda x: "alto" if x >= 8.5 else "medio"
)

seleccion_loc = df_sin_duplicados.loc[df_sin_duplicados["carrera"] == "Ing", ["nombre", "promedio"]]
seleccion_iloc = df_sin_duplicados.iloc[0:3, 0:3]

nuevos = pd.DataFrame(
    {
        "nombre": ["Elena", "Mario"],
        "edad": [24, 20],
        "carrera": ["Lic", "Ing"],
        "promedio": [8.9, 7.9],
        "categoria_promedio": ["alto", "medio"],
    }
)

concatenado = pd.concat([df_sin_duplicados, nuevos], ignore_index=True)

print("DataFrame con NaN y duplicados:")
print(df)
print("\nDataFrame con faltantes llenados:")
print(df_filled)
print("\nDataFrame sin duplicados y con apply():")
print(df_sin_duplicados)
print("\nUso de loc:")
print(seleccion_loc)
print("\nUso de iloc:")
print(seleccion_iloc)
print("\nDataFrame concatenado:")
print(concatenado)
