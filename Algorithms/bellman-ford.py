from typing import Dict, List, Tuple


def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, int]:
    connected_edges = []
    queue = [source]
    visited = {source}

    while queue:
        vertex = queue.pop()
        children = graph[vertex]
        if not children:
            continue

        for child, weight in children:
            connected_edges.append((vertex, child, weight))
            if child not in visited:
                queue.append(child)
                visited.add(child)

    vertex_dist = {vertex: float("inf") for vertex in graph}
    vertex_dist[source] = 0

    for i in range(len(connected_edges)):
        for edge_source, edge_destination, edge_weight in connected_edges:
            if vertex_dist[edge_source] + edge_weight < vertex_dist[edge_destination]:
                if not i or i < len(connected_edges) - 1:
                    vertex_dist[edge_destination] = vertex_dist[edge_source] + edge_weight
                    continue

                vertex_dist[edge_destination] = float("-inf")

    return vertex_dist


if __name__ == "__main__":
    graph = {0: [(1, 999), (3, 2)],
             1: [(2, -2)],
             2: [(1, 1)],
             3: [],
             4: []}

    graph2 = {0: [(1, -100)],
              1: []}

    graph3 = {0: [(1, 1)],
              1: [(2, 1)],
              2: [(3, 1)],
              3: [(4, 1)],
              4: [(5, 1)],
              5: [(6, 1)],
              6: [(7, 1)],
              7: []}

    graph4 = {0: [(1, 1)],
              1: [(2, -3)],
              2: [(0, 1)]}

    print(bellman_ford(graph, 0))   # {0: 0, 1: -inf, 2: -inf, 3: 2, 4: inf}
    print(bellman_ford(graph2, 0))  # {0: 0, 1: -100}
    print(bellman_ford(graph3, 0))  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    print(bellman_ford(graph4, 0))  # {0: -inf, 1: -inf, 2: -inf}
