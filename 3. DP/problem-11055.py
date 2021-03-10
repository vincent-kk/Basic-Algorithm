import sys
from typing import List

input = sys.stdin.readline


# def solution(N: int, nums: List[int]):
#     __cache__ = [[0, 0] for _ in range(N)]
#     __cache__[0] = [nums[0], nums[0]]

#     for i in range(1, N):
#         __prev__ = 0
#         for j in range(i - 1, -1, -1):
#             if nums[j] < nums[i]:
#                 __prev__ = max(__prev__, __cache__[j][0])
#         __cache__[i][0] = __prev__ + nums[i]
#         __cache__[i][1] = max(__cache__[i - 1][1], __cache__[i][0])

#     return __cache__[N - 1][1]


def solution(N: int, nums: List[int]):
    __cache__ = [0] * 1001
    for num in nums:
        __cache__[num] = max(__cache__[:num]) + num
    return max(__cache__)


N = int(input())
nums = list(map(int, input().split()))
__cache__ = [0] * 1001
for num in nums:
    __cache__[num] = max(__cache__[:num]) + num
print(max(__cache__))
