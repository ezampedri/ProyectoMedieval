import random as r
import json
import suerte


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
        "atk": 10,
        "agi": 20,
        "def": 5,
        "lk": suerte.suerte,
        "arma": 10,
        "habilidades": ["curar"]
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



