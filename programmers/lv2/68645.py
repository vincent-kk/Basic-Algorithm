from typing import List
from itertools import chain


def solution(n: int) -> List[int]:

    answer = [[0 for _ in range(i)] for i in range(1, n + 1)]
    direction = [(1, 0), (0, 1), (-1, -1)]
    step = 0
    x, y = -1, 0
    for snail in range(n):
        for _ in range(snail, n):
            dx, dy = direction[snail % 3]
            x += dx
            y += dy
            step += 1
            answer[x][y] = step
    return list(chain(*answer))


if __name__ == "__main__":
    i = 4
    print(solution(i))
