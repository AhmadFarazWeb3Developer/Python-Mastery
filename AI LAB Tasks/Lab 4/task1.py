mygraph = {
    "1": ["2", "3", "4"],
    "2": ["5", "6"],
    "3": [],
    "4": ["7", "8"],
    "5": ["9", "10"],
    "6": [],
    "7": ["11", "12"],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": []
}

# BFS implementation


def bfs(graph, start, goal):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(f"Visiting: {node}")

        if node == goal:
            print(f"Goal {goal} reached!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# DFS implementation


def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    print(f"Visiting: {start}")
    if start == goal:
        print(f"Goal {goal} reached!")
        return True

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False


# Running BFS
print("BFS Traversal:")
bfs(mygraph, "1", "11")

print("\nDFS Traversal:")
dfs(mygraph, "1", "11")
