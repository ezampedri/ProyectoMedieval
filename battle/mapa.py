import random
from types import NoneType
import keyboard
from assets import funciones_champion
import time as t
from colorama import Fore, Style
import os
from battle import partida
from battle import battle
import msvcrt


# U0001F7EB es tierra
# U0001F9D9 es heroe
# U0001F480 es contrincante
# U0001F9F1 es pared
# U0001F333 es arbol
# U0001F532 es salida


mapaGuardado = None
nivelGuardado = None
posicionHeroeGuardado = None
heroeGuardado = None

def limpiarBuffer():
    msvcrt.getch()

def imprimirGameOver():
    with open('assets/game_over.txt', 'r') as file:
        for line in file:
            print(line, end='')


def armadoDeMapa(filas, columnas, nivel):
    #Se llena la matriz FxC con tierra lo que representa el piso del mapa
    mapa = [['\U0001F7EB' for _ in range(columnas)] for _ in range(filas)] 

    #Calculo de arboles (A) y paredes (P) para agregar
    cantidadArboles = (filas * columnas) // 6
    cantidadParedes = (filas * columnas) // 6
    cantidadContrincantes = (filas * columnas) // 7
    cantidadSalidas=1

    contadorArbolesColocados=0
    contadorParedesColocadas=0
    contadorContrincantesColocados=0
    contadorSalidasColocadas=0

    if nivel != 4:
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

        #Se colocan los contrincantes en posiciones random (x,y) que no coincidan con otros arboles, pared o posicion x,y=(0,0) donde inicia el Heroe
        while contadorContrincantesColocados < cantidadContrincantes:
            x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
            if (x, y) != (0, 0) and mapa[x][y] == '\U0001F7EB' and mapa[x][y] != '\U0001F532':  
                mapa[x][y] = '\U0001F480'
                contadorContrincantesColocados+=1
    else:
        mapa = [['\U0001F9F1' for _ in range(columnas)] for _ in range(filas)]
        mapa[1][2] = '\U0001F7EB'
        mapa[2][2] = '\U0001F480' #Jefe final
        mapa[3][2] = '\U0001F532' #Salida
        
    return mapa


#Imprimir el mapa
def imprimirMapa(mapa, posicionHeroe):
    print('\n')
    for i, fila in enumerate(mapa):
        for j, columna in enumerate(fila):
            if (i, j) == posicionHeroe:
                print('\U0001F9D9', end=' ')
            else:
                print(columna, end=' ')
        print()


#Controlar la posicion del Heroe y verificar si llego a la S(Salida) o se topo con un C(Contrincante)
def controlDePosicion(mapa, posicion, nivel):
    salidaAlcanzada = False

    try:
        if mapa[posicion[0]][posicion[1]] == '\U0001F480':
            if nivel == 1:
                enemigo = funciones_champion.cargar_enemigo('Goblin Travieso')
                print()
                battle.generar_texto("¡Un Goblin escurridizo aparece de entre las sombras! Su risa burlona resuena mientras te prepara una trampa \n")
            elif nivel == 2:
                enemigo = funciones_champion.cargar_enemigo('Orco Guardian')
                print()
                battle.generar_texto("Un imponente Orco emerge del bosque, blandiendo su enorme hacha con una mirada desafiante. ¡Prepárate para una batalla brutal contra este coloso!\n")
            elif nivel == 3:
                enemigo = funciones_champion.cargar_enemigo('Troll Quejumbroso')
                print()
                battle.generar_texto("El suelo tiembla bajo tus pies mientras un Troll gigantesco avanza lentamente hacia ti. Su gruñido profundo anuncia un combate feroz. \n")
            elif nivel == 4:
                enemigo = funciones_champion.cargar_enemigo('Drafnakk, Tirano de Gyanavall')
                print()
                battle.generar_texto("El suelo tiembla y un rugido estremecedor rompe el silencio. ¡Has desafiado a Drafnakk, el Tirano de Gyanavall! No habrá escapatoria... Esta será la batalla de tu vida. \n")

            global heroeGuardado
            recompensa = battle.batalla(heroeGuardado, enemigo)

            if recompensa['victoria'] == True:
                progreso(recompensa)
                mapa[posicion[0]][posicion[1]] = '\U0001F7EB'
            else:
                battle.generar_texto("¡El mundo ha caído!")
                print()
                imprimirGameOver()
                exit()

        if mapa[posicion[0]][posicion[1]] == '\U0001F532':
            print()
            print(f"¡Has alcanzado la salida! Nivel {nivel} completado.")
            salidaAlcanzada = True

        return salidaAlcanzada, mapa
    
    except SystemExit:
        exit()
    except BaseException:
        print()
        print('Movimiento invalido')
        return salidaAlcanzada, mapa
        


#Movimiento del Heroe por el mapa
def movimientoHeroe(mapa, posicion, nivel):
    filas, columnas = len(mapa), len(mapa[0])
    move=''

    movimientos = {
        'w': (-1, 0),  # Arriba
        'a': (0, -1),  # Izquierda
        's': (1, 0),   # Abajo
        'd': (0, 1)    # Derecha
    }

    print("Moverse: w=arriba, a=izquierda, s=abajo, d=derecha. M=Menu Contextual")

    while move != 'w' and 'a' and 's' and 'd':    
        eventoTecla = keyboard.read_event()

        if eventoTecla.event_type == 'down':
            move = eventoTecla.name.lower()
            limpiarBuffer()

            if move in movimientos:
                nuevaPosicion = (posicion[0] + movimientos[move][0], posicion[1] + movimientos[move][1])
                
                # Control de posición para evitar salir del mapa o moverse a un obstáculo
                if 0 <= nuevaPosicion[0] < filas and 0 <= nuevaPosicion[1] < columnas:
                    if mapa[nuevaPosicion[0]][nuevaPosicion[1]] not in ['\U0001F333', '\U0001F9F1']:
                        return nuevaPosicion
                    else:
                        print()
                        print("¡Hay un obstaculo!")
                        nuevaPosicion = posicion
                        return nuevaPosicion
                else:
                    print()
                    print("¡No puedes salir del mapa!")
                    nuevaPosicion = posicion
                    return nuevaPosicion
            else:
                if move == 'm':
                    menuContextual(mapa, posicion, nivel)
                else:
                    print()
                    print("Movimiento invalido")

    

