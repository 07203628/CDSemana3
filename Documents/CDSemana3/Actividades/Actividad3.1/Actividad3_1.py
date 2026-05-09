# Actividad 3.1: Refuerzo de Python

# Ejercicio 1: Crear una lista y acceder a sus elementos
def crear_lista():
	frutas = ["manzana", "pera", "uva", "mango"] # Crear una lista
	print("\nEjercicio 1: crear una lista")
	print("Lista original:", frutas)
	print("Primer elemento:", frutas[0]) # Acceder al primer elemento
	print("Ultimo elemento:", frutas[-1]) # Acceder al último elemento
	print()

# Ejercicio 2: Modificar una lista
def modificar_lista():
	numeros = [10, 20, 30] # Crear una lista de números
	numeros.append(40) # Agregar un nuevo número al final de la lista
	numeros.remove(20) # Eliminar el número 20 de la lista
	print("\nEjercicio 2: modificar una lista")
	print("Lista final:", numeros) # Mostrar la lista después de las modificaciones
	print()

# Ejercicio 3: Recorrer una lista y sumar sus elementos
def ecorrer_y_sumar():
	numeros = [1, 2, 3, 4, 5] # Crear una lista de números
	suma = 0 # Variable para almacenar la suma total

	for numero in numeros: # Recorrer cada número en la lista
		suma += numero # Sumar el número actual a la suma total

	print("\nEjercicio 3: recorrer una lista y sumar")
	print("Lista:", numeros) # Mostrar la lista original
	print("Suma total:", suma) # Mostrar la suma total de los elementos de la lista
	print()

# Ejercicio 4: Trabajar con un diccionario
def diccionario_estudiante():
	estudiante = {
		"nombre": "Ana",
		"edad": 20,
		"carrera": "Ciencia de Datos",
		"promedio": 8.9,
	} # Crear un diccionario para almacenar información de un estudiante

	estudiante["aprobado"] = estudiante["promedio"] >= 7 # Agregar una nueva clave "aprobado" al diccionario, indicando si el estudiante aprobó o no

	print("\nEjercicio 4: trabajar con un diccionario")
	print("Diccionario:", estudiante) # Mostrar el diccionario completo
	print("Nombre:", estudiante["nombre"]) # Acceder al valor asociado a la clave "nombre"
	print("Carrera:", estudiante.get("carrera")) # Acceder al valor asociado a la clave "carrera" usando el método get()
	print()

# Ejercicio 5: Contar frecuencias de palabras en una lista usando un diccionario
def contar_frecuencias():
	palabras = ["python", "datos", "python", "analisis", "datos", "python"] # Crear una lista de palabras con algunas repeticiones
	frecuencias = {} # Crear un diccionario vacío para almacenar las frecuencias de cada palabra

	for palabra in palabras: # Recorrer cada palabra en la lista
		if palabra in frecuencias: # Si la palabra ya está en el diccionario, incrementar su frecuencia
			frecuencias[palabra] += 1 # Incrementar la frecuencia de la palabra existente
		else:
			frecuencias[palabra] = 1 # Si la palabra no está en el diccionario, agregarla con una frecuencia inicial de 1

	print("\nEjercicio 5: contar frecuencias con diccionario")
	print("Lista de palabras:", palabras) # Mostrar la lista original de palabras
	print("Frecuencias:", frecuencias) # Mostrar el diccionario con las frecuencias de cada palabra
	print()



def menu():
	print("1. Crear una lista")
	print("2. Modificar una lista")
	print("3. Recorrer una lista y sumar")
	print("4. Trabajar con un diccionario")
	print("5. Contar frecuencias de palabras")
	print("6. Salir")
	print()

def ejecutar_opcion(opcion):
	if opcion == "1":
		crear_lista()
	elif opcion == "2":
		modificar_lista()
	elif opcion == "3":
		ecorrer_y_sumar()
	elif opcion == "4":
		diccionario_estudiante()
	elif opcion == "5":
		contar_frecuencias()
	elif opcion == "6":
		print("Saliendo del programa...")
	else:
		print("Opcion no valida. Intenta de nuevo.")


def main():
	while True:
		menu()
		opcion = input("Selecciona una opcion: ")
		if opcion == "6":
			ejecutar_opcion(opcion)
			break
		ejecutar_opcion(opcion)


if __name__ == "__main__":
	main()
