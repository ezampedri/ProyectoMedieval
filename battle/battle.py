import random as r
import json
from battle import suerte
import os
import time as tm
import sys
import keyboard
from colorama import Back, Style, Fore


'''
Glosario para no-tan-nerds como yo (por si acaso):
acc: Acción
Acciones: Las acciones que puede realizar el jugador en un turno
acc_ai: Acción del enemigo
ac_ataque: Acción de ataque
ac_evade: Acción de evasión
ac_magia: Acción de magia
ac_atk_sobrecarga: Acción de ataque especial
minijuego_sobrecarga: Es un minijuego que se ejecuta para realizar un ataque especial, utiliza una lista vacía la cual se recorre por el iterador, si el jugador presiona espacio en el momento adecuado, se acumulan puntos.
generar_texto: Función que imprime texto en pantalla letra por letra, es una ilusion de que el texto se escribe solo. Solo tiene un uso estético.
interfaz: Función que imprime la interfaz de la batalla, mostrando los nombres de los personajes, sus hp y mp.
'''

hp_total = None  # Guardar la vida total del héroe

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
    with open('assets/habilidades.json', 'r') as file:
        data = json.load(file)['habilidades']
    for m in data:
        if m['nombre'] == habilidad:
            daño = m['atk'] * actor['mag']
            vs['hp'] -= daño
            generar_texto(f"{actor['nombre']} lanzó {habilidad} sobre {vs['nombre']} por un total de {daño} de hp")
        else:
            ("No se reconoce la habilidad")

def interfaz(heroe, enemigo):
    print("="*42)
    print(f"{heroe['nombre']:^20} | {enemigo['nombre']:^20}")
    print("-" * 42)
    print(f"HP: {heroe['hp']:<17} | HP: {enemigo['hp']:<20}")
    print(f"MP: {heroe['mp']:<17} | MP: {enemigo.get('mp', 'N/A'):<20}")
    print("===================================")

def escape(heroe):
    escapada = suerte.tirada((suerte.suerte // 2) + heroe['agi'])
    if escapada:
        generar_texto(f"{heroe['nombre']} logró escapar exitosamente.")
    else:
        generar_texto(f"{heroe['nombre']} no logró escapar.")

def minijuego_sobrecarga():
    '''Este minijuego genera una barra que se mueve de derecha a izquierda.
       El jugador debe presionar espacio cuando la barra de impacto está dentro
       de una sección roja. Si lo hace correctamente, acumula puntos.'''

    cont = 0  # Contador para acumular los aciertos
    x = 30  # Ancho de la barra
    x_redband = r.randint(1, 3)  # Ancho aleatorio de la banda roja
    pos_redband = 2  # Posición de inicio de la banda roja

    # Crear la barra roja en una posición aleatoria
    barra = list(range(pos_redband, min(pos_redband + x_redband, x))) 

    # 5 iteraciones de la barra moviéndose
    for _ in range(5):
        flag = True  # Inicializamos la bandera en True para empezar el ciclo
        for i in range(x - 1, -1, -1):  # Movimiento de derecha a izquierda
            if not flag:  # Si la bandera está en False, salimos del ciclo
                flag = False

            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
            linea = [' '] * x  # Crear la línea vacía

            # Colocar la banda roja en la posición correspondiente
            for j in barra:
                linea[j] = Back.RED + ' ' + Style.RESET_ALL

            linea[i] = '|-'  # El cursor que se mueve de derecha a izquierda

            print(''.join(linea))  # Mostrar la barra en pantalla

            tm.sleep(0.03)  # Velocidad de movimiento de la barra

            # Comprobar si se presionó espacio
            if keyboard.is_pressed('space'):
                tm.sleep(0.07)
                if i in barra:  # Si el cursor está en la banda roja
                    cont += 1  # Incrementar el contador si se presionó correctamente
                flag = False  # Cambiar la bandera a False para salir del ciclo

    tm.sleep(0.4)  # Pausa final
    return cont  # Retornar el número de aciertos

def sobrecargado(heroe): #esto devuelve True o False según la vida faltante de nuestro personaje
    sobrecarga = suerte.tirada(hp_total-heroe['hp']//1)
    return sobrecarga

def ac_atk_sobrecarga(heroe, enemigo):
    generar_texto('Concentras tu ataque especial...')
    tm.sleep(1)
    multiplicador = minijuego_sobrecarga()
    daño = calcular_daño(heroe, enemigo)*multiplicador
    generar_texto(f"{heroe['nombre']} logró dañar a {enemigo} por un total de {daño}")
    enemigo['hp'] -= daño

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
        print(f"input {user}")
        print(f"heroe {heroe['habilidades']}")
        if user.lower() in heroe['habilidades']:
            ac_magia(heroe, enemigo, user)
        else:
            generar_texto(f'Ese conjuro no forma parte del conocimiento de {heroe["nombre"]}')
    elif user == "evadir":
        generar_texto(f'{heroe["nombre"]} ¡se prepara para evadir el próximo ataque!')
        heroe['agi'] *= 2  # Dobla la agilidad temporalmente
    elif user == 'escapar':
        escape(heroe)
    elif user == 'sobrecarga':
        ac_atk_sobrecarga(heroe, enemigo)
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
    global hp_total
    hp_total = heroe['hp']

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
        generar_texto(f"{enemigo['nombre']} ha sido derrotado!")
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
