from collections import deque
from typing import Dict, List, Set


def dfs(graph: Dict[float, List[float]], node: float) -> None:
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


def dfs_recursive(graph: Dict[float, List[float]], node: float, visited: Set[float] = set()) -> None:
    print(node)
    visited.add(node)
    if not graph[node]:
        return

    for child in graph[node]:
        if child in visited:
            continue
        dfs_recursive(graph, child)


if __name__ == "__main__":
    graph = {5: [3, 7],
             3: [2, 4],
             7: [8],
             2: [],
             4: [8],
             8: []}

    dfs_recursive(graph, 5)