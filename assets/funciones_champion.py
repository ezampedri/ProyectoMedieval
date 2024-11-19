import keyboard
import json



def curarse(heroe, cantidad=50):
    heroe["hp"] += cantidad


def seleccionarHeroe(nombre):
    try:
        with open("assets/heroes.json", 'r') as archivo:
            data = json.load(archivo)

        heroe = data['heroe'].get(nombre)
        if heroe:
            return heroe
        else:
            print(f"No se encontró al héroe: {nombre}")
            return None
    except FileNotFoundError:
        print(f"Sigue roto, no encuentro: {archivo.name}")
        return None
    except KeyError as e:
        print(f"Error de clave: {e}")
        return None



def cargar_enemigo(nombre_enemigo):
    """
    Función para cargar un enemigo del archivo JSON.

    Parámetros:
    nombre_enemigo: Nombre del enemigo a cargar.

    Retorna:
    Un diccionario con los datos del enemigo.
    """
    try:
        with open("assets/enemigos.json", 'r') as archivo:
            data = json.load(archivo)
        enemigo = data["enemigos"].get(nombre_enemigo)

        if enemigo:
            return enemigo
        else:
            print(f"No se encontró al enemigo: {nombre_enemigo}")
            return None
    except FileNotFoundError:
        print(f"No se encontró archivo {archivo.name}")
        return None


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