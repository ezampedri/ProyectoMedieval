import menu
from battle import battle
from battle import mapa
from battle import partida
import colorama
import random as r
import time as tm
import sys
import os
import json
import keyboard
from colorama import Fore, Back, Style

# Agregar la ruta del directorio actual al sys.path para poder importar módulos desde otros directorios
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Inicializar colorama
colorama.init()

# Punto de entrada al juego
if __name__ == "__main__":
    menu.main()
