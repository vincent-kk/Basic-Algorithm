import sys

from operator import itemgetter
from typing import List

input = sys.stdin.readline


def solution(N: int, timetable: List):
    if N == 0:
        return 0
    timetable.sort(key=itemgetter(0))
    timetable.sort(key=itemgetter(1))
    usable = 0
    finish_time = -1
    for start, end in timetable:
        if start >= finish_time:
            finish_time = end
            usable += 1
    return usable


N = int(input())
timetable = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, timetable))