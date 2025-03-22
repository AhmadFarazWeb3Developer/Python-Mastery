myGraph = {
    "S": [("A", 6), ("B", 5), ("C", 10)],
    "A": [("E", 6)],
    "B": [("E", 7), ("D", 4)],
    "C": [("D", 6)],
    "D": [("F", 6)],
    "E": [("F", 4)],
    "F": [("G", 3)],
    "G": []
}

H_table = {"S": 17, "A": 10, "B": 13, "C": 4, "D": 2, "E": 4, "F": 1, "G": 0}


def path_cost_gbfs(path):

    return H_table[path[-1][0]]


def mygbfs(mygraph, start, goal):

    visited = set()
    queue = [[(start, 0)]]
    expansion_order = []

    while queue:
        queue.sort(key=path_cost_gbfs)
        path = queue.pop(0)
        node = path[-1][0]

        if node not in visited:
            visited.add(node)
            expansion_order.append(node)

            if node == goal:
                return path, expansion_order

            for neighbor, cost in mygraph.get(node, []):
                new_path = path.copy()
                new_path.append((neighbor, cost))
                queue.append(new_path)

    return None, expansion_order


answer_path, expansion_order = mygbfs(myGraph, "S", "G")

shortest_path = [node for node, _ in answer_path]
total_cost = sum(cost for _, cost in answer_path[1:])


print("1. Shorest path : ", shortest_path)

print("2. Total Path Cost : ", total_cost)

print("3. Order of Node Expension : ", expansion_order)
