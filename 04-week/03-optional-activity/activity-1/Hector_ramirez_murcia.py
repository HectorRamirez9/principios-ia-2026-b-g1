# 8-puzzle: comparación de BFS, UCS y A*
# Este programa prueba tres formas de buscar una solución.

import heapq
import time
from collections import deque

# Estado que queremos conseguir.
# El 0 representa el espacio vacío.
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

N = 3


def successors(state):
    """Genera los movimientos que se pueden hacer desde un estado."""

    zero = state.index(0)
    row, col = divmod(zero, N)

    # Posibles movimientos del espacio vacío.
    moves = [
        (-1, 0, "Arriba"),
        (1, 0, "Abajo"),
        (0, -1, "Izquierda"),
        (0, 1, "Derecha")
    ]

    for dr, dc, move in moves:
        new_row = row + dr
        new_col = col + dc

        # Revisamos que el movimiento no salga del tablero.
        if 0 <= new_row < N and 0 <= new_col < N:
            new_zero = new_row * N + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            yield tuple(new_state), move


def manhattan(state):
    """Calcula la distancia Manhattan de las fichas."""

    total = 0

    for i, tile in enumerate(state):
        # El espacio vacío no se cuenta.
        if tile == 0:
            continue

        # Posición que debería tener la ficha.
        goal_row, goal_col = divmod(tile - 1, N)

        # Posición actual de la ficha.
        row, col = divmod(i, N)

        # Distancia entre las dos posiciones.
        total += abs(row - goal_row) + abs(col - goal_col)

    return total


def bfs(start):
    """Busca la solución usando BFS."""

    queue = deque([(start, [])])
    visited = {start}
    expanded = 0

    while queue:
        state, path = queue.popleft()
        expanded += 1

        if state == GOAL:
            return path, expanded

        for next_state, move in successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [move])
                )

    return None, expanded


def uniform_cost_search(start):
    """Busca la solución usando costo uniforme (UCS)."""

    # Como cada movimiento cuesta 1, UCS se parece mucho a BFS.
    heap = [(0, 0, start, [])]
    best_g = {start: 0}
    counter = 0
    expanded = 0

    while heap:
        g, _, state, path = heapq.heappop(heap)

        # Si ya encontramos un costo mejor, ignoramos este estado.
        if g != best_g.get(state):
            continue

        expanded += 1

        if state == GOAL:
            return path, expanded

        for next_state, move in successors(state):
            new_g = g + 1

            if new_g < best_g.get(next_state, float("inf")):
                best_g[next_state] = new_g
                counter += 1

                heapq.heappush(
                    heap,
                    (new_g, counter, next_state, path + [move])
                )

    return None, expanded


def a_star(start):
    """Busca la solución usando A* y distancia Manhattan."""

    # A* utiliza f(n) = g(n) + h(n).
    # g = costo recorrido
    # h = distancia Manhattan
    initial_h = manhattan(start)

    heap = [(initial_h, 0, 0, start, [])]
    best_g = {start: 0}
    counter = 0
    expanded = 0

    while heap:
        f, g, _, state, path = heapq.heappop(heap)

        if g != best_g.get(state):
            continue

        expanded += 1

        if state == GOAL:
            return path, expanded

        for next_state, move in successors(state):
            new_g = g + 1

            if new_g < best_g.get(next_state, float("inf")):
                best_g[next_state] = new_g
                counter += 1

                # Calculamos la heurística Manhattan.
                h = manhattan(next_state)

                # A* ordena los estados por g + h.
                heapq.heappush(
                    heap,
                    (
                        new_g + h,
                        new_g,
                        counter,
                        next_state,
                        path + [move]
                    )
                )

    return None, expanded


def benchmark(instances):
    """Ejecuta los tres algoritmos y muestra sus resultados."""

    algorithms = {
        "BFS": bfs,
        "UCS": uniform_cost_search,
        "A*": a_star
    }

    for name, start in instances.items():

        print("\n" + name)
        print("Estado inicial:", start)

        for algorithm_name, algorithm in algorithms.items():

            start_time = time.perf_counter()

            path, expanded = algorithm(start)

            elapsed = (
                time.perf_counter() - start_time
            ) * 1000

            print(
                f"{algorithm_name:4} | "
                f"Movimientos: {len(path):2d} | "
                f"Nodos: {expanded:6d} | "
                f"Tiempo: {elapsed:10.3f} ms"
            )


if __name__ == "__main__":

    # Tres casos para comparar los algoritmos.
    instances = {
        "Instancia 1 (fácil)": (
            1, 2, 3,
            4, 5, 6,
            0, 7, 8
        ),

        "Instancia 2 (media)": (
            1, 2, 3,
            5, 0, 6,
            4, 7, 8
        ),

        "Instancia 3 (difícil)": (
            8, 6, 7,
            2, 5, 4,
            3, 0, 1
        )
    }

    benchmark(instances)
