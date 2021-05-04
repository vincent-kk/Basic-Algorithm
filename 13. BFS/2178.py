from sys import stdin
from collections import deque

input = stdin.readline


def solution(board, R, C) -> int:
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    queue = deque([(0, 0, 1)])
    board[0][0] = 0
    while queue:
        tr, tc, path = queue.popleft()
        if (tr, tc) == (R - 1, C - 1):
            return path
        for dr, dc in directions:
            r, c = tr + dr, tc + dc
            if 0 <= r < R and 0 <= c < C:
                if board[r][c]:
                    board[r][c] = 0
                    queue.append((r, c, path + 1))

    return -1


N, M = map(int, input().split())
board = [list(map(int, list(input()[:-1]))) for _ in range(N)]
print(solution(board, N, M))
