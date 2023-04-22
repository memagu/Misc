from collections import deque
from typing import Dict, List, Optional, Set


def bfs_with_depth(graph: Dict[float, List[float]], node: float) -> None:
    visited = set()
    queue = deque([node])
    depth = 0

    while queue:
        for _ in range(len(queue)):
            current_node = queue.popleft()
            print(f"{current_node=}, {depth=}")

            for child in graph[current_node]:
                if child in visited:
                    continue

                visited.add(child)
                queue.append(child)

        depth += 1


def bfs(graph: Dict[int, List[int]], node: int) -> None:
    visited = set()
    queue = deque((node,))

    while queue:
        current_node = queue.popleft()
        print(f"{current_node=}")

        for child in graph[current_node]:
            if child in visited:
                continue

            visited.add(child)
            queue.append(child)


def bfs_recursive(graph: Dict[int, List[int]], node: int, visited: Optional[Set[int]] = None, queue: Optional[deque] = None):
    if visited is None:
        visited = set()

    if queue is None:
        queue = deque((node,))

    if not queue:
        return

    current_node = queue.popleft()
    print(f"{current_node=}")

    for child in graph[current_node]:
        if child in visited:
            continue

        visited.add(child)
        queue.append(child)

    bfs_recursive(graph, current_node, visited, queue)


if __name__ == "__main__":
    graph = {5: [3, 7],
             3: [2, 4],
             7: [8],
             2: [],
             4: [8],
             8: []}

    print(bfs_with_depth.__name__)
    bfs_with_depth(graph, 5)
    print()
    bfs_with_depth(graph, 3)
    print()
    bfs_with_depth(graph, 7)

    print()
    print()

    print(bfs.__name__)
    bfs(graph, 5)
    print()
    bfs(graph, 3)
    print()
    bfs(graph, 7)

    print()
    print()

    print(bfs_recursive.__name__)
    bfs_recursive(graph, 5)
    print()
    bfs_recursive(graph, 3)
    print()
    bfs_recursive(graph, 7)
