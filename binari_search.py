import random
import time

def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1

def busqueda_binaria(lista, objetivo, limit_inf=None, limit_sup=None):
    if limit_inf is None:
        limit_inf = 0
    if limit_sup is None:
        limit_sup = len(lista)-1

    if limit_sup < limit_inf:
        return -1
    
    punto_medio = (limit_inf + limit_sup) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limit_inf, punto_medio-1)
    else: 
        return busqueda_binaria(lista, objetivo, punto_medio+1, limit_sup)
    
if __name__=='__main__':
    
    size = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < size:
        conjunto_inicial.add(random.randint(-3*size, 3*size))

    lista_ordenada = sorted(list(conjunto_inicial))

    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"tiempo de bisqueda ingenua: {fin - inicio} segundos.")

    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"tiempo de bisqueda binaria: {fin - inicio} segundos.")

