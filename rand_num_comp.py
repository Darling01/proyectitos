import random

def rand_num_comp(x):
    
    print(f"selecciona un numero entre 1 y {x}")

    limit_inferior = 1
    limit_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar una prediccion
        if limit_inferior != limit_superior:
            prediccion = random.randint(limit_inferior, limit_superior)
        else:
            prediccion = limit_inferior

        #obtener respuesta del usuario

        respuesta = input(f"mi prediccion es {prediccion}, si es muy alta (A). Si es muy baja (B). Si es correcta (C): ").lower()

        if respuesta == "a":
            limit_superior = prediccion - 1
        elif respuesta == "b":
            limit_inferior = prediccion + 1

    print(f"la computador adivino tu numero: {prediccion}")


rand_num_comp(10)



