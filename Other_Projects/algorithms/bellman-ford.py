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

    edge_queue = connected_edges
    vertex_dist = {vertex: float("inf") for vertex in graph}
    vertex_dist[source] = 0

    for i in range(len(connected_edges)):
        if not edge_queue:
            break

        for _ in range(len(edge_queue)):
            edge_source, edge_destination, edge_weight = edge_queue.pop()
            if vertex_dist[edge_source] + edge_weight < vertex_dist[edge_destination]:
                if destination_children := graph[edge_destination]:
                    for child, weight in destination_children:
                        edge_queue.append((edge_destination, child, weight))

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

    print(bellman_ford(graph, 0))  # {0: 0, 1: -inf, 2: -inf, 3: 2, 4: inf}
    print(bellman_ford(graph2, 0))  # {0: 0, 1: -100}
