import json, time


def guardar_partida(mapa, nivel, posicionHeroe, heroe):
    data = { 
        "EstadoMapa": mapa, 
        "EstadoHeroe": heroe, 
        "EstadoNivel": nivel, 
        "EstadoPosicionHeroe": posicionHeroe
    }

    with open("assets/partida.json", 'w') as archivo:
        json.dump(data, archivo)


def cargar_partida(nombre_archivo="assets/partida.json"):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None, None, None, None #estamos trabajando con un cobolero

