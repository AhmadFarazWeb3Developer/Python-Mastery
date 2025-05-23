graph = {
    'A': ['B', 'D', 'E'],
    'B': ['C', 'G'],
    'C': [],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G']
}

# BFS Implementation


def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            print("BFS Path:", " -> ".join(path))
            return

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)


start = "A"
goal = "G"
bfs(graph, start, goal)

# DFS Implementation


def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        print("DFS Path:", " -> ".join(path))
        return True

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, path, visited):
                return True

    path.pop()
    return False


start = "A"
goal = "G"

dfs(graph, start, goal)
