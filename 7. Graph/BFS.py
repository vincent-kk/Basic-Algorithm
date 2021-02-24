def bfs(nodes, edges, start):
    size = len(nodes)
    checks = [False] * size
    queue = []

    path = []

    # init dfs
    queue.append(start)
    checks[start] = True
    path.append(start)

    # do dfs
    while len(queue) > 0:
        this = queue.pop(0)
        for n in range(len(edges[this])):
            if not checks[edges[this][n]]:
                checks[edges[this][n]] = True
                path.append(edges[this][n])
                queue.append(edges[this][n])

    print(path)


nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [
    [1, 3, 7, 8],
    [0, 2, 3],
    [1],
    [0, 1, 4, 5],
    [3],
    [3],
    [8, 9],
    [0, 9],
    [0, 6],
    [6, 7],
]

for i in range(len(nodes)):
    print(nodes[i], edges[i])

bfs(nodes, edges, 0)