import sys
from typing import List

input = sys.stdin.readline


def solution(board: List[List[int]]) -> int:
    row, calumn = len(board), len(board[0])
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def dfs(r, c, board):
        stack = [(r, c)]
        board[r][c] = 0
        size = 1
        while stack:
            tr, tc = stack[-1]
            remove = True
            for dr, dc in directions:
                if 0 <= tr + dr < row and 0 <= tc + dc < calumn:
                    if board[tr + dr][tc + dc]:
                        board[tr + dr][tc + dc] = 0
                        stack.append((tr + dr, tc + dc))
                        remove = False
                        size += 1
                        break
            if remove:
                stack.pop()
        return size

    global_max = -1
    for r in range(row):
        for c in range(calumn):
            if board[r][c]:
                local_max = dfs(r, c, board)
                global_max = local_max if local_max > global_max else global_max

    return global_max


N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1
print(solution(board))