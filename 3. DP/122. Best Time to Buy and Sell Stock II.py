from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):  # -> int:
        size = len(prices)
        result = [0]*(size-1)
        for i in range(size-1):
            result[i] = max(prices[i+1]-prices[i], 0)
        return sum(result)


s = Solution()

i = [7, 1, 5, 3, 6, 4]

o = s.maxProfit(i)

print(o)
