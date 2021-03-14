import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, tasks: List[int]):
    low, high = max(tasks), sum(tasks)
    optimal = high
    # #2. 반복 조건에 high >= low 로 되어있는 것이 어떤 의미가 있는가?
    while high >= low:
        pivot = (low + high) // 2

        free = pivot
        disks = 1
        for task in tasks:
            if free - task >= 0:
                free -= task
            else:
                free = pivot - task
                disks += 1

        # #2. pivot을 포함하지 않는다?
        if disks > M:
            low = pivot + 1
        else:
            high = pivot - 1
            # #1. optimal이라는 것이 최저를 계속 갱신하는 역할을 한다.
            optimal = pivot if pivot < optimal else optimal

    return optimal


"""
def solution(N: int, M: int, tasks: List[int]):
    lesson_total = sum(tasks)
    left, right = lesson_total // M, lesson_total
    answer = right
    while left <= right:
        mid = (left + right) // 2

        if mid < max(tasks):
            left = mid + 1
            continue
        # 조건 만족 확인
        count, temp = 0, 0
        for i in range(len(tasks)):
            if tasks[i] > mid:
                break
            elif temp + tasks[i] <= mid:
                temp += tasks[i]
            else:
                temp = tasks[i]
                count += 1

        if count <= M - 1:  # 가능한 경우 (더 작은 값이 있는지 확인해야 한다)
            right = mid - 1
            answer = min(answer, mid)  # answer 값 업데이트
        else:  # 값을 증가시켜야 한다.
            left = mid + 1

    return answer
"""

N, M = map(int, input().split())
tasks = list(map(int, input().split()))

print(solution(N, M, tasks))
