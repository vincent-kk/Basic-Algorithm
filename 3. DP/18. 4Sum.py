from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int):
        length = len(nums)
        sorted_nums = sorted(nums)
        result = []

        for i in range(length - 1, 1, -1):
            for j in range(i - 1):
                p1, p2, p3, p4 = j, j + 1, i - 1, i
                while p2 < p3:
                    instruction = (
                        sorted_nums[p1]
                        + sorted_nums[p2]
                        + sorted_nums[p3]
                        + sorted_nums[p4]
                    )
                    if instruction < target:
                        p2 += 1
                    elif instruction > target:
                        p3 -= 1
                    else:
                        temp = [
                            sorted_nums[p1],
                            sorted_nums[p2],
                            sorted_nums[p3],
                            sorted_nums[p4],
                        ]
                        if temp not in result:
                            result.append(temp)
                        p2 += 1
        return result


s = Solution()
i1 = [1, 0, -1, 0, -2, 2]
i2 = 0
o = s.fourSum(i1, i2)
print(o)
