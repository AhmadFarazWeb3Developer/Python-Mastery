myGraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


visited = []


def dfs(visited, myGraph, startNode):
    if startNode not in visited:
        a = myGraph[startNode]
        visited.append(startNode)
        for neighbors in a:
            dfs(visited, myGraph, neighbors)


dfs(visited, myGraph, "A")
print('Visited Path ', visited)
