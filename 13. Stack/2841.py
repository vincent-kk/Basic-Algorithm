import sys
from collections import defaultdict
from typing import List, Tuple

input = sys.stdin.readline


def solution(N: int, P: int, code: List[Tuple[int]]):
    fingers = defaultdict(list)
    movement = 0
    for s, p in code:
        while len(fingers[s]) > 0:
            if p < fingers[s][-1]:
                fingers[s].pop()
                movement += 1
            else:
                break
        if not (len(fingers[s]) > 0 and fingers[s][-1] == p):
            fingers[s].append(p)
            movement += 1

    return movement


if __name__ == "__main__":
    N, P = map(int, input().split())
    code = [tuple(map(int, input().split())) for _ in range(N)]
    print(solution(N, P, code))
