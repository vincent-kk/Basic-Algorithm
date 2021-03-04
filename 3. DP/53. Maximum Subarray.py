from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]):
        prev_max = nums[0]
        global_max = nums[0]

        for num in nums[1:]:
            local_max = num if (prev_max + num < num) else prev_max + num
            global_max = local_max if (local_max > global_max) else global_max
            prev_max = local_max
        return global_max


s = Solution()
i = [-1]
o = s.maxSubArray(i)
print(o)