from battle import mapa
from assets import partida

# Punto de entrada al juego
def main():
    while True:
        print('---------------------')
        print('- Proyecto Medieval -')
        print('---------------------')
        print('1) Iniciar Juego     ')
        print('2) Continuar         ')
        print('3) Reglas del juego  ')
        print('4) Exit              ')
        print('---------------------')

        try:
            opcion=int(input('Ingrese una opcion:'))

            if opcion == 1:
                mapa.iniciarMapa(1)
                mapa.iniciarMapa(2)

                #Aquí iría el minijuego de Alan
                mapa.iniciarMapa(3)
            elif opcion == 2:
                print('Continuar juego guardado')
                #mapa.continuarJuego(mapaGuardado, nivelGuardado, posicionHeroeGuardado)
            elif opcion == 3:
                print('''             
                    Primera vez jugando RPG?

                    En primera instancia, el juego ofrece 4 ¨clases¨ de personajes para elegir: Aragorn, Legolas, Morgana y Gandalf.
                    Cada uno de ellos tiene habilidades distintas para desempeñar un rol unico, Guerrero, Arquero, Mago y Healer.
                    A su vez, tienen estadisticas base repartidas de forma acorde al rol que cumple cada ¨clase¨
                    
                    El juego consta de 3 mapas, donde deberemos pelear con distintos enemigos hata llegar al 3er 
                    y ultimo mapa donde tendremos la pelea con el jefe final, comunmente conocido como ¨BOSS¨.
                    
                    El modo de pelea sera un combate por turnos que esta basado en un sistema de tirada de dados donde el que saque el mayor 
                    numero podra efectuar su habilidad exitosamente.
                    
                    Sacar un numero alto o bajo, dependera directamente de la estadistica ¨lk¨ (suerte), donde a mayor ¨lk¨ mayor probabilidad 
                    tendremos de lanzar una habulidad de forma exitosa.
                    
                    Glosario:
                    hp: puntos de vida
                    mp: puntos de energia
                    atk: puntos de ataque
                    mag: puntos de ataque mágico
                    def: puntos de defensa
                    lk: puntos de suerte
                    exp: contador de experiencia
                    habilidades: lo que hace cada personaje.                
                    ''')
            elif opcion == 4:
                exit()
            else:
                print('Opcion invalida')
        except ValueError:
            print('Opcion invalida')


# Invocación de main
main()