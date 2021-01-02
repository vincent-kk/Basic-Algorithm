from sys import stdin
from functools import lru_cache

input = stdin.readline


@lru_cache(maxsize=None)
def run(n: int):
    if n < 2:
        return n
    else:
        return run(n-1) + run(n-2)


n = int(input())

print(run(n))
