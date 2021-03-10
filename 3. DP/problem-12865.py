import sys
from typing import List, Tuple

input = sys.stdin.readline


def solution(N: int, W: int, items: List[Tuple[int]]):
    __cache__ = [0] * (W + 1)

    for w, v in items:
        prev_state = __cache__[:]
        for limit in range(1, W + 1):
            if limit < w:
                continue
            __cache__[limit] = max(prev_state[limit], prev_state[limit - w] + v)

    return __cache__[W]


N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(N, W, items))
