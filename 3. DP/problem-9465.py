import sys
from typing import List

input = sys.stdin.readline


def takeStiker(input_array: List[List[int]]):
    upper_max = input_array[0][0]
    under_max = input_array[0][1]
    skip_max = 0
    for up, down in input_array[1:]:
        upper_max, under_max, skip_max = (
            max(under_max + up, skip_max + up),
            max(upper_max + down, skip_max + down),
            max(upper_max, under_max),
        )

    return max(upper_max, under_max, skip_max)


N = int(input())
for _ in range(N):
    L = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    input_array = []
    for i in range(L):
        input_array.append((line1[i], line2[i]))
    print(takeStiker(input_array))
