tablero = [[" " for j in range(3)]for i in range(3)]
jugadores = {
    0:"X",
    1:"O",
    }
partida_terminada = False
turno = 0

#métodos y funciones
def mostrar_tablero(tablero):
    for i,v in enumerate(tablero):
        for j, k in enumerate(v):
            print(k, end = "")
            if j<2:
                print(" | ", end="")
        print()
        if i<2:
            print("-"*9)
            
def casilla_ocupada(fila, columna, tablero):
    return tablero[fila][columna] != " "

def comrpobar_coordenada(num):
    if not num.isnumeric():
        print("introduce un número del 0 al 2")
        return False
    if int(num)<0 or int(num)>2:
        print("introduce un número del 0 al 2")
        return False
    else:
        return True

def hacer_jugada(jugador,tablero):
    jugada_valida = False
    while not jugada_valida:
        #fila
        fila = input("Ingresa la fila: ")
        
        while not comrpobar_coordenada(fila):
            fila = input("Ingresa la fila: ")
        fila = int(fila)
        
        #columna
        columna = input("Ingresa la columna: ")
        
        while not comrpobar_coordenada(columna):
            columna = input("Ingresa la columna: ")
        columna = int(columna)
        
        #comprobar si es válido
        if not casilla_ocupada(fila, columna, tablero):
            jugada_valida = True
            print("jugada válida", fila, columna)
            tablero[fila][columna] = jugador
        else:
            print("Jugada no válida, repite las coordenadas")
            
def v_vertical(jugador, tablero):
    for j in range(len(tablero[0])):
        num_fichas = 0
        for i in range(len(tablero)):
            if tablero[i][j] == jugador:
                num_fichas +=1
        if num_fichas == 3:
            return True
    return False

def v_horizontal(jugador, tablero):
    for i in range(len(tablero)):
        num_fichas = 0
        for j in range(len(tablero[0])):
            if tablero[i][j] == jugador:
                num_fichas +=1
        if num_fichas == 3:
            return True
    return False
        
def v_diagonal(jugador, tablero):
    mayor = 0
    menor = 0
    #mayor
    for i in range(len(tablero)):
        if tablero[i][i] == jugador:
            mayor+=1
    #menor (de 0 a 2)
    for i in range(len(tablero)):
        if tablero[len(tablero) -1 -i][i] == jugador:
            menor +=1
    return mayor==3 or menor==3

def victoria(jugador, tablero):
    return v_vertical(jugador, tablero) or \
           v_horizontal(jugador, tablero) or \
           v_diagonal(jugador, tablero)


def empate(tablero):
    huecos = 0
    for i in tablero:
        for v in i:
            if v == " ":
                huecos+=1
    return huecos == 0

def partida():
    global turno, partida_terminada, tablero, jugadores
    while not partida_terminada:
        print(f"Es el turno del jugador {jugadores[turno%2]}")
        mostrar_tablero(tablero)
        hacer_jugada(jugadores[turno%2], tablero)
        
        if victoria(jugadores[turno%2], tablero):
            partida_terminada = True
            print(f"Gana el jugador {jugadores[turno%2]}")
            mostrar_tablero(tablero)
        elif empate(tablero):
            partida_terminada = True
            print("Ha habido un empate")
            mostrar_tablero(tablero)
        else:
            turno += 1
    
    
    
partida()
    

    
    


 