import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, tasks: List[int]):
    high = sum(tasks)
    low = high // M

    while high > low + 1:
        pivot = (low + high) // 2

        free = pivot
        disks = 1
        for task in tasks:
            free -= task
            if free < 0:
                disks += 1
                free = pivot - task
            if free == 0:
                disks += 1
                free = pivot

        if disks > M:
            low = pivot
        else:
            high = pivot

    return (low + high) // 2


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
