from typing import List
from collections import defaultdict, Counter
import heapq


def solution(n: int, e: List[List[int]]):
    edges = defaultdict(list)
    distances = defaultdict(lambda: n + 1)
    for s, d in e:
        edges[s].append(d)
        edges[d].append(s)

    start = 1
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        p_distance, p_destination = heapq.heappop(queue)

        if distances[p_destination] < p_distance:
            continue

        for n_destination in edges[p_destination]:
            distance = p_distance + 1
            if distance < distances[n_destination]:
                distances[n_destination] = distance
                heapq.heappush(queue, [distance, n_destination])

    counter = Counter(distances)
    m = max(counter.values())
    return len(list(filter(lambda k: counter[k] == m, counter.keys())))


if __name__ == "__main__":
    n = 6
    e = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, e))
