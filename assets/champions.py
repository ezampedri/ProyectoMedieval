import keyboard
import json
import champions

def curarse(nombre_heroe):
    """
    Funcion para curarse

    Parametros
    nombre_heore: nombre del heroe a curar

    Retorna
    Le suma 50 puntos de HP
    
    """
    with open("champions.json", 'r') as archivo:
        for heroe in champions["heroe"]:
            if heroe["nombre"] == nombre_heroe:
                heroe["hp"] +=50

def rejuvenecer(nombre_heroe):
    """
    Funcion para Rejuvenecer

    Parametros
    nombre_heore: nombre del heroe a rejuvencer

    Retorna
    Le suma 200 puntos de MP
    
    """
    for heroe in champions["heroe"]:
        with open("champions.json", 'r') as archivo:
            if heroe["nombre"] == nombre_heroe:
                if nombre_heroe == "Gandalf":
                    heroe["hp"] -= 5
                    heroe["mp"] += 200


def seleccionarHeore(nombre_heroe):
    with open("champions.json", 'r') as archivo:
        data = json.load(archivo)['heroe']
        for heroe in data:
            if heroe["nombre"] == nombre_heroe:
                campeon= champions.get(nombre_heroe, {})
                return campeon
            



# U0001F47D es emoji de heroe 
def menu():
    """
    Funcion para elegir el Heroe para empezar a jugar

    Parametros
    Numero de heroe seleccionado

    Retorna
    Sin retorno.
    
    """

    while True:
        print('---------------------------------------------------')
        print('- Proyecto Medieval -------------------------------')
        print('---------------------------------------------------')
        print("\nSeleccionar Heroe:")
        print("1. \U0001F47D Gandalf - Curador")
        print('---------------------------------------------------')
        print("Habilidades: Rejuvenecer")
        print("\n2. \U0001F47D Aragorn - Guerrero")
        print('---------------------------------------------------')
        print("Habilidades: Corte Dimensional y Disparo Penetrante")
        print("\n3. \U0001F47D Morgana - Maga")
        print('---------------------------------------------------')
        print("Habilidades: Bola de fuego")
        print("\n4. \U0001F47D Legolas - Arquero")
        print('---------------------------------------------------')
        print("Habilidades: Corte Dimensional")
        print("\n5. Salir")
        print('---------------------------------------------------')
        print("Elija una opción:")
        opcion = keyboard.read_event()
        if opcion == '1':
            seleccionarHeore('Gandalf')
        elif opcion == '2':
            seleccionarHeore('Aragorn')
        elif opcion == '3':
            seleccionarHeore('Morgana')
        elif opcion == '4':
            seleccionarHeore('Legolas')
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


