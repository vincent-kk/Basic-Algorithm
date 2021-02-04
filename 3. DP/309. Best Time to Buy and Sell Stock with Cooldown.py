from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]):
        length = len(prices) - 1

        @lru_cache(maxsize=None)
        def getMaxProfit(end):
            if end < 0:
                return 0
            max_profit = getMaxProfit(end-1)
            for i in range(1, end+1):
                start = end-i
                this_profit = prices[end] - prices[start]
                if this_profit < 0:
                    continue
                prev_profit = getMaxProfit(start-2)
                max_profit = max(max_profit, this_profit+prev_profit)
            return max_profit

        return getMaxProfit(length)


s = Solution()
i = [1, 4, 2]
o = s.maxProfit(i)

print(o)
