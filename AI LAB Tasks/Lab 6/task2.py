mygraph = {
    "A": [("B", 6), ("F", 3)],
    "B": [("C", 3), ("D", 2)],
    "C": [("E", 5)],
    "D": [("E", 8)],
    "E": [("I", 5), ("J", 5)],
    "F": [("G", 1), ("H", 7)],
    "G": [("I", 3)],
    "H": [("I", 2)],
    "I": [("J", 3)],
    "J": []
}

H_table = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6,
    'G': 5, 'H': 3, 'I': 1, 'J': 0
}


def path_cost_a_star(path):
    total_g_cost = sum(cost for _, cost in path[1:])
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return total_g_cost + h_cost


def a_star_search(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    expansion_order = []

    while queue:
        queue.sort(key=path_cost_a_star)
        path = queue.pop(0)
        node = path[-1][0]

        if node not in visited:
            visited.add(node)
            expansion_order.append(node)

            if node == goal:
                return path, expansion_order

            for neighbor, cost in graph.get(node, []):
                new_path = path.copy()
                new_path.append((neighbor, cost))
                queue.append(new_path)

    return None, expansion_order


answer_path, expansion_order = a_star_search(mygraph, "A", "J")

shortest_path = [node for node, _ in answer_path]
total_cost = sum(cost for _, cost in answer_path[1:])

print("1. Shortest Path:", shortest_path)
print("2. Total Path Cost:", total_cost)
print("3. Order of Node Expansion:", expansion_order)
