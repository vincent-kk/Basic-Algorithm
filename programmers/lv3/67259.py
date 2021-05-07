from typing import List
from collections import deque


def solution(board: List[List[int]]):
    N = len(board)
    INF = N * N * 500 + 1
    min_cost = [[INF] * N for _ in range(N)]

    # 0: Down, 1: Right, 2: Up, 3: Left
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # r, c, head, cost
    start1 = (0, 0, 0, 0)
    start2 = (0, 0, 1, 0)
    min_cost[0][0] = 0

    queue = deque([start1, start2])

    while queue:
        tr, tc, head, cost = queue.popleft()

        if tr == N - 1 and tc == N - 1:
            min_cost[tr][tc] = cost if cost < min_cost[tr][tc] else min_cost[tr][tc]
            continue

        for h, (dr, dc) in enumerate(directions):
            r, c = tr + dr, tc + dc
            if 0 <= r < N and 0 <= c < N:
                next_cost = cost + (100 if h == head else 600)
                if not board[r][c] and next_cost <= min_cost[r][c]:
                    min_cost[r][c] = next_cost
                    queue.append((r, c, h, next_cost))

    return min_cost[N - 1][N - 1]


if __name__ == "__main__":
    i = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(solution(i))