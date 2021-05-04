from typing import List


class Solution:
    def threeSum(self, nums: List[int]):  # -> List[List[int]]:
        length = len(nums)

        result = set()
        out = []
        sorted_nums = sorted(nums)

        for i in range(length - 1, -1, -1):
            last = sorted_nums[i]
            start, end = 0, i - 1

            while end > start:
                indicator = last + sorted_nums[start] + sorted_nums[end]
                if indicator < 0:
                    start += 1
                elif indicator > 0:
                    end -= 1
                else:
                    if (last, sorted_nums[start], sorted_nums[end]) not in result:
                        out.append([last, sorted_nums[start], sorted_nums[end]])
                    result.add((last, sorted_nums[start], sorted_nums[end]))
                    start += 1
        return out
        # i, j = 0, length - 1

        # while i < length and j > 0:

        #     for k in range(i + 1, j):
        #         if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
        #             temp = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
        #             if temp not in result:
        #                 result.append(temp)

        #     indicator = sorted_nums[i] + sorted_nums[j]
        #     if indicator < 0:
        #         i += 1
        #     elif indicator > 0:
        #         j -= 1


s = Solution()
i = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# print(sorted(i))
#   [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
o = s.threeSum(i)

print(o)
