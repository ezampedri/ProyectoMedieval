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

def ac_evade(actor, vs):
    probabilidad_evade = actor['agi'] - vs['agi']  # Comparar agilidad entre ambos
    return r.randint(0, 100) < probabilidad_evade  # Si es menor que el umbral, esquiva

def calcular_daño(actor, vs):
    # Si el actor tiene un arma, el daño será ajustado según el valor del arma
    if 'arma' in actor:
        daño_base = actor['atk'] * ((actor['arma'] / 10) + 1)
    else:
        daño_base = actor['atk']
    
    # Multiplicador de daño crítico
    critico = r.choice([1.5, 1.75, 2.0])  # Valores posibles para ataque crítico
    
    if r.randint(0, 100) < actor['lk']:  # Probabilidad de crítico basada en la suerte
        print(f"¡Ataque crítico de {actor['nombre']}!, ¡esto va a doler!")
        daño_base *= critico  # Aplicamos el multiplicador de crítico
    
    # Daño neto después de aplicar la defensa del enemigo
    daño_neto = max(0, daño_base - vs['def'])  # El daño no puede ser menor que 0
    return daño_neto

def ac_ataque(actor, vs):
    # Calcula el daño potencial
    daño = calcular_daño(actor, vs)
    
    if daño is None:  # Verificación extra para asegurar que no sea None
        daño = 0
    
    print(f'¡{actor["nombre"]} lanza un ataque con {daño} de daño potencial!')

    # Verifica si el oponente esquiva
    if ac_evade(vs, actor):
        print(f"{vs['nombre']} esquivó el ataque de {actor['nombre']}!")
    else:
        # Comprueba si el ataque conecta, basándose en la suerte del actor
        if suerte.tirada(actor['lk'] + 50):  # Modifica la probabilidad de acierto
            vs['hp'] -= daño  # Asegurarse que `daño` es un número válido
            print(f"El ataque de {actor['nombre']} conectó e infligió {daño} de daño a {vs['nombre']}.")
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
    print("="*42)
    print(f"{heroe['nombre']:^20} | {enemigo['nombre']:^20}")
    print("-" * 42)
    print(f"HP: {heroe['hp']:<17} | HP: {enemigo['hp']:<20}")
    print(f"MP: {heroe['mp']:<17} | MP: {enemigo.get('mp', 'N/A'):<20}")
    print("===================================")

def escape():
    escapada = suerte.tirada((suerte.suerte // 2) + heroe['agi'])
    return escapada

#función que maneja todas las acciones posibles del jugador.
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

#función que maneja todos los ataques del enemigo.
def acc_ai(enemigo):
    acciones = ['atacar']
    media_vida = enemigo['hp'] //2
    # Si el enemigo tiene la habilidad 'curar' y su HP es menor a 50, agregar la opción de curar
    if enemigo['hp'] < media_vida and 'curar' in enemigo['habilidades']:
        acciones.append('curar')
    
    eleccion = r.choice(acciones)
    if eleccion == 'atacar':
        ac_ataque(enemigo, heroe)
    elif eleccion == 'curar':
        ac_magia(enemigo, enemigo, 'curar')  # El enemigo se cura a sí mismo
    

#esto encapsula todas las funciones en un solo llamado para ejecutar el programa.
def batalla(heroe, enemigo):
    while heroe['hp'] > 0 and enemigo['hp'] > 0:
        interfaz(heroe, enemigo)
        acc(heroe)
        input('----->')
        os.system('cls')
        interfaz(heroe, enemigo)
        acc_ai(enemigo)
        input('----->')
        os.system('cls')
    if enemigo['hp'] <= 0:
        recompensa = {
            'victoria': True,
            'xp':r.randint(20, 70)
        }
    else:
        recompensa ={
            'victoria' : False,
            'xp' : 0
        }
    return recompensa



batalla(heroe, enemigo)