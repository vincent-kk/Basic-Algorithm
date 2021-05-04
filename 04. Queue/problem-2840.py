from sys import stdin
from collections import deque
from typing import List

input = stdin.readline


def solution(N: int, K: int, memos: List[int]):
    result = deque(["?" for _ in range(N)])
    cache = set()
    for step, code in memos:
        result.rotate(int(step))
        if result[0] == "?" and code not in cache:
            result[0] = code
            cache.add(code)
        else:
            if result[0] == code:
                continue
            else:
                return "!"

    return "".join(result)


if __name__ == "__main__":
    N, K = map(int, input().split())
    memos = [list(input().split()) for _ in range(K)]
    print(solution(N, K, memos))
