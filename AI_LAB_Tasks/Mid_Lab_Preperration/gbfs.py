myGraph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("B", 2), ("C", 5), ("G", 12)],
    "B": [("C", 2)],
    "C": [("G", 3)]
}

H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}


def handle_costs(path):
    total_g_cost = 0
    for (node, g_cost) in path:
        total_g_cost = total_g_cost + g_cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost, last_node


def greedy_best_first_algo(myGraph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=handle_costs)
        path = queue.pop(0)
        node = path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                neighbours_nodes = myGraph.get(node, [])
                for node2, cost in neighbours_nodes:
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)
        else:
            continue


shortest_path = greedy_best_first_algo(myGraph, "S", "G")
print("Shortest Path ", shortest_path)
