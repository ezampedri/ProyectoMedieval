from colorama import Fore, Style
import os

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
        for fila in puzzle:
            print(" ".join(fila))
        
        print("solucion")
        for fila in solucion:
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


    print("Las magníficas puertas de la sala del trono se abren para ti, eres digno.")
    
minijuego_cerradura()