import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

suma_elemento = arr1 + arr2
escalar = 3
multiplicado = arr1 * escalar

media = np.mean(arr1)
mediana = np.median(arr1)
desviacion = np.std(arr1)

valores_unicos = np.unique(np.array([1, 2, 2, 3, 4, 4, 5, 5, 5]))

array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = array_1d.reshape(2, 3)

print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"Suma elemento a elemento: {suma_elemento}")
print(f"arr1 multiplicado por {escalar}: {multiplicado}")
print(f"Media de arr1: {media}")
print(f"Mediana de arr1: {mediana}")
print(f"Desviacion estandar de arr1: {desviacion}")
print(f"Valores unicos: {valores_unicos}")
print(f"Array 1D: {array_1d}")
print("Array 2D (reshape 2x3):")
print(array_2d)
