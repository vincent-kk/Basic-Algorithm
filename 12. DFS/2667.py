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

    count = 0
    blocks = []
    for r in range(row):
        for c in range(calumn):
            if board[r][c]:
                blocks.append(dfs(r, c, board))
                count += 1
    return count, sorted(blocks)


N = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
count, blocks = solution(board)
print(count)
for block in blocks:
    print(block)