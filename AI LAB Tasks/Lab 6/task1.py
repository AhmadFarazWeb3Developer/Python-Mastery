mygraph = {
    "A": [("B", 2), ("E", 3)],
    "B": [("C", 1), ("G", 9)],
    "C": [],
    "E": [("D", 6)],
    "D": [("G", 1)],
    "G": []
}

H_table = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}


def path_cost_a_star(path):
    total_g_cost = sum(cost for _, cost in path[1:])
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = total_g_cost + h_cost
    return f_cost


def my_a_star(mygraph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    expansion_order = []

    while queue:
        queue.sort(key=path_cost_a_star)
        path = queue.pop(0)
        node = path[-1][0]

        if node not in visited:
            visited.append(node)
            expansion_order.append(node)

            if node == goal:
                return path, expansion_order

            else:
                for (node2, cost) in mygraph.get(node, []):
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)

    return None, expansion_order


answer_path, expansion_order = my_a_star(mygraph, "A", "G")

shortest_path = [node for node, _ in answer_path]
total_cost = sum(cost for _, cost in answer_path[1:])

print("1. Shortest Path:", shortest_path)
print("2. Total Path Cost:", total_cost)
print("3. Order of Node Expansion:", expansion_order)
