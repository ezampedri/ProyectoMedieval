import pytest
from main import sumar, masgrande
from battle import suerte
from battle.mapa import armadoDeMapa, movimientoHeroe, controlDePosicion, imprimirMapa
from battle.battle import calcular_daño, ac_evade, batalla
from assets import funciones_champion

heroeGuardado = {
    "nombre": 'Vincent',
    "hp": 270,
    "mp": 40,
    "atk": 50,
    "mag": 30,
    "agi": 50,
    "def": 20,
    "lk": 100,
    "exp": 0,
    "arma": 10,
    "habilidades": ["Rejuvenecer"]
    }

enemigo = {
    'nombre': 'Goblin',
    "hp": 60,
    "mp": 20,
    "atk": 40,
    "mag": 20,
    "agi": 20,
    "def": 20,
    "lk": 20,
    "exp": 20,
    "habilidades": ["curar"]
    }


#estas dos son funciones de prueba básicas
def test_sumar():
    assert sumar(1, 2) == 3
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(-1, -1) == -2

def test_masgrande():
    assert masgrande(2, 1) == True
    assert masgrande(1, 2) == False
    assert masgrande(2, 2) == False
    assert masgrande(-1, -2) == True


#esto puede fallar si la suerte no está de nuestro lado
def test_calcular_daño():
    actor = heroeGuardado
    vs = enemigo
    daño = calcular_daño(actor, vs)
    if daño in [180, 130, 155]:
        assert True
    else:
        assert False

def test_suerte():
    assert suerte.tirada(0) == False
    assert suerte.tirada(100) == True
    
def test_armadoDeMapa():
    mapa = armadoDeMapa(10, 10)
    assert len(mapa) == 10
    assert len(mapa[0]) == 10
    assert any('\U0001F333' in fila for fila in mapa)  # Check if there are trees
    assert any('\U0001F9F1' in fila for fila in mapa)  # Check if there are walls
    assert any('\U0001F480' in fila for fila in mapa)  # Check if there are enemies
    assert any('\U0001F532' in fila for fila in mapa)  # Check if there is an exit

def test_controlDePosicion():
    mapa = armadoDeMapa(10, 10)
    posicionHeroe = (0, 0)
    nivel = 1
    salidaAlcanzada = controlDePosicion(mapa, posicionHeroe, nivel)
    assert salidaAlcanzada == False  # Initial position should not be the exit

def test_imprimirMapa(capsys):
    mapa = armadoDeMapa(10, 10)
    posicionHeroe = (0, 0)
    imprimirMapa(mapa, posicionHeroe)
    captured = capsys.readouterr()
    assert '\U0001F9D9' in captured.out  # Check if hero is printed


def test_cargar_enemigo():
    enemigo = funciones_champion.cargar_enemigo('Goblin')
    assert enemigo is not None
    assert enemigo['nombre'] == 'Goblin'
    assert enemigo['hp'] == 20
    assert enemigo['mp'] == 20
    assert enemigo['atk'] == 20
    assert enemigo['mag'] == 20
    assert enemigo['agi'] == 20
    assert enemigo['def'] == 5
    assert enemigo['lk'] == 20
    assert enemigo['exp'] == 20
    assert 'curar' not in enemigo['habilidades'] 
    
def test_batalla_recompensa_victoria():
    heroe = heroeGuardado.copy()
    enemigo = {
        'nombre': 'Goblin',
        "hp": 0,  # Set enemy HP to 0 to simulate victory
        "mp": 20,
        "atk": 40,
        "mag": 20,
        "agi": 20,
        "def": 20,
        "lk": 20,
        "exp": 20,
        "habilidades": ["curar"]
    }
    recompensa = batalla(heroe, enemigo)
    assert recompensa['victoria'] == True
    assert 20 <= recompensa['xp'] <= 70  # XP should be within the expected range




