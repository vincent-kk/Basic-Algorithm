import sys
from typing import List

input = sys.stdin.readline


def printStar(N: int):
    # length = 3 ** N
    result = [([True] * N) for _ in range(N)]

    def makeStar(N: int, x: int, y: int):
        if N == 3:
            result[x + 1][y + 1] = False
            return

        length: int = N
        step: int = N // 3

        for i in range(x + step, x + step * 2):
            for j in range(y + step, y + step * 2):
                result[i][j] = False

        for i in range(x, x + length, step):
            for j in range(y, y + length, step):
                if not result[i][j]:
                    continue
                makeStar(step, i, j)

    makeStar(N, 0, 0)
    return result


N = int(input())
for row in printStar(N):
    for c in row:
        print("*" if c else " ", end="")
    print()