from typing import List


class Solution:
    def threeSum(self, nums: List[int]):  # -> List[List[int]]:
        size = len(nums)
        dp = {}
        result = []
        for i in range(size):
            for j in range(i):
                if -(nums[i]+nums[j]) in dp:
                    dp[-(nums[i]+nums[j])].append((i, j))
                else:
                    dp[-(nums[i]+nums[j])] = [(i, j)]

        for i in range(size):
            if nums[i] in dp:
                elements = dp[nums[i]]
                for temp in elements:
                    if i == temp[0] or i == temp[1]:
                        continue
                    answer = [nums[i], nums[temp[0]], nums[temp[1]]]
                    answer.sort()
                    if answer not in result:
                        result.append(answer)

        return result


s = Solution()
i = [3, 0, -2, -1, 1, 2]

o = s.threeSum(i)

print(o)
