from sys import stdin
from collections import defaultdict, deque
import heapq


input = stdin.readline


def dfs(start, edges):
    visited = set()
    path = [start]
    stack = [start]
    visited.add(start)
    while stack:
        this = stack[-1]
        remove = True
        for near in edges[this]:
            if near in visited:
                continue
            stack.append(near)
            path.append(near)
            visited.add(near)
            remove = False
            break
        if remove:
            stack.pop()
    return path


def bfs(start, edges):
    visited = set()
    path = [start]
    queue = deque([start])
    visited.add(start)
    while queue:
        this = queue.popleft()
        for near in edges[this]:
            if near in visited:
                continue
            queue.append(near)
            path.append(near)
            visited.add(near)
    return path


N, M, V = map(int, input().split())
edges = defaultdict(list)

for _ in range(M):
    s, d = map(int, input().split())
    if d in edges[s] or s in edges[d]:
        continue
    edges[s].append(d)
    edges[d].append(s)

for k in edges.keys():
    edges[k].sort()

dfs_path = dfs(V, edges)
bfs_path = bfs(V, edges)

for n in dfs_path:
    print(n, end=" ")
print()

for n in bfs_path:
    print(n, end=" ")
print()