graph = {
    "Alice": ["Bob"],
    "Bob": ["Alice", "Charlie", "David"],
    "Charlie": ["Bob", "Eve", "David"],
    "Eve": ["Charlie"],
    "David": ["Bob", "Charlie", "Frank"],
    "Frank": ["David", "Grace"],
    "Grace": ["Frank", "Hank"],
    "Hank": ["Grace", "Ivy"],
    "Ivy": ["Jack", "Hank"],
    "Jack": ["Ivy"]
}


def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


path_bfs = bfs(graph, "Bob", "Jack")
print("BFS Path:", path_bfs)
