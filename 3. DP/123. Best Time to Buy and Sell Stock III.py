from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    cost: int = float("inf")
    profit: int = 0


class Solution:
    def maxProfit(self, prices: List[int]):

        first, second = Transaction(), Transaction()

        for price in prices:
            first.cost = min(first.cost, price)
            first.profit = max(first.profit, price - first.cost)
            second.cost = min(second.cost, price - first.profit)
            second.profit = max(second.profit, price - second.cost)

        return second.profit


s = Solution()
i = [3, 3, 5, 0, 0, 3, 1, 4]
o = s.maxProfit(i)
print(o)
