import random
import keyboard

def armadoDeMapa(filas, columnas):
    #Se llena la matriz FxC con '.' lo que representa el piso del mapa
    mapa = [['.' for _ in range(columnas)] for _ in range(filas)] 

    #Calculo de arboles (A) y paredes (P) para agregar
    cantidadArboles = (filas * columnas) // 5
    cantidadParedes = (filas * columnas) // 5
    cantidadContrincantes=5
    cantidadSalidas=1

    contadorArbolesColocados=0
    contadorParedesColocadas=0
    contadorContrincantesColocados=0
    contadorSalidasColocadas=0

    #Se colocan los arboles en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe 
    while contadorArbolesColocados < cantidadArboles:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '.':  
            mapa[x][y] = 'A'
            contadorArbolesColocados+=1
            
    #Se colocan las paredes en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe
    while contadorParedesColocadas < cantidadParedes:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '.':  
            mapa[x][y] = 'P'
            contadorParedesColocadas+=1

    #Se colocan los contrincantes en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe
    while contadorContrincantesColocados < cantidadContrincantes:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '.':  
            mapa[x][y] = 'C'
            contadorContrincantesColocados+=1

    #Se colocan los salidas en posiciones random (x,y) que no coincidan con otros arboles, pared, contrincante o posicion x,y=(0,0) donde inicia el Heroe
    salida = (0, 0)
    while contadorSalidasColocadas < cantidadSalidas:
        x, y = random.randint(filas//2, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '.':  
            mapa[x][y] = 'S'
            salida = (x, y)
            contadorSalidasColocadas+=1

    #Camino seguro: Se quitan obstaculos para que el Heroe tenga acceso a la salida y esta no quede bloqueada
    caminoSeguro = (0, 0)
    xSalida, ySalida = salida[0], salida[1]
    while caminoSeguro < salida:
        x, y = caminoSeguro[0], caminoSeguro[1]
        if x < xSalida:
            x += 1
            if mapa[x][y] != 'S':
                mapa[x][y] = '.'
        elif y < ySalida:
            y += 1
            if mapa[x][y] != 'S':
                mapa[x][y] = '.'
        caminoSeguro = (x, y)
        
    return mapa


#Imprimir el mapa
def imprimirMapa(mapa, posicionHeroe):
    for i, fila in enumerate(mapa):
        for j, columna in enumerate(fila):
            if (i, j) == posicionHeroe:
                print('H', end=' ')
            else:
                print(columna, end=' ')
        print()


#Controlar la posicion del Heroe y verificar si llego a la S(Salida) o se topo con un C(Contrincante)
def controlDePosicion(mapa, posicion):
    if mapa[posicion[0]][posicion[1]] == 'C':
        print("¡Has encontrado un contrincante! ¡Preparate para la batalla!")

    if mapa[posicion[0]][posicion[1]] == 'S':
        print("¡Has alcanzado la salida! Nivel completado.")
        exit()


#Movimiento del Heroe por el mapa
def movimientoHeroe(mapa, posicion):
    filas, columnas = len(mapa), len(mapa[0])

    movimientos = {
        'w': (-1, 0),  # Arriba
        's': (1, 0),   # Abajo
        'a': (0, -1),  # Izquierda
        'd': (0, 1)    # Derecha
    }

    print("Moverse: w=arriba, s=abajo, a=izquierda, d=derecha")
    move = input("Elige un movimiento: ").lower()

    if move in movimientos:
        nuevaPosicion = (posicion[0] + movimientos[move][0], posicion[1] + movimientos[move][1])
        
        # Control de posición para evitar salir del mapa o moverse a un obstáculo
        if 0 <= nuevaPosicion[0] < filas and 0 <= nuevaPosicion[1] < columnas:
            if mapa[nuevaPosicion[0]][nuevaPosicion[1]] not in ['A', 'P']:
                return nuevaPosicion
            else:
                print("¡Hay un obstaculo!")
                return posicion
        else:
            print("¡No puedes salir del mapa!")
            return posicion
    else:
        print("Movimiento invalido")
        return posicion


#Iniciar mapa 
def iniciarMapa():
    mapa = armadoDeMapa(10, 10)
    posicionHeroe = (0, 0)

    while True:
        imprimirMapa(mapa, posicionHeroe)
        posicionHeroe = movimientoHeroe(mapa, posicionHeroe)
        controlDePosicion(mapa, posicionHeroe)