import json, time

partida_data=[]

historial_partidas_data = []

def guardar_partida(partida):
    with open("partida.json", 'w') as archivo:
        json.dump(partida, archivo, indent=4)

def cargar_partida(nombre_archivo="partida.json"):
    try:
        
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return partida_data
    
def actualizar_y_guardar(partida, historial):
    historial.append(partida.copy())  
    with open("partida.json", 'w') as archivo:
        json.dump(historial, archivo, indent=4)
        
def cargar_historial():
    with open("partida.json", 'r') as archivo:
        return json.load(archivo)
    

current_save = cargar_partida()

##in progress
##while True:
   ## guardar_partida()