import sys
from typing import List, Tuple

input = sys.stdin.readline


def solution(N: int, data: List[Tuple[int]]):
    sorted_data = sorted(data, key=lambda x: -x[1])
    center = sorted_data[0]
    left = right = center[0]
    result = center[1]
    for row in sorted_data[1:]:
        if row[0] > left:
            result += abs(row[0] - left) * row[1]
            left = row[0]
        if row[0] < right:
            result += abs(row[0] - right) * row[1]
            right = row[0]

    return result


if __name__ == "__main__":
    N = int(input())
    data = [tuple(map(int, input().split())) for _ in range(N)]
    print(solution(N, data))
