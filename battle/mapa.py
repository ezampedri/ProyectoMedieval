import random
import keyboard
from battle import battle
from assets import champions

# U0001F7EB es tierra
# U0001F47D es heroe
# U0001F480 es contrincante
# U0001F9F1 es pared
# U0001F333 es arbol
# U0001F532 es salida

def armadoDeMapa(filas, columnas):
    #Se llena la matriz FxC con tierra lo que representa el piso del mapa
    mapa = [['\U0001F7EB' for _ in range(columnas)] for _ in range(filas)] 

    #Calculo de arboles (A) y paredes (P) para agregar
    cantidadArboles = (filas * columnas) // 5
    cantidadParedes = (filas * columnas) // 5
    cantidadContrincantes = (filas * columnas) // 7
    cantidadSalidas=1

    contadorArbolesColocados=0
    contadorParedesColocadas=0
    contadorContrincantesColocados=0
    contadorSalidasColocadas=0

    #Se colocan los arboles en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe 
    while contadorArbolesColocados < cantidadArboles:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '\U0001F7EB':  
            mapa[x][y] = '\U0001F333'
            contadorArbolesColocados+=1
            
    #Se colocan las paredes en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe
    while contadorParedesColocadas < cantidadParedes:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '\U0001F7EB':  
            mapa[x][y] = '\U0001F9F1'
            contadorParedesColocadas+=1

    #Se colocan los contrincantes en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe
    while contadorContrincantesColocados < cantidadContrincantes:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '\U0001F7EB':  
            mapa[x][y] = '\U0001F480'
            contadorContrincantesColocados+=1

    #Se colocan los salidas en posiciones random (x,y) que no coincidan con otros arboles, pared, contrincante o posicion x,y=(0,0) donde inicia el Heroe
    salida = (0, 0)
    while contadorSalidasColocadas < cantidadSalidas:
        x, y = random.randint(filas//2, filas-1), random.randint(0, columnas-1)
        if (x, y) != (0, 0) and mapa[x][y] == '\U0001F7EB':  
            mapa[x][y] = '\U0001F532'
            salida = (x, y)
            contadorSalidasColocadas+=1

    #Camino seguro: Se quitan obstaculos para que el Heroe tenga acceso a la salida y esta no quede bloqueada
    caminoSeguro = (0, 0)
    xSalida, ySalida = salida[0], salida[1]
    while caminoSeguro < salida:
        x, y = caminoSeguro[0], caminoSeguro[1]
        if x < xSalida:
            x += 1
            if mapa[x][y] != '\U0001F532':
                mapa[x][y] = '\U0001F7EB'
        elif y < ySalida:
            y += 1
            if mapa[x][y] != '\U0001F532':
                mapa[x][y] = '\U0001F7EB'
        caminoSeguro = (x, y)
        
    return mapa


#Imprimir el mapa
def imprimirMapa(mapa, posicionHeroe):
    for i, fila in enumerate(mapa):
        for j, columna in enumerate(fila):
            if (i, j) == posicionHeroe:
                print('\U0001F47D', end=' ')
            else:
                print(columna, end=' ')
        print()


#Controlar la posicion del Heroe y verificar si llego a la S(Salida) o se topo con un C(Contrincante)
def controlDePosicion(mapa, posicion, nivel):
    salidaAlcanzada = False

    if mapa[posicion[0]][posicion[1]] == '\U0001F480':
        print("¡Has encontrado un contrincante! ¡Preparate para la batalla!")
        recompensa = battle.batalla(random.choice(champions.champions['heroe']), random.choice(champions.champions['enemigos']))
        
        if recompensa['victoria'] == True:
            mapa[posicion[0]][posicion[1]] = '\U0001F7EB'
        else:
            print("¡El mundo medio ha caído!")

    if mapa[posicion[0]][posicion[1]] == '\U0001F532':
        print(f"¡Has alcanzado la salida! Nivel {nivel} completado.")
        salidaAlcanzada = True

    return salidaAlcanzada
        


#Movimiento del Heroe por el mapa
def movimientoHeroe(mapa, posicion):
    filas, columnas = len(mapa), len(mapa[0])
    move=''

    movimientos = {
        'w': (-1, 0),  # Arriba
        'a': (0, -1),  # Izquierda
        's': (1, 0),   # Abajo
        'd': (0, 1)    # Derecha
    }

    print("Moverse: w=arriba, a=izquierda, s=abajo, d=derecha")

    while move != 'w' and 'a' and 's' and 'd':    
        eventoTecla = keyboard.read_event()

        if eventoTecla.event_type == 'down':
            move = eventoTecla.name.lower()

            if move in movimientos:
                nuevaPosicion = (posicion[0] + movimientos[move][0], posicion[1] + movimientos[move][1])
                
                # Control de posición para evitar salir del mapa o moverse a un obstáculo
                if 0 <= nuevaPosicion[0] < filas and 0 <= nuevaPosicion[1] < columnas:
                    if mapa[nuevaPosicion[0]][nuevaPosicion[1]] not in ['\U0001F333', '\U0001F9F1']:
                        return nuevaPosicion
                    else:
                        print("¡Hay un obstaculo!")
                else:
                    print("¡No puedes salir del mapa!")
            else:
                print("Movimiento invalido")


# Iniciar juego 
def iniciarMapa(nivel):
    if nivel == 1:
        mapa = armadoDeMapa(10, 15)
    elif nivel == 2:
        mapa = armadoDeMapa(15, 20)
    else:
        mapa = armadoDeMapa(20, 25)

    posicionHeroe = (0, 0)
    salidaAlcanzada = False

    while salidaAlcanzada == False:
        imprimirMapa(mapa, posicionHeroe)
        posicionHeroe = movimientoHeroe(mapa, posicionHeroe)
        salidaAlcanzada=controlDePosicion(mapa, posicionHeroe, nivel)


# Continuar juego guardado
def continuarJuego(mapa, nivel, heroePosicion):
    salidaAlcanzada = False

    while salidaAlcanzada == False:
        imprimirMapa(mapa, posicionHeroe)
        posicionHeroe = movimientoHeroe(mapa, posicionHeroe)
        salidaAlcanzada=controlDePosicion(mapa, posicionHeroe, nivel)