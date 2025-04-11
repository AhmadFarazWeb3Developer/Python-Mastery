
myGraph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


visited = []
queue = []


def bfs(startNode, myGraph):
    visited.append(startNode)
    queue.append(startNode)

    while queue:
        a = queue.pop(0)
        for neighbors in myGraph[a]:
            if neighbors not in visited:
                visited.append(neighbors)
                # visited.append("->")
                queue.append(neighbors)
    print("Visited Path ", visited)


bfs("A", myGraph)
