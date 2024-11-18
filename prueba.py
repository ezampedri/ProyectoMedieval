import json

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

        enemigo = data.get(nombre_enemigo)

        if enemigo:
            return enemigo
        else:
            print(f"No se encontró al enemigo: {nombre_enemigo}")
            return None
    except FileNotFoundError:
        print(f"No se encontró archivo {archivo.name}")
        return None
    
print(cargar_enemigo('Goblin'))