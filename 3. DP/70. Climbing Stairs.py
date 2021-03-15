from functools import cache


class Solution:
    def climbStairs(self, n: int):
        @cache
        def makeSteps(x: int):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 2
            return makeSteps(x - 1) + makeSteps(x - 2)

        return makeSteps(n)


if __name__ == "__main__":
    s = Solution()
    i = 3
    o = s.climbStairs(i)
    print(o)
