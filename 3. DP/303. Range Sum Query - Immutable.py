from typing import List
from collections import defaultdict


class NumArray:
    def __init__(self, nums: List[int]):
        self.cache = defaultdict(int)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.cache[i] = total

    def sumRange(self, i: int, j: int):
        if i == 0:
            return self.cache[j]
        else:
            return self.cache[j] - self.cache[i - 1]


s = NumArray([-2, 0, 3, -5, 2, -1])

print(s.sumRange(0, 2))
print(s.sumRange(2, 5))
print(s.sumRange(0, 5))
