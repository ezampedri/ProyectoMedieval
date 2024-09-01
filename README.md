# Proyecto juego RPG Medieval

TP Programacion 1- UADE
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

--------------------------------------------------------------------------------------
El trabajo práctico esta dividido en 3 partes. El tablero de juego, los personajes con sus habilidades y la batalla propiamente dicha.

Funciones a Desarrollar
                  
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

Distribucion de tareas
      Tablero de juego o mapa: Edu.
      Batalla: Alan
      Personajes con sus habilidades: Maca.

Si bien cada integrante tiene asignada una tarea del proyecto, colaboramos entre todos en todas las tareas cuando un companero necesite soporte.

--------------------------------------------------------------------------------------

Primera vez jugando RPG? 

Los personajes son Champions y tienen Stats o sea estadísticas. Las Stats pueden ser:
      hp: puntos de vida
      mp: puntos de energia
      atk: puntos de ataque
      mag: puntos de ataque mágico
      def: puntos de defensa
      lk: puntos de suerte
      exp: contador de experiencia
      habilidades: lo que hace cada personaje.


--------------------------------------------------------------------------------------

Instrucciones del Juego

El juego se va a ejecutar en la terminal de Python. 
