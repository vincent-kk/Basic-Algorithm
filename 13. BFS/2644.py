from sys import stdin
from collections import defaultdict, deque

input = stdin.readline


def solution(S, D, edges):
    checked = set()
    checked.add(S)
    queue = deque([S])
    link = 0
    while queue:
        for _ in range(len(queue)):
            this = queue.popleft()
            if this == D:
                return link
            for near in edges[this]:
                if near in checked:
                    continue
                queue.append(near)
                checked.add(near)
        link += 1
    return -1


N = int(input())
S, D = map(int, input().split())
m = int(input())
edges = defaultdict(list)

for _ in range(m):
    s, d = map(int, input().split())
    edges[s].append(d)
    edges[d].append(s)
for k in edges.keys():
    edges[k].sort()

print(solution(S, D, edges))
