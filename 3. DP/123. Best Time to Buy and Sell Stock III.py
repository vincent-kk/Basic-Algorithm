from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):  # -> int:
        length = len(prices)
        differential = [0]*length
        diff_sum = [0]*length
        for i in range(1, length):
            differential[i] = prices[i]-prices[i-1]
            diff_sum[i] = diff_sum[i-1] + differential[i]

        def findMaximumSubArray(start, end):
            subarray_start = start
            subarray_end = end
            subarray_max = 0
            # for i in range(start, end):

        return differential, diff_sum


s = Solution()

i = [7, 1, 5, 3, 6, 4]

o = s.maxProfit(i)

print(o)
