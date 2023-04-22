from typing import Dict, List, Set


def dfs(graph: Dict[float, List[float]], node: float) -> None:
    visited = set()
    stack = [node]

    while stack:
        current_node = stack.pop()
        print(f"{current_node=}")

        for child in reversed(graph[current_node]):
            if child in visited:
                continue

            visited.add(child)
            stack.append(child)


def dfs_recursive(graph: Dict[float, List[float]], node: float, visited: Set[float] = set()) -> None:
    print(f"{node=}")
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

    dfs(graph, 5)
    dfs_recursive(graph, 5)
