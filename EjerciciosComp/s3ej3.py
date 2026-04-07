import math


def area_circulo(radio):
    return math.pi * (radio ** 2)


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


def maximo_y_minimo(numeros):
    if len(numeros) == 0:
        return None
    return max(numeros), min(numeros)


if __name__ == "__main__":
    radio = 5
    temperatura = 30
    valores = [10, 20, 30, 40, 50]

    print(f"Area del circulo (radio={radio}): {area_circulo(radio):.2f}")
    print(f"{temperatura} C en Fahrenheit: {celsius_a_fahrenheit(temperatura):.2f} F")
    print(f"Promedio de {valores}: {promedio_lista(valores):.2f}")

    resultado = maximo_y_minimo(valores)
    if resultado is not None:
        maximo, minimo = resultado
        print(f"Maximo: {maximo}, Minimo: {minimo}")