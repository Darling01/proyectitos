import random

def jugar():
    usuario = input("escoge una opcion. \n").lower()
    
    comp = random.choice(['piedra', 'papel', 'tijera'])

    if usuario == comp:
        return 'empate'
    if gano_usuario(usuario, comp):
        return 'ganaste'
    
    return 'perdiste'

def gano_usuario(jugador, oponente):
    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False
    
print(jugar())
