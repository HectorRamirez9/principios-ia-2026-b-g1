Laberinto con BFS y A*
Descripción
Este proyecto consiste en resolver un laberinto representado mediante una matriz en Python.
Se implementaron dos algoritmos de búsqueda:
BFS (Breadth-First Search): realiza una búsqueda por niveles.
A*: utiliza la heurística de distancia Manhattan para buscar de una manera más orientada hacia la meta.
El objetivo es encontrar un camino desde el punto inicial hasta el punto final y comparar cuál algoritmo expande menos nodos.
Representación del laberinto
La matriz utiliza:
`0` para representar un espacio por donde se puede pasar.
`1` para representar una pared.
El punto inicial es:
`(0, 0)`
El punto final es:
`(4, 4)`
Espacio de estados
Cada posición `(fila, columna)` del laberinto representa un estado.
Desde cada estado se puede intentar realizar cuatro movimientos:
Arriba
Abajo
Izquierda
Derecha
No se permite salir de los límites de la matriz ni atravesar paredes.
Por lo tanto, el problema consiste en encontrar una secuencia de estados que permita llegar desde `(0, 0)` hasta `(4, 4)`.
Algoritmo BFS
BFS utiliza una cola y explora primero las posiciones que están más cerca del punto inicial.
Una ventaja de BFS es que, cuando todos los movimientos tienen el mismo costo, encuentra un camino más corto.
Algoritmo A*
A* combina el costo que ya se ha recorrido con una estimación de lo que falta para llegar a la meta.
Se utiliza la distancia Manhattan:
`h = |fila1 - fila2| + |columna1 - columna2|`
La función de A* es:
`f = g + h`
Donde:
`g` = costo del camino recorrido.
`h` = estimación de la distancia hasta la meta.
`f` = valor utilizado para decidir qué posición explorar primero.
Cómo ejecutar el programa
Tener instalado Python 3.
Guardar el archivo como `laberinto.py`.
Abrir una terminal en la carpeta del proyecto.
Ejecutar:
```bash
python laberinto.py
```
Resultados
El programa muestra:
El camino encontrado por BFS.
La cantidad de nodos expandidos por BFS.
El camino encontrado por A*.
La cantidad de nodos expandidos por A*.
Una comparación indicando cuál algoritmo fue más eficiente.
Conclusión
Los dos algoritmos pueden encontrar un camino desde el inicio hasta la meta. La diferencia principal es la forma en que buscan.
BFS explora de manera uniforme desde el inicio, mientras que A* utiliza la heurística Manhattan para darle prioridad a los estados que parecen estar más cerca de la meta.
En este ejercicio se pueden comparar los nodos expandidos para saber cuál fue más eficiente en el laberinto utilizado.
