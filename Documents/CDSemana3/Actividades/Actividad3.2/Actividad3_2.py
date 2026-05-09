import ssl
from io import StringIO
from urllib.request import urlopen

import pandas as pd


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with urlopen(url, context=context) as response:
	contenido = response.read().decode("utf-8")

df = pd.read_csv(StringIO(contenido))

def mostrar_seccion(titulo):
	print("\n" + "=" * 40)
	print(titulo)
	print("=" * 40)


mostrar_seccion("Primeras 10 filas")
print(df.head(10).to_string(index=False))

mostrar_seccion("Informacion general")
df.info()

mostrar_seccion("Tipos de datos")
print(df.dtypes.to_string())

mostrar_seccion("Valores nulos por columna")
print(df.isnull().sum().to_string())

mostrar_seccion("Estadisticas basicas")
print(df.describe().round(2).to_string())