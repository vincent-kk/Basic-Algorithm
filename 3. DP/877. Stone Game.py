from typing import List


class Solution:
    def stoneGame(self, piles: List[int]):
        length = len(piles)
        memo = [[-1] * length for _ in range(length)]

        def dp(start, end, player):
            if start == end:
                if player % 2 == 0:
                    return piles[start]
                else:
                    return 0

            if start < 0 or end >= length or start > end:
                return 0

            if memo[start][end] != -1:
                return memo[start][end]

            first = piles[start] + dp(start + 1, end, player + 1)
            second = piles[end] + dp(start, end - 1, player + 1)
            memo[start][end] = max(first, second)
            return memo[start][end]

        return dp(0, length - 1, 0) > sum(piles) // 2


s = Solution()
i = [5, 6, 4, 5, 1]
o = s.stoneGame(i)

print(o)
