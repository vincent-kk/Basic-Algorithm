import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, histogram: List):
    def findMaxArea(start, end):
        if start == end:
            return histogram[start]

        mid = (start + end) // 2
        local_max = max(findMaxArea(start, mid), findMaxArea(mid + 1, end))

        left, right = mid, mid + 1
        _min = min(histogram[left], histogram[right])
        _length = 2
        local_max = max(local_max, _min * _length)

        while left > start or right < end:
            if left > start and (
                right == end or histogram[left - 1] > histogram[right + 1]
            ):
                left -= 1
                _min = min(_min, histogram[left])
            else:
                right += 1
                _min = min(_min, histogram[right])
            _length += 1
            local_max = max(local_max, _min * _length)
        return local_max

    return findMaxArea(0, N - 1)


N = int(input())
histogram = []
for _ in range(N):
    value = int(input())
    histogram.append(value)

print(solution(N, histogram))
