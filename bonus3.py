import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento < numero_aleatorio:
        print("El número es mayor. Intenta nuevamente.")
    elif intento > numero_aleatorio:
        print("El número es menor. Intenta nuevamente.")
    else:
        print(f"Felicitaciones, has adivinado el número en {intentos} intentos.")
        break
