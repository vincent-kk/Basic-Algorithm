import sys
from typing import List

input = sys.stdin.readline


def solution(nodes: int, board: List[List[int]]) -> List[List[int]]:
    answer = []
    for n in range(nodes):
        visited = [0] * nodes
        stack = [n]

        while stack:
            this = stack[-1]
            remove = True
            for d in range(nodes):
                if visited[d]:
                    continue
                if board[this][d]:
                    visited[d] = 1
                    stack.append(d)
                    remove = False
                    break
            if remove:
                stack.pop()
        answer.append(visited)
    return answer


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

answer = solution(N, board)

for r in range(N):
    for c in range(N):
        print(answer[r][c], end=" ")
    print()