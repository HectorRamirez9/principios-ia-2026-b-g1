Proyecto: Comparación de BFS, UCS y A* en el 8-Puzzle.

Introducción

En este trabajo escogí el problema del 8-puzzle para poner en práctica algunos algoritmos de búsqueda que hemos visto en Inteligencia Artificial.
La idea es partir de una posición inicial de las fichas y tratar de llegar a una posición final ordenada. Para resolverlo se implementaron tres algoritmos: BFS, búsqueda de costo uniforme (UCS) y A*. En el caso de A*, se utilizó la distancia Manhattan como heurística.
Además, se hicieron pruebas con tres casos diferentes para comparar cuántos nodos revisa cada algoritmo y cuánto tiempo tarda en encontrar la solución.

1. ¿Qué problema estamos resolviendo?

El 8-puzzle es un tablero de 3×3 que tiene ocho números y un espacio vacío. El objetivo es ordenar las fichas de esta forma:
```text
1 2 3

4 5 6

7 8 0

```
El `0` representa el espacio vacío.
Por ejemplo, podemos comenzar con:
```text
1 2 3
4 5 6
0 7 8
```

y mover el espacio vacío hasta conseguir el estado final.

El problema como espacio de estados

Para poder resolver el puzzle con algoritmos de búsqueda, lo podemos representar de la siguiente manera:

Estado: la posición actual de todas las fichas.

Estado inicial: la configuración con la que comenzamos.

Estado final: `(1,2,3,4,5,6,7,8,0)`.

Acciones: mover el espacio vacío arriba, abajo, izquierda o derecha.

Costo: cada movimiento cuesta 1.

Solución: una serie de movimientos que permite llegar al estado final.

En total existen 9! configuraciones posibles, pero solamente la mitad son alcanzables desde un estado determinado. Por eso hay hasta 181.440 estados alcanzables.

---

2. Algoritmo A* y distancia Manhattan
   
A* fue el algoritmo que más nos interesa porque no solamente mira el costo que ya llevamos, sino que también intenta calcular qué tan lejos estamos de la solución.

La fórmula utilizada es:

```text

f(n) = g(n) + h(n)

```

Donde:

`g(n)` = costo de los movimientos realizados hasta el momento.

`h(n)` = estimación del costo que falta.

`f(n)` = valor utilizado por A* para decidir qué estado revisar primero.

Para `h(n)` usamos la distancia Manhattan.

Esta heurística calcula cuántos movimientos tendría que hacer cada ficha para llegar a su posición correcta, sumando las diferencias de filas y columnas.

Por ejemplo, una parte del código es:

```python

def manhattan(state):

    total = 0

    for i, tile in enumerate(state):

        if tile == 0:

            continue

        goal_row, goal_col = divmod(tile - 1, 3)

        row, col = divmod(i, 3)

        total += abs(row - goal_row) + abs(col - goal_col)

    return total

```

No se toma en cuenta el espacio vacío. Esta heurística es admisible porque no sobreestima el número mínimo de movimientos que faltan.

---

3. Algoritmos utilizados
   
BFS

BFS (Breadth-First Search) revisa primero los estados que están más cerca del estado inicial.
Como en nuestro problema todos los movimientos tienen costo 1, BFS encuentra una solución óptima.
El problema es que cuando el puzzle se vuelve difícil, puede tener que revisar una gran cantidad de estados y consumir bastante memoria.

UCS

UCS (Uniform Cost Search) selecciona el estado que tenga el menor costo acumulado.
En este ejercicio cada movimiento cuesta exactamente 1. Por eso UCS termina teniendo un comportamiento muy parecido a BFS.
La diferencia es que UCS está pensado especialmente para problemas donde los costos de las acciones pueden ser diferentes.

A*

A* combina el costo que ya llevamos con una estimación de lo que falta:

```text

f(n) = g(n) + h(n)
```

En este caso usamos la distancia Manhattan. Esto ayuda a que A* no tenga que revisar tantos estados que no parecen acercarnos a la solución.

---

4. Código principal
   
El archivo `eight_puzzle.py` contiene los tres algoritmos y una función para realizar las pruebas.
La idea básica de A* es:

```text

1. Comenzar con el estado inicial.

2. Calcular su distancia Manhattan.

3. Elegir el estado con menor f(n).

4. Generar sus posibles movimientos.

5. Calcular el nuevo costo y la heurística.

6. Repetir hasta encontrar el estado final.

```

Una parte importante del código es:

