from typing import List
import heapq


def solution(jobs: List[List[int]]):
    execution_time, now, index = 0, 0, 0
    start = -1
    size = len(jobs)
    pq = []

    while index < size:
        for arrive, execution in jobs:
            if start < arrive <= now:
                heapq.heappush(pq, [execution, arrive])
        if pq:
            execution, arrive = heapq.heappop(pq)
            start = now
            now += execution
            execution_time += now - arrive
            index += 1
        else:
            now += 1

    return execution_time // size


if __name__ == "__main__":
    j = [[0, 3], [1, 9], [4, 6]]
    print(solution(j))