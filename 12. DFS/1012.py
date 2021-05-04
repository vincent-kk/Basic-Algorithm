import sys
from typing import List

input = sys.stdin.readline


def solution(board: List[List[int]]) -> int:
    row, calumn = len(board), len(board[0])
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    worm = 0

    def dfs(r, c, board):
        stack = [(r, c)]
        board[r][c] = 0
        while stack:
            tr, tc = stack[-1]
            remove = True
            for dr, dc in directions:
                if 0 <= tr + dr < row and 0 <= tc + dc < calumn:
                    if board[tr + dr][tc + dc]:
                        board[tr + dr][tc + dc] = 0
                        stack.append((tr + dr, tc + dc))
                        remove = False
                        break
            if remove:
                stack.pop()

    for r in range(row):
        for c in range(calumn):
            if board[r][c]:
                dfs(r, c, board)
                worm += 1

    return worm


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    print(solution(board))