import random
import keyboard
from colorama import Fore, Style
import battle

# U0001F7EB es tierra
# U0001F47D es heroe
# U0001F480 es contrincante
# U0001F9F1 es pared
# U0001F333 es arbol
# U0001F532 es salida

def armadoDeMapa(filas, columnas):
    #Se llena la matriz FxC con '.' lo que representa el piso del mapa
    mapa = [['\U0001F7EB' for _ in range(columnas)] for _ in range(filas)] 

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
def controlDePosicion(mapa, posicion):
    if mapa[posicion[0]][posicion[1]] == '\U0001F480':
        print("¡Has encontrado un contrincante! ¡Preparate para la batalla!")

    if mapa[posicion[0]][posicion[1]] == '\U0001F532':
        print("¡Has alcanzado la salida! Nivel completado.")
        exit()


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


#Iniciar mapa 
def iniciarMapa():
    mapa = armadoDeMapa(10, 10)
    posicionHeroe = (0, 0)

    while True:
        imprimirMapa(mapa, posicionHeroe)
        posicionHeroe = movimientoHeroe(mapa, posicionHeroe)
        controlDePosicion(mapa, posicionHeroe)


def minijuego_cerradura():
    # Guarda en memoria las flechas para trabajarlas más fácil
    izquierda = "←"
    arriba = "↑" 
    derecha = "→" 
    abajo = "↓"
    
    # Crear todas sus variantes
    ra = Fore.RED + arriba + Style.RESET_ALL    # Arriba rojo
    rb = Fore.RED + abajo + Style.RESET_ALL     # Abajo rojo
    rd = Fore.RED + derecha + Style.RESET_ALL    # Derecha rojo
    ri = Fore.RED + izquierda + Style.RESET_ALL   # Izquierda rojo
    rojas = [ra, rb, rd, ri]

    va = Fore.GREEN + arriba + Style.RESET_ALL   # Arriba verde
    vb = Fore.GREEN + abajo + Style.RESET_ALL     # Abajo verde
    vd = Fore.GREEN + derecha + Style.RESET_ALL    # Derecha verde
    vi = Fore.GREEN + izquierda + Style.RESET_ALL   # Izquierda verde
    verdes = [va, vb, vd, vi]

    aa = Fore.YELLOW + arriba + Style.RESET_ALL   # Arriba amarillo
    ab = Fore.YELLOW + abajo + Style.RESET_ALL     # Abajo amarillo
    ad = Fore.YELLOW + derecha + Style.RESET_ALL    # Derecha amarillo
    ai = Fore.YELLOW + izquierda + Style.RESET_ALL   # Izquierda amarillo
    azules = [aa, ab, ad, ai]

    solucion = [
        [vd, rb, ri],  # Fila 0
        [va, aa, aa],  # Fila 1
        [ai, rd, vd]   # Fila 2
    ]

    puzzle = [
        [vi, ri, rb],  # Fila 0
        [vb, ai, ai],  # Fila 1
        [ad, ra, vi]   # Fila 2
    ]

    def girar_flechas(color):
        posiciones = []
        for i, fila in enumerate(puzzle):
            for j, celda in enumerate(fila):
                if celda in color:
                    posiciones.append((i, j))

        # Ciclar los colores en las posiciones encontradas
        for i, j in posiciones:
            color_actual = puzzle[i][j]
            try:
                # Intentar obtener el índice del color actual
                indice_actual = color.index(color_actual)
                # Calcular el índice del siguiente color (circular)
                siguiente_indice = indice_actual + 1
                puzzle[i][j] = color[siguiente_indice]
            except IndexError:
                puzzle[i][j] = color[0]

    while puzzle != solucion:
        # Imprimir el puzzle
        for fila in puzzle:
            print(" ".join(fila))
        
        user = input("Ingresa un color para mover(V/R/A): ").lower()
        if user == "v":
            girar_flechas(verdes)
        elif user == "r":
            girar_flechas(rojas)
        elif user == "a":
            girar_flechas(azules)
        else:
            print("Entrada no válida. Por favor, ingresa 'V', 'R' o 'A'.")

    for fila in puzzle:
        print(" ".join(fila))
    print("Las magníficas puertas de la sala del trono se abren para ti, eres digno.")

    return True


imprimirMapa(armadoDeMapa(), ("0,0)")