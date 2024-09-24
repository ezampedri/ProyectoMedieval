champions = {
    "heroe": [{
        "nombre": "Gandalf",
        "clase":"Healer",
        "hp": 270,
        "mp": 40,
        "atk": 10,
        "mag": 15,
        "agi":50,
        "def": 5,
        "lk": 10,
        "exp": 0,
        "habilidades": ["Rejuvenecer"]
    },
    {
        "nombre": "Aragorn",
        "clase":"Guerrero",
        "hp": 350,
        "mp": 25,
        "atk": 20,
        "mag": 5,
        "agi":80,
        "def": 10,
        "lk": 10,
        "exp": 0,
        "habilidades": ["Corte Dimensional", "Disparo Penetrante"]
    },
    {
        "nombre": "Morgana",
        "clase":"Maga",
        "hp": 250,
        "mp": 50,
        "atk": 5,
        "mag": 5,
        "agi":90,
        "def": 5,
        "lk": 20,
        "exp": 0,
        "habilidades": ["Bola de fuego"]
    },
    {
        "nombre": "Legolas",
        "clase":"Arquero",
        "hp": 250,
        "mp": 50,
        "atk": 5,
        "mag": 5,
        "agi":60,
        "def": 5,
        "lk": 20,
        "exp": 0,
        "habilidades": ["Disparo Penetrante"]
    }
    ],
    "enemigos": [
        {
            "nombre": "Goblin",
            "hp": 20,
            "mp": 20,
            "atk": 20,
            "mag": 20,
            "agi": 20,
            "def": 20,
            "lk": 20,
            "exp": 20
        },
        {
            "nombre": "Orco",
            "hp": 20,
            "mp": 20,
            "atk": 20,
            "mag": 20,
            "agi": 20,
            "def": 20,
            "lk": 20,
            "exp": 20

        },
        {
            "nombre": "Drafnakk, Tirano de Gyanavall",
            "hp": 500,
            "mp": 20,
            "atk": 20,
            "mag": 20,
            "agi": 20,
            "def": 20,
            "lk": 20,
            "exp": 20
        }
    ]
}


def curarse(nombre_heroe):
    for heroe in champions["heroe"]:
        if heroe["nombre"] == nombre_heroe:
            heroe["hp"] +=50

def rejuvenecer(nombre_heroe):
    for heroe in champions["heroe"]:
        if heroe["nombre"] == nombre_heroe:
            if nombre_heroe == "Gandalf":
                heroe["hp"] -= 5

def mostrar_heroes():
    print("Héroes:")
    for heroe in champions["heroe"]:
        print(f"Nombre: {heroe['nombre']}, Clase: {heroe['clase']}, HP: {heroe['hp']}, MP: {heroe['mp']}, ATK: {heroe['atk']}, MAG: {heroe['mag']}, AGI: {heroe['agi']}, DEF: {heroe['def']}, LK: {heroe['lk']}, EXP: {heroe['exp']}, Habilidades: {', '.join(heroe['habilidades'])}")

def mostrar_enemigos():
    print("Enemigos:")
    for enemigo in champions["enemigos"]:
        print(f"Nombre: {enemigo['nombre']}, HP: {enemigo['hp']}, MP: {enemigo['mp']}, ATK: {enemigo['atk']}, MAG: {enemigo['mag']}, AGI: {enemigo['agi']}, DEF: {enemigo['def']}, LK: {enemigo['lk']}, EXP: {enemigo['exp']}")

def menu():
    while True:
        print('---------------------')
        print('- Proyecto Medieval -')
        print('---------------------')
        print("\nMenu:")
        print("1. Ver Héroes")
        print("2. Ver Enemigos")
        print("3. Salir")
        print('---------------------')
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_heroes()
        elif opcion == '2':
            mostrar_enemigos()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


menu()
                