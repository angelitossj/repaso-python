# Inicializar listas para edades menores de 18 y mayores o iguales a 18
edades_menores = []
edades_mayores = []

# Pedir al usuario ingresar la edad de 10 personas
for i in range(1, 11):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    
    # Verificar si la edad es menor de 18 o mayor/igual a 18 y agregarla a la lista correspondiente
    if edad < 18:
        edades_menores.append(edad)
    else:
        edades_mayores.append(edad)

# Imprimir las listas de edades clasificadas
print("Edades menores de 18 años:", edades_menores)
print("Edades mayores o iguales a 18 años:", edades_mayores)
