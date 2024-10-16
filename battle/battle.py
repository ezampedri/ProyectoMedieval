import random as r
import json
from assets import suerte
import os
import time as tm
import sys


def generar_texto(texto, velocidad= 0.02):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        tm.sleep(velocidad)
    print()

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
        generar_texto(f"¡Ataque crítico de {actor['nombre']}!, ¡esto va a doler!",0.03)
        daño_base *= critico  # Aplicamos el multiplicador de crítico
    
    # Daño neto después de aplicar la defensa del enemigo
    daño_neto = max(0, daño_base - vs['def'])  # El daño no puede ser menor que 0
    return daño_neto

def ac_ataque(actor, vs):
    # Calcula el daño potencial
    daño = calcular_daño(actor, vs)
    
    if daño is None:  # Verificación extra para asegurar que no sea None
        daño = 0
    # Verifica si el oponente esquiva
    if ac_evade(vs, actor):
        generar_texto(f"{vs['nombre']} esquivó el ataque de {actor['nombre']}!")
    else:
        # Comprueba si el ataque conecta, basándose en la suerte del actor
        if suerte.tirada(actor['lk'] + 50):  # Modifica la probabilidad de acierto
            vs['hp'] -= daño  # Asegurarse que `daño` es un número válido
            generar_texto(f"El ataque de {actor['nombre']} conectó e infligió {daño} de daño a {vs['nombre']}.")
        else:
            generar_texto(f"{actor['nombre']} falló el ataque.")

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

def escape(heroe):
    escapada = suerte.tirada((suerte.suerte // 2) + heroe['agi'])
    return escapada

#función que maneja todas las acciones posibles del jugador.
def acc(heroe, enemigo):
    print(f"Escribe tu acción! \n\n")
    print(f"Atacar")
    print(f"Habilidades")
    print(f"Evadir")
    print(f"Escapar")
    generar_texto("¡Toma el destino en tus manos!")
    user = input().lower()
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
            generar_texto(f'Ese conjuro no forma parte del conocimiento de {heroe["nombre"]}')
    elif user == "evadir":
        generar_texto(f'{heroe["nombre"]} ¡se prepara para evadir el próximo ataque!')
        heroe['agi'] *= 2  # Dobla la agilidad temporalmente
    elif user == 'escapar':
        escape(heroe)
    else:
        generar_texto('No se reconoce el comando!')

#función que maneja todos los ataques del enemigo.
def acc_ai(enemigo, heroe):
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
        acc(heroe, enemigo)
        tm.sleep(1.5)
        os.system('cls')
        interfaz(heroe, enemigo)
        acc_ai(enemigo, heroe)
        tm.sleep(1.5)
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