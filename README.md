# Proyecto juego RPG Medieval <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">

TP Programacion 1- UADE

:construction: Proyecto en construcción :construction:


--------------------------------------------------------------------------------------

El objetivo del trabajo practico es aplicar los conocimientos de Python vistos durante la cursada.

--------------------------------------------------------------------------------------
Integrantes del equipo:

      Eduardo Zampedri
      Agustin Athis
      Macarena Molina

Pasos a seguir para probar el trabajo practico:

    1- Instalar python
    2- Clonar Repositorio
    3- Ir al archivo Menu.py y ejecutar el codigo.
    4- En la consola se iniciará el proyecto. A jugar!

--------------------------------------------------------------------------------------
## :console: Funciones a Desarrollar



Primera vez jugando RPG? 

- En primera instancia, el juego ofrece 4 ¨clases¨ de personajes para elegir: Aragorn, Legolas, Morgana y Gandalf.
- Cada uno de ellos tiene habilidades distintas para desempeñar un rol unico, Guerrero, Arquero, Mago y Healer. 
- A su vez, tienen estadisticas base repartidas de forma acorde al rol que cumple cada ¨clase¨
- El juego consta de 3 mapas, donde deberemos pelear con distintos enemigos hata llegar al 3er y ultimo mapa donde tendremos la pelea con el jefe final, comunmente conocido como ¨BOSS¨.
- El modo de pelea sera un combate por turnos que esta basado en un sistema de tirada de dados donde el que saque el mayor numero podra efectuar su habilidad exitosamente. 
- Sacar un numero alto o bajo, dependera directamente de la estadistica ¨lk¨ (suerte), donde a mayor ¨lk¨ mayor probabilidad tendremos de lanzar una habulidad de forma exitosa.

Glosario:
- `hp`: puntos de vida
- `mp`: puntos de energia
- `atk`: puntos de ataque
- `mag`: puntos de ataque mágico
- `def`: puntos de defensa
- `lk`: puntos de suerte
- `exp`: contador de experiencia
- `habilidades`: lo que hace cada personaje.
            
--------------------------------------------------------------------------------------
El trabajo práctico esta dividido en 3 partes. 

            1) El tablero de juego, 
            2) los personajes con sus habilidades y 
            3) la batalla propiamente dicha entre los personajes.

## :hammer: Funciones a Desarrollar
                  
      Mapa
      armadoDeMapa     : funcion que genera el mapa 
      movimientoHeroe  : funcion que permite el movimiento del heroe por el mapa
      controlDePosicion: controla la posicion del heroe paro controlar si entra en batalla, sale del mapa o cambia de nivel

      Heroe
      inicializarEstado: inicializar stat del hereo
      movimiento       : movimiento por el mapa
      generarDaño      : generar daño
      recibirDaño      : recbir daño
      curarse          : curarse hp
      devolverHP       : devolver hp del heroe

      Suerte
      shuffle          : barajar 
      genSuerte        : generar suerte aleatoria
      tirarda          : tirada del dado virtual

      Batalla
      ataque           : se materializa el ataque heroe/contrincante o contrincante/heroe
      defensa          : se materializa la defensa heroe/contrincante o contrincante/heroe
      esquivar         : se materializa el esquivar heroe/contrincante o contrincante/heroe

      Partida
      guardarPartida
      cargarPartida

      Jsons
      heroes           : todos los personajes que se pueden elegir con sus stats
      enemigos         : todos los enemigos y el jefe final

Distribucion de tareas

- Tablero de juego o mapa: `Edu`
- Batalla: `Alan`
- Personajes con sus habilidades, Guardar Partida, Menu Personajes: `Maca`

Si bien cada integrante tiene asignada una tarea del proyecto, colaboramos entre todos en todas las tareas cuando un companero necesite soporte.

--------------------------------------------------------------------------------------



