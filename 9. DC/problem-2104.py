import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, histogram: List):
    def findMaximum(start, end):
        if end == start:
            return histogram[start] * histogram[start]
        mid = (start + end) // 2

        local_max = max(findMaximum(start, mid), findMaximum(mid + 1, end))
        left, right = mid, mid + 1
        _sum = histogram[left] + histogram[right]
        _min = min(histogram[left], histogram[right])
        local_max = max(local_max, _min * _sum)
        while left > start or right < end:

            if right < end and (
                left == start or histogram[left - 1] < histogram[right + 1]
            ):
                right += 1
                _sum += histogram[right]
                _min = min(_min, histogram[right])
            else:
                left -= 1
                _sum += histogram[left]
                _min = min(_min, histogram[left])

            local_max = local_max = max(local_max, _min * _sum)

        return local_max

    return findMaximum(0, N - 1)


N = int(input())
histogram = list(map(int, input().split()))

print(solution(N, histogram))
