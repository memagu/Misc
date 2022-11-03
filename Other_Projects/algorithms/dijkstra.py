from typing import Dict, Optional, Tuple


def dijkstra(graph: Dict[str, Tuple[Tuple[str, float], Tuple[str, float]]], node: str) -> Dict[str, Tuple[Optional[str], float]]:
    visited = set()
    infomap = {node: (None, 0)}  # {node: (prev_node, dist), ...}
    current_node = node

    while True:
        for child, distance in graph[current_node]:

            total_distance = infomap[current_node][1] + distance

            if child not in infomap:
                infomap[child] = (current_node, total_distance)
                continue

            if infomap[child][1] <= total_distance:
                continue

            infomap[child] = (current_node, total_distance)

        visited.add(current_node)

        if len(visited) == len(graph):
            break

        current_node = min(((unvisited, infomap[unvisited][1]) for unvisited in infomap if unvisited not in visited),
                           key=lambda x: x[1])[0]

    return infomap


if __name__ == "__main__":
    graph = {'A': (('B', 1), ('C', 4)),
             'B': (('A', 1), ('E', 2), ('F', 7)),
             'C': (('A', 4), ('D', 1)),
             'D': (('C', 1), ('F', 2)),
             'E': (('B', 2), ('F', 3)),
             'F': (('B', 7), ('D', 2), ('E', 3))}

    graph_2 = {'A': (('B', 4), ('C', 2)),
               'B': (('C', 3), ('D', 2), ('E', 3)),
               'C': (('B', 1), ('D', 4), ('E', 5)),
               'D': (),
               'E': (('D', 1),)}

    print(dijkstra(graph, 'A'))  # {'A': (None, 0), 'B': ('A', 1), 'C': ('A', 4), 'E': ('B', 3), 'F': ('E', 6), 'D': ('C', 5)}
    print()
    print(dijkstra(graph_2, 'A'))  # {'A': (None, 0), 'B': ('C', 3), 'C': ('A', 2), 'D': ('B', 5), 'E': ('B', 6)}
