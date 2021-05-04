from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int):

        length = len(nums) - 1
        sorted_nums = sorted(nums)
        closest = 0
        diff = float("inf")
        for i in range(length):
            start = i
            mid, end = i + 1, length

            while mid < end:
                instruction = sorted_nums[start] + sorted_nums[mid] + sorted_nums[end]
                local_diff = abs(instruction - target)
                if diff > local_diff:
                    closest = instruction
                    diff = local_diff
                if instruction < target:
                    mid += 1
                else:
                    end -= 1
        return closest


s = Solution()
i1 = [0, 2, 1, -3]
i2 = 1
o = s.threeSumClosest(i1, i2)
print(o)
