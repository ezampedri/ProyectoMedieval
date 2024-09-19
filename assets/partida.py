import champions

partida=[

]

def mostrarMenuPersonajes():
    print("1. Healer")
    print("2. Guerrero")
    print("3. Maga")
    print("4. Arquero")
    print("5. Salir")


def detallePersonaje(personajeSeleccionado):
    for personaje in champions:
        if champions['nombre']==personajeSeleccionado:
            print(personaje)
    



partida=True

while partida:
    mostrarMenuPersonajes()
    opcion=int(input("Ingrese la opcion para ver los personajes\n"))

    if opcion==5:
        bandera=False
    elif opcion==1:
        detallePersonaje('Gandalf')
    elif opcion==2:
        detallePersonaje('Aragorn')
    elif opcion==3:
        detallePersonaje('Morgana')
    elif opcion==4:
        detallePersonaje('Legolas')
