def clasificar_numero(numero):
	if numero > 0:
		return "positivo"
	elif numero < 0:
		return "negativo"
	else:
		return "cero"


def mostrar_lista_con_for(lista):
	for indice, elemento in enumerate(lista, start=1):
		print(f"{indice}. {elemento}")


def factorial_con_while(numero):
	if numero < 0:
		return None

	resultado = 1
	contador = 1
	while contador <= numero:
		resultado *= contador
		contador += 1
	return resultado


def menu():
	while True:
		print("\nMenu de opciones")
		print("1. Determinar si un numero es positivo o negativo")
		print("2. Iterar una lista con for")
		print("3. Calcular factorial con while")
		print("4. Salir")

		opcion = input("Seleccione una opción: ").strip()

		if opcion == "1":
			valor = int(input("Ingresa un numero entero: "))
			tipo = clasificar_numero(valor)
			print(f"El numero {valor} es {tipo}.")
		elif opcion == "2":
			frutas = ["manzana", "pera", "mango", "uva"]
			print("Lista de frutas:")
			mostrar_lista_con_for(frutas)
		elif opcion == "3":
			valor = int(input("Ingresa un numero entero no negativo: "))
			resultado = factorial_con_while(valor)
			if resultado is None:
				print("No existe factorial para numeros negativos.")
			else:
				print(f"El factorial de {valor} es {resultado}.")
		elif opcion == "4":
			print("Programa finalizado.")
			break
		else:
			print("Opción inválida.")


if __name__ == "__main__":
	menu()
