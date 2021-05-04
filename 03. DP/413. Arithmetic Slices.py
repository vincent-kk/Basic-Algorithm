from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]):
        def calcArithemtic(l: int):
            if l < 3:
                return 0
            return (l - 1) * (l - 2) // 2

        size = len(nums)
        total = 0
        pivot = 0
        length = 1
        step = 0
        while pivot < size - 1:
            if nums[pivot] + step == nums[pivot + 1]:
                length += 1
                pivot += 1
            else:
                if length >= 3:
                    total += calcArithemtic(length)
                length = 1
                step = nums[pivot + 1] - nums[pivot]

        if length >= 3:
            total += calcArithemtic(length)
        return total


if __name__ == "__main__":
    s = Solution()
    nums = [1]
    o = s.numberOfArithmeticSlices(nums)
    print(o)