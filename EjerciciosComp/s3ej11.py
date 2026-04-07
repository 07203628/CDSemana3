def calcular_rango(datos):
    return max(datos) - min(datos)


def calcular_media(datos):
    return sum(datos) / len(datos)


def calcular_varianza(datos):
    media = calcular_media(datos)
    suma_cuadrados = 0
    for valor in datos:
        suma_cuadrados += (valor - media) ** 2
    return suma_cuadrados / len(datos)


def raiz_cuadrada(numero, tolerancia=1e-10, max_iter=1000):
    if numero == 0:
        return 0.0
    x = numero
    for _ in range(max_iter):
        siguiente = 0.5 * (x + numero / x)
        if abs(siguiente - x) < tolerancia:
            return siguiente
        x = siguiente
    return x


def calcular_desviacion_estandar(datos):
    varianza = calcular_varianza(datos)
    return raiz_cuadrada(varianza)


def procesar(datos):
    rango = calcular_rango(datos)
    varianza = calcular_varianza(datos)
    desviacion = calcular_desviacion_estandar(datos)
    return rango, varianza, desviacion


conjuntos = [
    [2, 4, 4, 4, 5, 5, 7, 9],
    [1, 3, 5, 7, 9],
]

for datos in conjuntos:
    rango, varianza, desviacion = procesar(datos)
    print(f"Datos: {datos}")
    print(f"Rango: {rango}")
    print(f"Varianza: {varianza}")
    print(f"Desviacion estandar: {desviacion}")
    print()
