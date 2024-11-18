# 🏰 MEDIE.PY🏰 <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
## TP Programacion 1 - UADE
## Proyecto Medieval: Juego en python Role-playing Game  

### Índice

* [Objetivo](#objetivo)

* [Integrantes del equipo](#integrantes-del-equipo)

* [Pasos a seguir para probar el trabajo practico](#-pasos-a-seguir-para-probar-el-trabajo-practico)

* [Instrucciones del Juego](#instrucciones-del-juego)
  
* [Glosario](#-glosario)


## Objetivo

> El objetivo del trabajo practico es aplicar los conocimientos de Python vistos durante la cursada.

Con una fuerte inspiración sobre videojuegos de Rol japoneses,
apuntamos a crear una épica que narre por consola
la historia de nuestro héroe, elegible de un abanico de opciones presentadas al
usuario,
que se adentrará en un calabozo lleno de criaturas fantásticas hostiles con las que
deberá batallar para finalmente llegar a derrotar al tirano Gyanavall.

## 🧑‍🤝‍🧑Integrantes del equipo:

- Eduardo Zampedri

- Alan Athis

- Macarena Molina

## 👌 Pasos a seguir para probar el trabajo practico:

1- Instalar python y Visual Studio Code.

2- Clonar Repositorio

      git clone https://github.com/ezampedri/ProyectoMedieval.git
      
3- Ir al archivo Main.py y ejecutar el codigo.

4- En la consola se iniciará el proyecto. 

5- A jugar!

## 🎮Instrucciones del Juego 

En primera instancia, el juego ofrece 4 _clases_ de personajes para elegir: Aragorn, Legolas, Morgana y Gandalf.

 Cada uno de ellos tiene habilidades distintas para desempeñar un rol unico, Guerrero, Arquero, Mago y Healer. 
 
 A su vez, tienen estadisticas base repartidas de forma acorde al rol que cumple cada _clase_.
 
 El juego consta de 3 mapas, donde deberemos pelear con distintos enemigos hata llegar al 3er y ultimo mapa donde tendremos la pelea con el jefe final, comunmente conocido como _Jefe_.
 
 El modo de pelea sera un combate por turnos que esta basado en un sistema de tirada de dados donde el que saque el mayor numero podra efectuar su habilidad exitosamente. 
 
 Sacar un numero alto o bajo, dependera directamente de la estadistica _lk_ (suerte), donde a mayor _lk_ mayor probabilidad tendremos de lanzar una habulidad de forma exitosa.

 

 ⭐ El menú Inicio

 Si es la primera vez jugando, se crea una nueva partida. Se ingresa el numero 1 en la terminal del proyecto.

<img width="auto" alt="imagen" src="https://github.com/user-attachments/assets/ae3af9af-66ee-4c5c-981a-0efb59c15fee">


 
 ⭐ Seleccion de Personaje

Se ingresa el numero acorde al personaje.
 
<img width="464" alt="imagen (1)" src="https://github.com/user-attachments/assets/ed02178a-45b1-4d1c-b877-dcfc8886b872">

 
 ⭐ Mapa
 El mapa posee una salida, al personaje, enemigos y obstaculos. Nuestro personaje esta identificado con un mago azul, la salida es el cuadrado blanco, los enemigos son las calaveras y los obstaculos son los arboles y los ladrillos. Debemos movernos con las teclas AWSD para llegar a la salida. Cuando nos crucemos con una calavera, se ejecuta automaticamente la batalla. Debemos ganarla si o si para avanzar el casillero.

<img width="464" alt="imagen (2)" src="https://github.com/user-attachments/assets/199f2ba4-75a3-40fc-8ffd-267ab1a47821">

 
 ⭐ Batalla entre Heroe y Enemigo
 
<img width="464" alt="imagen (3)" src="https://github.com/user-attachments/assets/27091f29-aada-4dac-a2ae-15305b3f9f06">


 ⭐ Desafios rompecabezas para avanzar de nivel en tablero

<img width="464" alt="imagen (4)" src="https://github.com/user-attachments/assets/bd515938-6166-482a-9ac7-a9dded41a0e9">

 
 
## 📖 Glosario:
| Termino          | Definición                                                                                                                                                                                                                                                                                                                                                   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _hp_      | puntos de vida.    
| _mp_      | puntos de energía. 
| _atk_      | puntos de ataque. 
| _mag_      | puntos de ataque mágico. 
| _agi_      | puntos de agilidad. 
| _def_      | puntos de defensa. 
| _lk_      | puntos de suerte. 
| _exp_      | contador de experiencia. 
| _habilidades_      | la gracia o lo que hace cada personaje. 


## :hammer: Funciones a Desarrollar

| Mapa          |                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _armadoDeMapa_      | funcion que genera el mapa.    
| _movimientoHeroe_      | puntos de energía. 
| _controlDePosicion_      | controla la posicion del heroe paro controlar si entra en batalla, sale del mapa o cambia de nivel. 


| Heroe          |                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _inicializarEstado_      | inicializar stat del hereo.    
| _movimiento_      | movimiento por el mapa. 
| _generarDaño_      | generar daño a un oponente. 
| _recibirDaño_      | recbir daño. 
| _curarse_      | curarse hp. 
| _devolverHP_      | devolver hp del heroe. 

| Suerte          |                                                                                                                                                                                                                                                                                                                                                 |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _shuffle_      | barajar.    
| _genSuerte_      | generar suerte aleatoria. 
| _tirarda_      | tirada del dado virtual. 

| Batalla          |                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _ataque_      | se materializa el ataque heroe/contrincante o contrincante/heroe.    
| _defensa_      | se materializa la defensa heroe/contrincante o contrincante/heroe. 
| _esquivar_      |  se materializa el esquivar heroe/contrincante o contrincante/heroe. 

## :hammer: Estructuras

| Partida          |                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _guardarPartida_      | se guardan en un txt los valores del personaje, las stats, el nivel del mapa y el mapa.    
| _cargarPartida_      | si existe un txt previamente generado, carga los valores al inciar el juego. 
 
| Jsons          |                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _heroes_      | todos los personajes que se pueden elegir con sus stats.    
| _enemigos_      | todos los enemigos y el jefe final. 
    


☑️ Distribucion de tareas

- Tablero de juego o mapa: `Edu`
- Batalla: `Alan`
- Personajes con sus habilidades, Guardar Partida, Menu Personajes: `Maca`


> [!NOTE]
> Si bien cada integrante tiene asignada una tarea del proyecto, colaboramos entre todos en todas las tareas cuando un companero necesite soporte.

