import keyboard
import json



def curarse(nombre_heroe):
    """
    Funcion para curarse

    Parametros
    nombre_heore: nombre del heroe a curar

    Retorna
    Le suma 50 puntos de HP
    
    """
    with open("champions.json", 'r') as archivo:
        data = json.load(archivo)['heroe']
        for heroe in data:
            if data["nombre"] == nombre_heroe:
                heroe["hp"] +=50


def rejuvenecer(nombre_heroe):
    """
    Función para rejuvenecer.

    Parámetros:
    nombre_heroe: Nombre del héroe a rejuvenecer.

    Retorna:
    Le suma 200 puntos de MP si el héroe es Gandalf y le resta 5 puntos de HP.
    """
    with open("champions.json", 'r') as archivo:
        data = json.load(archivo)['heroe']
        for heroe in data:
            if heroe["nombre"] == nombre_heroe:
                if nombre_heroe == "Gandalf":
                    heroe["hp"] -= 5
                    heroe["mp"] += 200


def seleccionarHeroe(nombre_heroe):
    """
    Función para seleccionar un héroe del archivo JSON.
    """
    try:
        with open("../ProyectoMedieval/assets/champions.json", 'r') as archivo:
            data = json.load(archivo)

        # Acceder al héroe directamente por su nombre
        heroe = data['heroe'].get(nombre_heroe)

        if heroe:
            return heroe
        else:
            print(f"No se encontró al héroe: {nombre_heroe}")
            return None
    except FileNotFoundError:
        print(f"No se encontró archivo {archivo.name}")
        return None


#Cargar enemigo desde el json
def cargar_enemigo(enemigo):
    enemigoCargado = ''

    with open('../ProyectoMedieval/assets/champions.json', 'r') as archivo: 
        data = json.load(archivo)
        enemigoCargado = data['enemigo'].get(enemigo)

    return enemigoCargado


# U0001F47D es emoji de heroe 
def menu():
    bandera = True
    campeon = None

    while bandera:
        print()
        print()
        print('---------------------------------------------------')
        print('-               Proyecto Medieval                 -')
        print('---------------------------------------------------')
        print("Seleccionar Heroe:")
        print("1. \U0001F9D9 Gandalf - Curador")
        print("Habilidades: Rejuvenecer")
        print('---------------------------------------------------')
        print("2. \U0001F9D9 Aragorn - Guerrero")
        print("Habilidades: Corte Dimensional y Disparo Penetrante")
        print('---------------------------------------------------')
        print("3. \U0001F9D9 Morgana - Maga")
        print("Habilidades: Bola de fuego")
        print('---------------------------------------------------')
        print("4. \U0001F9D9 Legolas - Arquero")
        print("Habilidades: Corte Dimensional")
        print('---------------------------------------------------')
        print("5. Salir")
        print('---------------------------------------------------')
        opcion = int(input("Ingrese opcion: "))

        if opcion == 1:
            campeon = seleccionarHeroe('Gandalf')
            bandera=False
        elif opcion == 2:
            campeon = seleccionarHeroe('Aragorn')
            bandera=False
        elif opcion == 3:
            campeon = seleccionarHeroe('Morgana')
            bandera=False
        elif opcion == 4:
            campeon = seleccionarHeroe('Legolas')
            bandera=False
        elif opcion == 5:
            print("Saliendo del programa...")
            bandera=False
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    return campeon