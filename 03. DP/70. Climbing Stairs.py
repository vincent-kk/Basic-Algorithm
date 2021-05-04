from functools import cache
from collections import defaultdict


class Solution:
    # Top-Down
    # def climbStairs(self, n: int):
    #     @cache
    #     def makeSteps(x: int):
    #         if x == 0:
    #             return 0
    #         if x == 1:
    #             return 1
    #         if x == 2:
    #             return 2
    #         return makeSteps(x - 1) + makeSteps(x - 2)

    #     return makeSteps(n)

    # Buttom-Up
    def climbStairs(self, n: int):
        cache = defaultdict(int)
        cache[1] = 1
        cache[2] = 2

        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]


if __name__ == "__main__":
    s = Solution()
    i = 3
    o = s.climbStairs(i)
    print(o)
