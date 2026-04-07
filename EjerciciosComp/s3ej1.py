edad = 21
altura = 1.75
nombre = "Diego"
es_estudiante = True
hobbies = ["leer", "correr", "programar"]
usuario = {
	"nombre": nombre,
	"edad": edad,
	"activo": es_estudiante,
}

numero_str = "42"
numero_int_desde_str = int(numero_str)

promedio_float = 9.8
promedio_int = int(promedio_float)

cantidad_int = 7
cantidad_float = float(cantidad_int)

print(f"El usuario tiene {edad} años")

print("\n--- Tipos de variables ---")
print(type(edad), type(altura), type(nombre), type(es_estudiante), type(hobbies), type(usuario))

print("\n--- Resultados de conversiones ---")
print(f"str a int: {numero_str} -> {numero_int_desde_str}")
print(f"float a int: {promedio_float} -> {promedio_int}")
print(f"int a float: {cantidad_int} -> {cantidad_float}")