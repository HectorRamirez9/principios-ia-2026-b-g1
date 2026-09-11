from collections import deque
import heapq

# ==========================================================
# LABERINTO
# ==========================================================
# 0 = camino libre
# 1 = pared
#
# Inicio: (0, 0)
# Meta:   (4, 4)

laberinto = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)

# ==========================================================
# ESPACIO DE ESTADOS
# ==========================================================
# Cada posición (fila, columna) representa un estado.
# Se puede mover arriba, abajo, izquierda o derecha.
# No se puede pasar por paredes ni salir del laberinto.
# Estado inicial: (0, 0)
# Estado objetivo: (4, 4)
# La solución es el camino desde el inicio hasta la meta.

movimientos = [
    (-1, 0),  # arriba
    (1, 0),   # abajo
    (0, -1),  # izquierda
    (0, 1)    # derecha
]

def es_valido(posicion):
    fila, columna = posicion

    if fila < 0 or fila >= len(laberinto):
        return False

    if columna < 0 or columna >= len(laberinto[0]):
        return False

    return laberinto[fila][columna] == 0


# ==========================================================
# BFS
# ==========================================================
def bfs():
    cola = deque()
    cola.append((inicio, [inicio]))

    visitados = {inicio}
    nodos_expandidos = 0

    while cola:
        posicion, camino = cola.popleft()
        nodos_expandidos += 1

        if posicion == meta:
            return camino, nodos_expandidos

        fila, columna = posicion

        for df, dc in movimientos:
            nueva_posicion = (fila + df, columna + dc)

            if es_valido(nueva_posicion) and nueva_posicion not in visitados:
                visitados.add(nueva_posicion)
                cola.append((nueva_posicion, camino + [nueva_posicion]))

    return None, nodos_expandidos


# ==========================================================
# HEURÍSTICA MANHATTAN
# ==========================================================
def manhattan(posicion, objetivo):
    f1, c1 = posicion
    f2, c2 = objetivo
    return abs(f1 - f2) + abs(c1 - c2)


# ==========================================================
# A*
# ==========================================================
def a_estrella():
    cola = []

    g_inicial = 0
    h_inicial = manhattan(inicio, meta)

    heapq.heappush(
        cola,
        (g_inicial + h_inicial, g_inicial, inicio, [inicio])
    )

    costos = {inicio: 0}
    nodos_expandidos = 0

    while cola:
        f, g, posicion, camino = heapq.heappop(cola)
        nodos_expandidos += 1

        if posicion == meta:
            return camino, nodos_expandidos

        fila, columna = posicion

        for df, dc in movimientos:
            nueva_posicion = (fila + df, columna + dc)

            if es_valido(nueva_posicion):
                nuevo_g = g + 1

                if nueva_posicion not in costos or nuevo_g < costos[nueva_posicion]:
                    costos[nueva_posicion] = nuevo_g
                    h = manhattan(nueva_posicion, meta)
                    nuevo_f = nuevo_g + h

                    heapq.heappush(
                        cola,
                        (nuevo_f, nuevo_g, nueva_posicion,
                         camino + [nueva_posicion])
                    )

    return None, nodos_expandidos


# ==========================================================
# EJECUCIÓN Y RESULTADOS
# ==========================================================
camino_bfs, nodos_bfs = bfs()
camino_a, nodos_a = a_estrella()

print("====================================")
print("       RESULTADOS DEL LABERINTO")
print("====================================")

print("\nCamino encontrado por BFS:")
print(camino_bfs)

print("\nNodos expandidos por BFS:")
print(nodos_bfs)

print("\nCamino encontrado por A*:")
print(camino_a)

print("\nNodos expandidos por A*:")
print(nodos_a)

print("\n====================================")

if nodos_bfs < nodos_a:
    print("BFS fue más eficiente porque expandió menos nodos.")
elif nodos_a < nodos_bfs:
    print("A* fue más eficiente porque expandió menos nodos.")
else:
    print("Los dos algoritmos expandieron la misma cantidad de nodos.")

print("====================================")
