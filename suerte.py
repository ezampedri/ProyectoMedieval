import random as r
import json

#el stat de suerte puede ser ligado a un stat dentro de un diccionario que represente las estadísticas del actor en el juego
suerte = 90
impares = (1, 3, 5, 7, 9)
pares = (2, 4, 6, 8)
#función lambda para tomar un elemento random de una lista, esto es una función de random pero no tenemos permitido usarla
choice = lambda lista: lista[r.randint(0, len(lista)-1)]

#barajar los elementos de la lista, esto es una función de random pero no tenemos permitido usarla
def shuffle(lista):
    n = len(lista)
    for i in range(n):
        j = r.randint(0, n-1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista

#genero la ruleta
def gensuerte():
    ruleta = []
    restantes = 100 - suerte
    for _ in range(suerte): #genero números pares
        elem = choice(pares)
        ruleta.append(elem)
    for _ in range(restantes): #genero números impares
        elem = choice(impares)
        ruleta.append(elem)
    shuffle(ruleta)
    return ruleta

def tirada():
    ruleta = gensuerte()
    output = choice(ruleta)
    if output % 2 == 0:
        return True
    else:
        return False
    
print(tirada())
