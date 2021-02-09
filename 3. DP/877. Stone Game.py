from typing import List


class Solution:
    def stoneGame(self, piles: List[int]):

        mat = [[-1]*len(piles) for _ in range(len(piles))]

        def dp(i, j, player):
            if i == j:
                if player % 2 == 0:
                    return piles[i]
                else:
                    return 0

            if i < 0 or i >= len(piles) or j < 0 or j >= len(piles) or i > j:
                return 0

            if mat[i][j] != -1:
                return mat[i][j]

            first = piles[i]+dp(i+1, j, player+1)
            second = piles[j]+dp(i, j-1, player+1)
            mat[i][j] = max(first, second)
            return mat[i][j]

        return dp(0, len(piles)-1, 0) > sum(piles)//2


s = Solution()
i = [5, 3, 4, 5]
o = s.stoneGame(i)

print(o)
