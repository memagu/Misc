from collections import deque
from typing import Dict, List, Tuple


def shortest_path_faster_algorithm(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, int]:
    connected_edges = deque()
    queue = [source]
    visited = {source}

    while queue:
        vertex = queue.pop()
        for child, weight in graph[vertex]:
            connected_edges.append((vertex, child, weight))
            if child not in visited:
                queue.append(child)
                visited.add(child)

    edge_queue = connected_edges.copy()
    vertex_dist = {vertex: float("inf") for vertex in graph}
    vertex_dist[source] = 0
    vertex_len = {vertex: 0 for vertex in graph}

    loop_detector = set()

    while edge_queue:
        print(edge_queue)
        if not edge_queue:
            break

        t_edge_queue = tuple(edge_queue)
        if t_edge_queue in loop_detector:
            for edge_source, edge_destination, edge_weight in edge_queue:
                vertex_dist[edge_destination] = float("-inf")
            break

        loop_detector.add(t_edge_queue)

        added = set()

        for _ in range(len(edge_queue)):
            edge_source, edge_destination, edge_weight = edge_queue.popleft()
            vertex_len[edge_source] += 1
            if vertex_dist[edge_source] + edge_weight < vertex_dist[edge_destination]:
                if vertex_len[edge_source] == len(graph):
                    vertex_dist[edge_destination] = float("-inf")
                else:
                    vertex_dist[edge_destination] = vertex_dist[edge_source] + edge_weight

                if edge_source in added:
                    continue

                add_queue = [edge_destination]
                while add_queue:
                    vertex = add_queue.pop()
                    for child, weight in graph[vertex]:
                        if child in added:
                            continue

                        added.add(child)
                        add_queue.append(child)
                        edge_queue.append((vertex, child, weight))

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

    graph5 = {0: [(1, 1)],
              1: [(2, -4)],
              2: [(3, 1)],
              3: [(0, 1)]}

    graph6 = {0: [(1, 10)],
              1: [(2, 1)],
              2: [(3, 3)],
              3: [(4, 22), (5, -10)],
              4: [],
              5: [(1, 4)],
              }

    print(shortest_path_faster_algorithm(graph, 0))   # {0: 0, 1: -inf, 2: -inf, 3: 2, 4: inf}
    print(shortest_path_faster_algorithm(graph2, 0))  # {0: 0, 1: -100}
    print(shortest_path_faster_algorithm(graph3, 0))  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    print(shortest_path_faster_algorithm(graph4, 0))  # {0: -inf, 1: -inf, 2: -inf}
    print(shortest_path_faster_algorithm(graph5, 0))  # {0: -inf, 1: -inf, 2: -inf, 3: -inf}
    print(shortest_path_faster_algorithm(graph6, 0))  # {0: -inf, 1: -inf, 2: -inf, 3: -inf}
