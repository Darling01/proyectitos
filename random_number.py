import random

def random_number(x):
    # x muestra el limite superior del rango de valores
    numero_aleatorio = random.randint(1, x)  # numero aleatorio entre 1 y x
    prediccion = 0  # para que no coincida con el numero

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"adivina el numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("intenta otra vez perrillo")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez")

    print(numero_aleatorio)

random_number(10)








