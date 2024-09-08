import random as r
import json
import suerte
import os

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
    "habilidades": ["Rejuvenecer", "Bola de fuego"]
}

enemigo = {
    "nombre": "Orco",
    "hp": 200,
    "atk": 15,
    "def": 7,
    "agi": 20,
    "lk": 20
}

def ac_evade(actor):
    dado = suerte.tirada(actor['agi'])
    return dado

def ac_ataque(actor, vs):
    if 'arma' in actor:
        golpe = actor['atk'] * ((actor['arma']/10) + 1)
    else:
        golpe = actor['atk']
    print(f'¡{actor["nombre"]} lanza un ataque por {golpe} de daño!')
    if ac_evade(vs):
        print(f"{vs.get('nombre')} esquivó el ataque")
    else:
        if suerte.tirada(actor['lk'] + 50):
            vs['hp'] -= golpe
            print(f"El ataque de {actor['nombre']} conectó por un total de {golpe}")
        else:
            print(f"{actor['nombre']} falló el ataque.")

def ac_magia(actor, vs, habilidad):
    with open('../ProyectoMedieval/assets/habilidades.json', 'r') as file:
        data = json.load(file)['habilidades']
    for m in data:
        if m['nombre'] == habilidad:
            daño = m['atk'] * actor['mag']
            vs['hp'] -= daño
            print(f"{actor['nombre']} lanzó {habilidad} sobre {vs['nombre']} por un total de {daño} de hp")

def interfaz(heroe, enemigo):
    os.system('cls')
    print("="*42)
    print(f"{heroe['nombre']:^20} | {enemigo['nombre']:^20}")
    print("-" * 42)
    print(f"HP: {heroe['hp']:<17} | HP: {enemigo['hp']:<20}")
    print(f"MP: {heroe['mp']:<17} | MP: {enemigo.get('mp', 'N/A'):<20}")
    print("===================================")

def escape():
    escapada = suerte.tirada((suerte.suerte // 2) + heroe['agi'])
    return escapada

def acc(heroe):
    print(f"Escribe tu acción! \n\n")
    print(f"Atacar")
    print(f"Habilidades")
    print(f"Evadir")
    print(f"Escapar")
    user = input("¡Tomá el destino en tus manos! ").lower()
    if user == "atacar":
        ac_ataque(heroe, enemigo)
    elif user == "habilidades":
        print(f"Elige una habilidad!")
        for habilidad in heroe['habilidades']:
            print(habilidad)
        user = input()
        if user in heroe['habilidades']:
            ac_magia(heroe, enemigo, user)
        else:
            print(f'Ese conjuro no forma parte del conocimiento de {heroe["nombre"]}')
    elif user == "evadir":
        print(f'{heroe["nombre"]} ¡se prepara para evadir el próximo ataque!')
        heroe['agi'] *= 2  # Dobla la agilidad temporalmente
    elif user == 'escapar':
        escape()
    else:
        print('No se reconoce el comando!')

def acc_ai(enemigo):
    acciones = ['atacar']
    #recordar que acá necesito sofisticar un poco el sistema de batalla para que algunas acciones tengan más chances de suceder que otras
    eleccion = r.choice(acciones)
    if eleccion == 'atacar':
        ac_ataque(enemigo, heroe)
    

def batalla(heroe, enemigo):
    while heroe['hp'] > 0 and enemigo['hp'] > 0:
        interfaz(heroe, enemigo)
        acc(heroe)
        input('----->')
        acc_ai(enemigo)
        input('----->')
        
        

batalla(heroe, enemigo)
