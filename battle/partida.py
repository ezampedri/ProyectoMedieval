import json

partida=[]

historial_partidas = []

def guardar_partida(partida, nombre_archivo="partida.json"):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(partida, archivo, indent=4)

def cargar_partida(nombre_archivo="partida.json"):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)
    
def actualizar_y_guardar(partida, historial, nombre_archivo="partida.json"):
    historial.append(partida.copy())  
    with open(nombre_archivo, 'w') as archivo:
        json.dump(historial, archivo, indent=4)
        
def cargar_historial(nombre_archivo="partida.json"):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)