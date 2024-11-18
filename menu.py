from battle import mapa
from battle import partida
from assets import funciones_champion
import os
import sys
import time as tm

def generar_texto(texto, velocidad= 0.02):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        tm.sleep(velocidad)
    print()



def imprimir_portada():
    with open('assets/portada.txt', 'r') as file:
        for line in file:
            print(line, end='')


with open('assets/tutorial.txt', 'r') as file:
    tutorial = file.read()

# Punto de entrada al juego
def main():
    while True:
        imprimir_portada()
        try:
            opcion=int(input('Ingrese una opcion: '))

            if opcion == 1:
                heroe = funciones_champion.menu()

                if heroe != None:
                    mapa.iniciarMapa(1, heroe, False)
                    mapa.iniciarMapa(2, heroe, False)
                    mapa.minijuego_cerradura()
                    mapa.iniciarMapa(3, heroe, False)
                else:
                    print('No ha seleccionado heroe')
            elif opcion == 2:
                partidaGuardada=partida.cargar_partida()
                mapa.iniciarJuegoGuardado(partidaGuardada['EstadoMapa'], partidaGuardada['EstadoNivel'], partidaGuardada['EstadoHeroe'], partidaGuardada['EstadoPosicionHeroe'])
            elif opcion == 3:
                generar_texto(tutorial)
                tm.sleep(5)
            elif opcion == 4:
                exit()
            else:
                os.system('cls')
                print('Opcion invalida')
        except ValueError:
            os.system('cls')
            print('Opcion invalida')


# Invocación de main
main()