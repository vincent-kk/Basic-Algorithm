from collections import defaultdict


def solution(N, road, K):
    edges = defaultdict(list)
    costs = defaultdict(lambda: 10001)
    for s, d, c in road:
        edges[s].append(d)
        edges[d].append(s)

        key = f"{s}-{d}" if s < d else f"{d}-{s}"
        costs[key] = min(costs[key], c)

    start = 1
    stack = [(start, 0)]
    visited = set([start])

    while stack:
        this, cost = stack[-1]
        pop = True

        for n in edges[this]:
            if n in visited:
                continue
            c = costs[f"{this}-{n}" if this < n else f"{n}-{this}"]
            if cost + c > K:
                continue
            visited.add(n)
            stack.append((n, cost + c))
            pop = False
        if pop:
            stack.pop()

    return len(visited)


if __name__ == "__main__":
    n = 5
    i = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    k = 3
    print(solution(n, i, k))
