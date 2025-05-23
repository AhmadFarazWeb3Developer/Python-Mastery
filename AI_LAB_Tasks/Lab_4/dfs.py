mygraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = []


def my_dfs(visited, mygraph, start_node):
    if start_node not in visited:
        print(start_node, end=" ")
        a = mygraph[start_node]
        visited.append(start_node)
        # print("a", a)
        for neighbors in a:
            # print("neighbor ", neighbors)
            my_dfs(visited, mygraph, neighbors)


my_dfs(visited, mygraph, "A")
