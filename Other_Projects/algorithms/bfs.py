from collections import deque
from typing import Dict, List


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
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        print(f"{current_node=}")

        for child in graph[current_node]:
            if child in visited:
                continue

            visited.add(child)
            queue.append(child)


if __name__ == "__main__":
    graph = {5: [3, 7],
             3: [2, 4],
             7: [8],
             2: [],
             4: [8],
             8: []}

    bfs_with_depth(graph, 5)
    print()
    bfs_with_depth(graph, 3)
    print()
    bfs_with_depth(graph, 7)

    print()
    print()

    bfs(graph, 5)
    print()
    bfs(graph, 3)
    print()
    bfs(graph, 7)
