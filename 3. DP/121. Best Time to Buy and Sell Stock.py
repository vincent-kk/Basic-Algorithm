from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        size = len(prices)
        answer = 0
        dp = [0]*size
        dp[0] = prices[0]
        for i in range(1, size):
            if prices[i] < dp[i-1]:
                dp[i] = prices[i]
            else:
                dp[i] = dp[i-1]
                answer = max(answer, prices[i] - dp[i])
        return answer


s = Solution()

i = [7, 1, 5, 3, 6, 4]

o = s.maxProfit(i)

print(o)
