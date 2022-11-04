# Representation av viktad graf:
#  {'A': [[1, B], [4, C]]} där index [n][0] svarar vikten och [n][1] svarar mot barnet eller grannoden
# 0 <= n <= len(value) - 1


graph = {'A': [[1, 'B'], [4, 'C']],
         'B': [[1, 'A'], [2, 'E'], [7, 'F']],
         'C': [[4, 'A'], [1, 'D']],
         'D': [[1, 'C'], [2, 'F']],
         'E': [[2, 'B'], [3, 'F']],
         'F': [[7, 'B'], [2, 'D'], [3, 'E']]}


# Representation av infomap:
# key är en nod i grafen och value är en lista med längd 2,
# där index 0 svarar mot kortaste vägen från startnoden och index 1 svarar mot föregående nod i vägen

def graph_to_infomap(graph):
    return {key: [float('inf'), None] for key in graph}


def dijkstras(graph, start_node):
    unvisited = [key for key in graph]
    visited = []
    infomap = graph_to_infomap(graph)
    infomap[start_node][0] = 0
    current_node = start_node

    while unvisited:
        for child_index in range(len(graph[current_node])):
            new_path = infomap[current_node][0] + graph[current_node][child_index][0]

            # Continue om längre än kortast hittils eller redan besökt
            if new_path >= infomap[graph[current_node][child_index][1]][0] or graph[current_node][child_index][1] in visited:
                continue

            infomap[graph[current_node][child_index][1]] = [new_path, current_node]

        current_node = min(((key, infomap[key][0]) for key in unvisited), key=lambda x: x[1])[0]
        unvisited.remove(current_node)
        visited.append(current_node)
        print(current_node, unvisited)

    return infomap


print(dijkstras(graph, 'A'))