def menuContextual(mapa, posicion, nivel):
        salirWhile = False
        while salirWhile == False:
            print('---------------------')
            print('-  Menu contextual  -')
            print('---------------------')
            print('1) Guardar Juego     ')
            print('2) Exit              ')
            print('---------------------')
            try:
                opcion=int(input('Ingrese una opcion:'))

                if opcion == 1:
                    global mapaGuardado, nivelGuardado, posicionHeroeGuardado, heroeGuardado
                    mapaGuardado = mapa
                    nivelGuardado = nivel
                    posicionHeroeGuardado = posicion
                    partida.guardar_partida(mapaGuardado, nivelGuardado, posicionHeroeGuardado, heroeGuardado)
                    limpiarBuffer()
                    print()
                    print('Partida guardada exitosamente. Mueva el heroe para continuar el juego')
                    salirWhile = True
                elif opcion == 2:
                    exit()
                else:
                    print()
                    print('Opcion invalida')
            except ValueError:
                print()
                print('Opcion invalida')


# Iniciar juego 
def iniciarMapa(nivel, heroe, restaurar):
    global heroeGuardado 
    heroeGuardado = heroe
    posicionHeroe = (0, 0)
    salidaAlcanzada = False

    if nivel == 1:
        mapa = armadoDeMapa(10, 15, nivel)
    elif nivel == 2:
        mapa = armadoDeMapa(15, 20, nivel)
    elif nivel == 3:
        mapa = armadoDeMapa(20, 25, nivel)
    else:
        mapa = armadoDeMapa(5, 5, nivel)
        posicionHeroe = (0, 2)

    if restaurar == True:
        global mapaGuardado, nivelGuardado, posicionHeroeGuardado
        mapa = mapaGuardado
        nivel = nivelGuardado
        heroe = heroeGuardado
        posicionHeroe = tuple(posicionHeroeGuardado)

    while salidaAlcanzada == False:
        imprimirMapa(mapa, posicionHeroe)
        posicionHeroe = movimientoHeroe(mapa, posicionHeroe, nivel)
        salidaAlcanzada, mapa = controlDePosicion(mapa, posicionHeroe, nivel)


# Iniciar juego guardado
def iniciarJuegoGuardado(mapa, nivel, heroe, posicionHeroe):
    global mapaGuardado, nivelGuardado, heroeGuardado, posicionHeroeGuardado
    mapaGuardado = mapa
    nivelGuardado = nivel
    heroeGuardado = heroe
    posicionHeroeGuardado = posicionHeroe
    iniciarMapa(nivel, heroe, True)


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
    rojas = [ra, rd, rb, ri]

    va = Fore.GREEN + arriba + Style.RESET_ALL   # Arriba verde
    vb = Fore.GREEN + abajo + Style.RESET_ALL     # Abajo verde
    vd = Fore.GREEN + derecha + Style.RESET_ALL    # Derecha verde
    vi = Fore.GREEN + izquierda + Style.RESET_ALL   # Izquierda verde
    verdes = [va, vd, vb, vi]

    aa = Fore.YELLOW + arriba + Style.RESET_ALL   # Arriba amarillo
    ab = Fore.YELLOW + abajo + Style.RESET_ALL     # Abajo amarillo
    ad = Fore.YELLOW + derecha + Style.RESET_ALL    # Derecha amarillo
    ai = Fore.YELLOW + izquierda + Style.RESET_ALL   # Izquierda amarillo
    azules = [aa, ad, ab, ai]

    solucion = [
        [vd, rb, ra],  # Fila 0
        [va, ab, aa],  # Fila 1
        [ai, rd, vd]   # Fila 2
    ]

    puzzle = [
        [vi, ri, rd],  # Fila 0
        [vb, ai, ad],  # Fila 1
        [aa, rb, vi]   # Fila 2
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
        print("Resuelve el puzzle para abrir la puerta, debes crear un camino de flechas hacía el otro lado.")
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
        os.system('cls')

    for fila in puzzle:
        print(" ".join(fila))


    battle.generar_texto("Las magníficas puertas de la sala del trono se abren para ti, eres digno.")
    t.sleep(3)
    return funciones_champion.curarse(heroeGuardado, 100)

 
def progreso(recompensa):
    global heroeGuardado
    heroeGuardado['exp'] += recompensa['xp']
    if heroeGuardado['exp'] > 100:
        battle.generar_texto('Sientes una gran fuerza aflorando desde tu interior\n')
        heroeGuardado['hp'] = int(heroeGuardado['hp'] * 1.15)
        heroeGuardado['mp'] += 30
        heroeGuardado['atk'] = int(heroeGuardado['atk'] * 1.10)
        heroeGuardado['mag'] = int(heroeGuardado['mag'] * 1.10)
        heroeGuardado['agi'] = int(heroeGuardado['agi'] * 1.10)
        heroeGuardado['def'] = int(heroeGuardado['def'] * 1.10)
        heroeGuardado['lk'] = int(heroeGuardado['lk'] * 1.10)
        heroeGuardado['exp'] = 0  # Resetear la experiencia después de subir de nivel