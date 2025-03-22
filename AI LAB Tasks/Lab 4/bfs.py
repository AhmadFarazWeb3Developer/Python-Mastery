mygraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = []
queue = []


def my_bfs(visited, mygraph, start_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        a = queue.pop(0)

        for neighbors in mygraph[a]:
            print("Node of ", a, " ", neighbors)
            if neighbors not in visited:
                visited.append(neighbors)
                queue.append(neighbors)


my_bfs(visited, mygraph, "A")
