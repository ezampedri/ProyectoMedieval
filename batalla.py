import random as r
import json
import suerte



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
        "def": 5,
        "lk": suerte.suerte,
        "arma": 10,
        "habilidades": ["curar"]
}

enemigo = {
    "nombre": contrincante["nombre"],
    "hp": contrincante["hp"],
    "atk": contrincante["atk"],
    "def": contrincante["def"]
}


def ac_ataque(actor, vs):
    if 'arma' in actor:
        golpe = actor['atk'] * ((actor['arma']/10) + 1)
    else:
        golpe = actor['atk']
    if suerte.tirada():
        vs['hp'] -= golpe
        print(f"El ataque de {actor.get('nombre')} conectó por un total de {golpe}")
    else:
        print(f"{actor.get('nombre', 'El actor')} falló el ataque.")

ac_ataque(enemigo, heroe)