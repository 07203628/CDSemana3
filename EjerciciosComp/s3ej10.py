def calcular_media(datos):
    suma = 0
    for valor in datos:
        suma += valor
    return suma / len(datos)


def calcular_mediana(datos):
    ordenados = sorted(datos)
    n = len(ordenados)
    mitad = n // 2

    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
    return ordenados[mitad]


def calcular_moda(datos):
    conteos = {}
    for valor in datos:
        conteos[valor] = conteos.get(valor, 0) + 1

    max_frecuencia = max(conteos.values())
    modas = [valor for valor, frecuencia in conteos.items() if frecuencia == max_frecuencia]

    if max_frecuencia == 1:
        return []
    return sorted(modas)


def procesar(datos):
    media = calcular_media(datos)
    mediana = calcular_mediana(datos)
    moda = calcular_moda(datos)
    return media, mediana, moda


conjuntos = [
    [5, 3, 8, 3, 7],
    [10, 20, 30, 40],
    [1, 2, 2, 3, 3, 3, 4],
]

for datos in conjuntos:
    media, mediana, moda = procesar(datos)
    print(f"Datos: {datos}")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    if moda:
        print(f"Moda: {moda}")
    else:
        print("Moda: sin moda")
    print()
