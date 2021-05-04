import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, lans: List[int]):
    low, high = 0, 2147483648
    # high가 sum(lans)나 max(lans)는 안되고 2^31 -1이여야 통과하는 이유가 무엇인가?

    while high > low + 1:
        pivot = (low + high) // 2

        # lines = 0
        # for lan in lans:
        #     lines += lan // pivot

        lines = sum([x // pivot for x in lans])

        if lines < M:
            high = pivot
        else:
            low = pivot

    return low


if __name__ == "__main__":
    N, M = map(int, input().split())
    lans = list(map(int, sys.stdin.readlines()))

    print(solution(N, M, lans))
