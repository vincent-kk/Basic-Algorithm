import sys
from copy import deepcopy
from typing import List, Tuple

input = sys.stdin.readline


def dfs(r, c, image, special=False):
    row, calumn = len(image), len(image[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    target, image[r][c] = image[r][c], -1
    checker = lambda x: x == target
    if special and (target == 1 or target == 2):
        checker = lambda x: x == 1 or x == 2

    stack = [(r, c)]
    while stack:
        tr, tc = stack[-1]
        remove = True
        for dr, dc in directions:
            x, y = tr + dr, tc + dc
            if 0 <= x < row and 0 <= y < calumn:
                if checker(image[x][y]):
                    image[x][y] = -1
                    stack.append((x, y))
                    remove = False
                    break
        if remove:
            stack.pop()


def solution(image: List[List[str]]) -> Tuple[int]:
    row, calumn = len(image), len(image[0])
    nomal = 0
    special = 0

    image_capy1 = deepcopy(image)

    for r in range(row):
        for c in range(calumn):
            if image_capy1[r][c] > 0:
                dfs(r, c, image_capy1)
                nomal += 1

    image_capy2 = deepcopy(image)
    for r in range(row):
        for c in range(calumn):
            if image_capy2[r][c] > 0:
                dfs(r, c, image_capy2, special=True)
                special += 1

    return nomal, special


N = int(input())

image = [
    list(
        map(
            lambda c: 1 if c == "R" else 2 if c == "G" else 3 if c == "B" else -1,
            list(input()[:-1]),
        )
    )
    for _ in range(N)
]

n, c = solution(image)
print(n, c)
