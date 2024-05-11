suma = 0
numero = int(input("Ingrese un número entero positivo (ingrese un número negativo para terminar): "))
while numero >= 0:
    suma += numero
    numero = int(input("Ingrese otro número entero positivo (o ingrese un número negativo para terminar): "))
print(f"La suma de los números positivos ingresados es: {suma}")
