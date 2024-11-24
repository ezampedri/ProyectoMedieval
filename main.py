import menu
import sys
import os
from colorama import Fore, Back, Style

# Agregar la ruta del directorio actual al sys.path para poder importar módulos desde otros directorios
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Punto de entrada al juego
if __name__ == "__main__" and not any("pytest" in arg for arg in sys.argv):
    menu.main()

#sí, estoy aprendiendo a usar pytest acá.
def sumar(a, b):
    return a + b

def masgrande(a,b):
    return a > b