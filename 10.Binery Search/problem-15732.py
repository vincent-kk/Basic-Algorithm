import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, K: int, D: int, rules: List[int]):
    low, high = 1, N
    while high > low:
        pivot = (low + high) // 2
        acorn = D
        for start, end, step in rules:
            if start > pivot:
                continue
            end = end if end < pivot else pivot
            need = ((end - start) // step) + 1
            acorn -= need
            if acorn < 0:
                break
        if acorn > 0:
            low = pivot + 1
        else:
            high = pivot
    return (low + high) // 2


if __name__ == "__main__":
    N, K, D = map(int, input().split())
    rules = [list(map(int, input().split())) for _ in range(K)]
    print(solution(N, K, D, rules))
