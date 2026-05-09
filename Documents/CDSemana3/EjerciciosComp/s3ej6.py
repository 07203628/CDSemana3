import pandas as pd

data = {
    "nombre": ["Ana", "Luis", "Maria", "Carlos", "Sofia"],
    "edad": [20, 22, 19, 21, 23],
    "carrera": ["Ing", "Ing", "Lic", "Ing", "Lic"],
    "promedio": [8.5, 9.0, 7.8, 8.2, 9.5],
}

df = pd.DataFrame(data)

nombres = df["nombre"]
filtrados = df[df["promedio"] > 8.5]
ordenado_por_edad = df.sort_values(by="edad")

df["aprobado"] = df["promedio"] >= 7
promedio_por_carrera = df.groupby("carrera")["promedio"].mean()

print("DataFrame original:")
print(df)
print("\nColumna nombre:")
print(nombres)
print("\nEstudiantes con promedio > 8.5:")
print(filtrados)
print("\nDataFrame ordenado por edad:")
print(ordenado_por_edad)
print("\nPromedio por carrera:")
print(promedio_por_carrera)
