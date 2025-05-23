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


def heuristic_cost(path):

    return H_table[path[-1][0]]


def greedy_best_first_search(graph, start, goal):

    visited = set()
    queue = [[(start, 0)]]
    expansion_order = []

    while queue:
        queue.sort(key=heuristic_cost)
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


answer_path, expansion_order = greedy_best_first_search(mygraph, "A", "J")


shortest_path = [node for node, _ in answer_path]

total_cost = sum(cost for _, cost in answer_path[1:])


print("1. Shorest path : ", shortest_path)

print("2. Total Path Cost : ", total_cost)

print("3. Order of Node Expension : ", expansion_order)