```python

new_g = g + 1

h = manhattan(nxt)


heapq.heappush(
    heap,


    (new_g + h, new_g, counter, nxt, path + [move])

)

```

Aquí se calcula `g + h`, que es precisamente el valor que utiliza A* para decidir qué nodo explorar.

---

5. Pruebas realizadas
   
Para comparar los algoritmos se utilizaron tres configuraciones diferentes:

Instancia	Estado inicial	Dificultad
1	`(1,2,3,4,5,6,0,7,8)`	Fácil
2	`(1,2,3,5,0,6,4,7,8)`	Media
3	`(8,6,7,2,5,4,3,0,1)`	Difícil

Se midió:

cantidad de movimientos de la solución;

cantidad de nodos expandidos;

tiempo de ejecución.

El tiempo mostrado corresponde al promedio de tres ejecuciones.

---

6. Resultados
   
Instancia	Algoritmo	Movimientos	Nodos expandidos	Tiempo promedio
Fácil	BFS	2	7	0.024 ms
Fácil	UCS	2	7	0.031 ms
Fácil	A*	2	3	0.020 ms
Media	BFS	4	33	0.093 ms
Media	UCS	4	33	0.105 ms
Media	A*	4	5	0.035 ms
Difícil	BFS	31	181.439	10627.460 ms
Difícil	UCS	31	181.439	1026.725 ms
Difícil	A*	31	21.198	177.897 ms

> Los tiempos pueden cambiar dependiendo del computador donde se ejecute el programa.

---

7. ¿Qué podemos observar?
   
En las dos primeras pruebas la diferencia no es tan grande porque son problemas sencillos.
La diferencia se nota mucho más en la tercera instancia. BFS y UCS tuvieron que expandir aproximadamente 181 mil nodos, mientras que A* expandió cerca de 21 mil.
Esto muestra que la heurística Manhattan ayuda bastante a A*. En este caso, A* encontró una solución de 31 movimientos, igual que BFS y UCS, pero revisando muchos menos estados.
También podemos observar que UCS no tiene una ventaja importante frente a BFS en este problema, porque todos los movimientos tienen el mismo costo

---

8. Algorithm Comparison
   
BFS explores the search tree level by level, so its time and space complexity can grow as O(b^d).  
UCS is also expensive in time and space because it keeps the lowest-cost frontier and may explore many states before reaching the goal.  
A* has exponential worst-case time and space complexity, but a good heuristic can reduce the number of states explored in practice.  
BFS is complete and optimal when all actions have the same cost, which is the case in this 8-puzzle implementation.  
UCS is complete and optimal when action costs are positive, so it also produces an optimal solution for this problem.  
A* is complete and optimal when the heuristic is admissible and consistent, and Manhattan distance satisfies these conditions for the 8-puzzle.  
Therefore, A* can obtain the same optimal solution as BFS and UCS while usually expanding fewer nodes.

---

9. Comparación general
    
Característica	BFS	UCS	A*
Usa heurística	No	No	Sí
Completo	Sí	Sí	Sí
Óptimo en este problema	Sí	Sí	Sí
Costo de los movimientos	Ignora diferencias	Tiene en cuenta costos	Tiene en cuenta costos + heurística
Memoria	Alta	Alta	Alta
Ventaja principal	Fácil de implementar	Funciona con diferentes costos	Busca de manera más inteligente

---

10. Conclusiones
    
Después de realizar las pruebas, considero que A* es la mejor opción para este problema cuando tenemos una buena heurística.
BFS es fácil de entender y funciona bien cuando el problema es pequeño. Sin embargo, cuando aumenta la dificultad, empieza a revisar demasiados estados.
UCS también encuentra la solución óptima, pero en este caso no presenta una ventaja clara porque todos los movimientos cuestan lo mismo.
Por otro lado, A* utiliza la distancia Manhattan para saber qué estados parecen estar más cerca de la solución. Esto permitió reducir bastante la cantidad de nodos expandidos en la prueba difícil.
En conclusión, los tres algoritmos son capaces de resolver el 8-puzzle de forma óptima en estas condiciones, pero A* resulta mucho más eficiente en las instancias difíciles gracias al uso de la heurística.

---

11. ¿Cómo ejecutar el programa?
    
Se necesita tener instalado Python .
Desde la terminal se puede ejecutar:

```bash

Python eight_puzzle.py

```

El programa mostrará para cada instancia el algoritmo utilizado, el número de movimientos, los nodos expandidos y el tiempo de ejecución.
