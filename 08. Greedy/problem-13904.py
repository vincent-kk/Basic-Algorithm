import sys
from typing import List

input = sys.stdin.readline


def solution(n: int, schedules: List):
    schedules.sort(key=lambda s: s[1], reverse=True)

    maxdue = max(schedules, key=lambda task: task[0])[0]
    total = 0
    timetable = [True] * (maxdue + 1)

    for due, score in schedules:
        pickup = -1
        for i in range(due, 0, -1):
            if timetable[i]:
                pickup = i
                break
        if pickup >= 0:
            timetable[pickup] = False
            total += score

    return total


N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, schedules))
