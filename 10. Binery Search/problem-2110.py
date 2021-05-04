import sys
from typing import List


def solution(N: int, C: int, houses: List[int]):
    low, high = 0, 10 ** 8
    maximum = low
    houses.sort()

    while high >= low:
        pivot = (high + low) // 2

        routers = 0
        routerX = 0
        for house in houses:
            if house > routerX:
                routerX = house + pivot
                routers += 1
        if routers < C:
            high = pivot - 1
        else:
            low = pivot + 1
            maximum = low if low > maximum else maximum

    return maximum


N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
print(solution(N, C, houses))
