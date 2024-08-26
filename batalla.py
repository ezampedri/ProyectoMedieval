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
    dado = suerte.tirada(actor.get('agi'))
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
    with open('ablt.json', 'r') as file:
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

