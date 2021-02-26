import sys
from functools import cache
from typing import List

input = sys.stdin.readline


def solution(N: int, histogram: List):
    def findMaximum(start, end):
        if end - start == 1:
            return histogram[start] * histogram[start]
        mid = (start + end) // 2
        local_max = max(findMaximum(start, mid), findMaximum(mid, end))
        left, right = mid - 1, mid + 1

        while right - left < end - start:

            if left - 1 < start or right + 1 > end:
                break

            left_height = min(histogram[left - 1 : right])
            left_width = sum(histogram[left - 1 : right])

            right_height = min(histogram[left : right + 1])
            right_width = sum(histogram[left : right + 1])

            inter_max = max(left_height * left_width, right_height * right_width)

            local_max = max(local_max, inter_max)
            left -= 1
            right += 1
        return local_max

    return findMaximum(0, N)


N = int(input())
histogram = list(map(int, input().split()))

print(solution(N, histogram))
