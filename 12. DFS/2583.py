import sys
from typing import List

input = sys.stdin.readline


def dfs(r, c, board: List[List[int]]) -> int:
    row, calumn = len(board), len(board[0])
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
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
                    size += 1
                    stack.append((tr + dr, tc + dc))
                    remove = False
                    break

        if remove:
            stack.pop()

    return size


def solution(board: List[List[int]]) -> int:
    row, calumn = len(board), len(board[0])
    count = 0
    area = []
    for r in range(row):
        for c in range(calumn):
            if board[r][c]:
                area.append(dfs(r, c, board))
                count += 1
    return count, sorted(area)


R, C, K = map(int, input().split())
board = [[1] * C for _ in range(R)]
for _ in range(K):
    lc, lr, rc, rr = map(int, input().split())
    for r in range(lr, rr):
        for c in range(lc, rc):
            board[r][c] = 0

count, area = solution(board)

print(count)
for a in area:
    print(a, end=" ")
print()