import sys
from typing import List

input = sys.stdin.readline


def solution(L: int, N: int, rf: int, rb: int, stops: List):
    unit_diff = rf - rb
    stops.sort(key=lambda stop: stop[1], reverse=True)

    prev_stop = 0
    maximum_venefit = 0
    for this_stop, venefit in stops:
        if this_stop < prev_stop:
            continue
        rest_time = (this_stop - prev_stop) * unit_diff
        maximum_venefit += venefit * rest_time
        prev_stop = this_stop

    return maximum_venefit


L, N, rf, rb = map(int, input().split())
rest_stops = [list(map(int, input().split())) for _ in range(N)]

print(solution(L, N, rf, rb, rest_stops))
