from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]):
        length = len(cost)
        cache = [-1] * length

        def findMinimum(index):
            if index >= length:
                return 0
            if cache[index] > 0:
                return cache[index]
            cache[index] = cost[index] + min(
                findMinimum(index + 1), findMinimum(index + 2)
            )
            return cache[index]

        return min(findMinimum(0), findMinimum(1))


s = Solution()
i = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
o = s.minCostClimbingStairs(i)
print(o)