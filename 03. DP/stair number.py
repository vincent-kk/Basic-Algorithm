from sys import stdin
from functools import lru_cache

input = stdin.readline


@lru_cache(maxsize=None)
def run(n: int):
    if n == 0:
        return [0]*10
    if n == 1:
        return [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result = [0]*10
    for i in range(10):
        if i == 0:
            result[i] = run(n-1)[i+1] % 1000000000
        elif i == 9:
            result[i] = run(n-1)[i-1] % 1000000000
        else:
            result[i] = ((run(n-1)[i-1]) + (run(n-1)[i+1])) % 1000000000
    return result


n = int(input())

print(sum(run(n)) % 1000000000)
