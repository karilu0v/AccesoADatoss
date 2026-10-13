import random

ganadas_jugador = 0
ganadas_maquina= 0
movimientos = ["piedra", "papel","tijeras"]

def movimiento_valido(movimiento, movimientos):
    for i in movimientos:
        if(movimiento == i):
            return True
    return False
        

def turno_maquina(movimientos):
    print("Turno de la máquina", end=": ")
    jugada = random.choice(movimientos)
    print(jugada)
    return jugada

def comparar_movimientos(movimiento, movimiento_maquina):
    global ganadas_maquina, ganadas_jugador
    if movimiento == movimiento_maquina:
       print("Habéis empatado") 
    else:
        if movimiento == "piedra" and movimiento_maquina == "tijeras":
            ganadas_jugador += 1
            print("Has ganado")
        elif movimiento == "papel" and movimiento_maquina == "piedra":
            ganadas_jugador += 1
            print("Has ganado")
        elif movimiento == "tijeras" and movimiento_maquina == "papel":
            ganadas_jugador += 1
            print("Has ganado")
        else:
            ganadas_maquina += 1
            print("Ha ganado la máquina")

    
def partida():
    global movimientos, ganadas_maquina, ganadas_jugador
    print("Juego de piedra, papel o tijeras")
    print()
    while ganadas_jugador < 3 and ganadas_maquina < 3:
        print("Tu turno:")
        print("Elije piedra, papel o tijeras")
        movimiento = input("Ingresa el movimiento: ")
        while not movimiento_valido(movimiento, movimientos):
            movimiento = input("Ingresa un término válido: ")
        movimiento_maquina = turno_maquina(movimientos)
        comparar_movimientos(movimiento, movimiento_maquina)
        print(f"jugador: {ganadas_jugador} máquina: {ganadas_maquina}")
        print()
    if ganadas_jugador == 3:
        print("gana el jugador")
    else:
        print("gana la máquina")
    
    

#Pruebas
partida()