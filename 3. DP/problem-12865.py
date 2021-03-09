import sys
from typing import List, Tuple

input = sys.stdin.readline


def solution(N: int, W: int, items: List[Tuple[int]]):
    __cache__ = [0] * (W + 1)

    for w, v in items:
        if w < W:
            if w in __cache__:
                __cache__[w] = max(__cache__[w], v)
            else:
                __cache__[w] = v

    for limit in range(1, W + 1):
        local_max = 0
        for w, v in items:
            if limit < w:
                continue
            local_max = max(local_max, __cache__[limit - w] + v)

        __cache__[limit] = local_max

    return __cache__[W]


N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(N, W, items))
