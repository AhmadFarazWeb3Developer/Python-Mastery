mygraph = {
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


def path_cost_gbfs(path):
    total_g_cost = 0
    for (node, g_cost) in path:
        total_g_cost = total_g_cost + g_cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost, last_node


def mygbfs(mygraph, start, goal):
    visited = []  # keeping track reocord of visited
    queue = [[(start, 0)]]  # queue of lists
    # print("Queue: ", queue)
    while queue:
        queue.sort(key=path_cost_gbfs)  # sort on the bais of h_cost and g_cost
        print("Queue: ", queue)
        path = queue.pop(0)
        node = path[-1][0]  # get the last node of path
        print('Path: ', path)
        if node not in visited:  # check if node is not visited
            visited.append(node)
            if node == goal:
                return path
            else:
                neighbour_nodes = mygraph.get(node, [])
                print("Neighbour Node: ", neighbour_nodes)
                for (node2, cost) in neighbour_nodes:
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)
        else:
            continue


answer_path = mygbfs(mygraph, "S", "G")
print("Shortest Path is: ", answer_path)
