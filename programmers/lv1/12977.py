from typing import List
from itertools import combinations


def isPrimeNumber(n: int):
    i = 2
    while i * i < n + 1:
        if n % i == 0:
            return False
        i += 1
    return True


# def solution(nums: List[int]):
#     answer = 0
#     l = len(nums)
#     for i in range(l - 2):
#         for j in range(i + 1, l - 1):
#             for k in range(j + 1, l):
#                 if isPrimeNumber(nums[i] + nums[j] + nums[k]):
#                     answer += 1
#     return answer


def solution(nums: List[int]):
    answer = 0
    for n in combinations(nums, 3):
        if isPrimeNumber(sum(n)):
            answer += 1
    return answer


if __name__ == "__main__":
    i = [1, 2, 7, 6, 4]
    print(solution(i))
