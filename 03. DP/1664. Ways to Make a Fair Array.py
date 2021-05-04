from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]):
        length = len(nums)

        # def checkFair(array):
        #     print(sum(array[0::2]), sum(array[1::2]))
        #     return sum(array[0::2]) == sum(array[1::2])

        # for i in range(length):
        #     if checkFair(nums[:i] + nums[i + 1 :]):
        #         result += 1

        odd = sum(nums[1::2])
        even = sum(nums[2::2])
        result = 1 * (odd == even)

        for pivot in range(1, length):
            if pivot % 2 == 0:
                even += nums[pivot - 1] - nums[pivot]
            else:
                odd += nums[pivot - 1] - nums[pivot]
            result += odd == even
        return result


s = Solution()
i = [2, 1, 6, 4]
o = s.waysToMakeFair(i)
print(o)