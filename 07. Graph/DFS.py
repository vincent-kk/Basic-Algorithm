def dfs(nodes, edges, start):
    size = len(nodes)
    checks = [False] * size
    stack = []

    path = []

    # init dfs
    stack.append(start)
    checks[start] = True

    path.append(start)

    # do dfs
    while len(stack) > 0:
        this = stack[-1]
        remain = False
        for n in range(len(edges[this])):
            if not checks[edges[this][n]]:
                checks[edges[this][n]] = True
                path.append(edges[this][n])
                stack.append(edges[this][n])
                remain = True
                break
        if not remain:
            stack.pop()
    print(path)


def dfs2(nodes, edges, start):
    size = len(nodes)
    checks = [False] * size
    path = []

    def dfs_re(this):
        checks[this] = True
        path.append(this)
        for n in range(len(edges[this])):
            if not checks[edges[this][n]]:
                dfs_re(edges[this][n])

    # do dfs
    dfs_re(start)

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

dfs2(nodes, edges, 0)