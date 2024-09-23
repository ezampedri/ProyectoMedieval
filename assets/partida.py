import champions

partida=[

]

def mostrarMenuPersonajes():
    """
    Muestra mediante carteles una lista de champions, simulando un menu en terminal
    
    Parámetros:
    No tiene

    Devuelve:
    cartel en pantalla con el nombre de cada champion
    """
    print('---------------------')
    print('- Proyecto Medieval -')
    print('---------------------')
    print("1. Healer")
    print("2. Guerrero")
    print("3. Maga")
    print("4. Arquero")
    print("5. Exit")
    print('---------------------')


def detallePersonaje(personajeSeleccionado):
    """
    Devuelve la informacion detalla de un champion
    
    Parámetros:
    personajeSeleccionado (string): El personaje seleccionado por el usuario.

    Devuelve:
    cartel en pantalla con la informacion del champion
    """
    for personaje in champions:
        if champions['nombre']==personajeSeleccionado:
            print('---------------------')
            print('- Proyecto Medieval -')
            print('---------------------')
            print("1. Nombre: "+ champions['nombre'] )
            print("2. Clase: " + champions['clase'])
            print("3. Puntos de Vida " + champions['hp'])
            print("4. Puntos de Energia" + champions['mp'])
            print("5. Puntos de Ataque" + champions['atk'])
            print("6. Puntos de Magia" + champions['mag'])
            print("7. Puntos de Agilidad" + champions['agi'])
            print("8. Puntos de Defensa" + champions['def'])
            print("9. Puntos de Experiencia" + champions['exp'])
            print("9. Puntos de Experiencia" + champions['habiliades'])
            print('---------------------')
            
    
def seleccionarPersonaje(personajeElegido):
    """
    Da de alta el personaje elegido en la partida
    
    Parámetros:
    personaje (string): El personaje seleccionado por el usuario.

    Devuelve:
    Da de alta en la lista el personaje
    """
    personajeDePartida=personajeElegido
    partida.append(personajeDePartida)



#programa del menu
partida=True

while partida:
    mostrarMenuPersonajes()
    print('---------------------')
    print('- Proyecto Medieval -')
    print('---------------------')
    opcion=int(input("Ingrese la opcion para ver los personajes:\n"))
    print('---------------------')

    if opcion==5:
        partida=False
    elif opcion==1:
        detallePersonaje('Gandalf')
    elif opcion==2:
        detallePersonaje('Aragorn')
    elif opcion==3:
        detallePersonaje('Morgana')
    elif opcion==4:
        detallePersonaje('Legolas')
    

