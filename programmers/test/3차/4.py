import heapq


def solution(n, works):
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)

    for _ in range(n):
        work = heapq.heappop(works)
        if work == 0:
            works = [0]
            break
        work += 1
        heapq.heappush(works, work)

    return sum([w * w for w in works])
