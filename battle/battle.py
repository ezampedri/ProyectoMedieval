import random as r
import json
import suerte
import os



#el json trae a los enemigos desde la 'base de datos'
with open('actors.json', 'r') as file:
    data = json.load(file)

ruta_pj = 'actors.json'
ruta_hab = 'ablt.json'
enemigo = data['enemigos']
contrincante = r.choice(enemigo)

heroe = {
        'nombre': 'Aiken',
        "hp": 270,
        "mp": 40,
        "atk": 10,
        "mag": 5,
        "agi": 20,
        "def": 5,
        "lk": suerte.suerte,
        "arma": 10,
        "habilidades": ["curar", "fuego"]
}

enemigo = {
    "nombre": contrincante["nombre"],
    "hp": contrincante["hp"],
    "atk": contrincante["atk"],
    "agi": contrincante["agi"],
    "def": contrincante["def"]
}

#esta función la voy a diseñar para usar después de cada ataque, para dar una tirada de suerte con chance de evitar el daño
def ac_evade(actor):
    dado = suerte.tirada(actor['agi'])
    return dado


def ac_ataque(actor, vs):
    if 'arma' in actor:
        golpe = actor['atk'] * ((actor['arma']/10) + 1)
    else:
        golpe = actor['atk']
    print(f'¡{actor} lanza un ataque por {golpe} de daño!')
    if ac_evade(vs):
        print(f"{vs.get('nombre')} esquivó el ataque")
    else:
        if suerte.tirada(suerte.suerte+50):
            vs['hp'] -= golpe
            print(f"El ataque de {actor.get('nombre')} conectó por un total de {golpe}")
        else:
            print(f"{actor.get('nombre')} falló el ataque.")

#para la magia va a ser un poco más complicado, se tienen que pasar el argumento del heroe, el vs, y la magia en cuestión
def ac_magia(actor, vs, habilidad):
    with open('habilidades.json', 'r') as file:
        data = json.load(file)['habilidades']
    for m in data:
        if m['nombre'] == habilidad:
            daño = m['atk'] * actor['mag']
            vs['hp'] -= daño
            print(f"{actor['nombre']} lanzó {habilidad} sobre {vs['nombre']} por un total de {daño} de hp")

#función para mostrar el cuadro con la vida actual del personaje y la del contrincante
def interfaz(heroe, enemigo):
    os.system('cls')
    print("="*42)
    print(f"{heroe['nombre']:^20} | {enemigo['nombre']:^20}")
    print("-" * 42)
    print(f"HP: {heroe['hp']:<17} | HP: {enemigo['hp']:<20}")
    print(f"MP: {heroe['mp']:<17} | MP: {enemigo.get('mp', 'N/A'):<20}")
    print("===================================")

#esta función termina la batalla sin recompensa
def escape():
    escapada = suerte.tirada((suerte.suerte//2)+heroe['agi'])
    return escapada


def acc(heroe, enemigo):
    bandera= True
    while bandera:
        interfaz(heroe, enemigo)
        print(f"\n \n Escribe tu acción!")
        print(f"Atacar")
        print(f"Habilidades")
        print(f"Evadir")
        print(f"Escapar")
        user= input("¡Tomá el destino en tus manos! ")
        if user.lower == "atacar":
            ac_ataque(heroe, enemigo)
        elif user.lower == "habilidades":
            print(f"Elige una habilidad!")
            for habilidad in heroe['habilidades']:
                print(habilidad)
            user = input()
            while True:
                for habilidad in heroe['habilidades']:
                    if user == habilidad:
                        ac_magia(habilidad)
                        break #acá uso break para que Juli me diga si este es un buen uso del break o no
                    else:
                        print(f'Ese conjuro no forma parte del conocimiento de {heroe}')
        elif user.lower == "evadir":
            print(f'{heroe} ¡se prepara para evadir el próximo ataque!')    
            heroe['agi'] * 2 #recordar dividir este parámetro después de que pase el turno en el módulo principal de batalla
        elif user.lower == 'escapar':
            escape()
        else:
            print('No se reconoce el comando!')