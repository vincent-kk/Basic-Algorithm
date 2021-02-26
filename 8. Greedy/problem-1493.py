import sys
from typing import List

input = sys.stdin.readline


def solution(L: int, W: int, H: int, cubs: List):
    minimum_edge = min(L, W, H)

    return


L, W, H = map(int, input().split())
N = int(input())
cubes = [list(map(int, input().split())) for _ in range(N)]

print(solution(L, W, H, cubes))
