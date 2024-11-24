from battle import mapa
from battle import partida
from assets import funciones_champion
import keyboard
import os
import sys
import time as tm

def generar_texto(texto, velocidad=0.02):
    for caracter in texto:
        if keyboard.is_pressed('space'):
            sys.stdout.write(caracter)
            sys.stdout.flush()
            tm.sleep(0.000000001)  # Tiempo muy rápido para que sea imperceptible
        else:
            sys.stdout.write(caracter)
            sys.stdout.flush()
            tm.sleep(velocidad)


def imprimir_portada():
    with open('assets/portada.txt', 'r') as file:
        for line in file:
            print(line, end='')


with open('assets/tutorial.txt', 'r', encoding='utf-8') as file:
    tutorial = file.read()

with open('assets/intro.txt', 'r', encoding='utf-8') as file:
    intro = file.read()


# Punto de entrada al juego
def main():
    while True:
        os.system('cls')
        imprimir_portada()
        try:
            print()
            print()
            opcion=int(input('Ingrese una opcion: '))

            if opcion == 1:
                heroe = funciones_champion.menu()
                generar_texto(intro)
                print('\n')
                input('Presione enter para continuar...')

                if heroe != None:
                    mapa.iniciarMapa(1, heroe, False)
                    mapa.iniciarMapa(2, heroe, False)
                    mapa.iniciarMapa(3, heroe, False)
                    mapa.minijuego_cerradura()
                    mapa.iniciarMapa(4, heroe, False)
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