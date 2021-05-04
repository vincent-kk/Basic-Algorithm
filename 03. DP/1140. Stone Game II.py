from typing import List
from functools import lru_cache
def fmax(x, y): return x if x > y else y


class Solution:
    def stoneGameII(self, piles: List[int]):
        length = len(piles)

        @lru_cache(maxsize=None)
        def optimalTurn(M: int, start: int):
            if start >= length:
                return 0
            if length - start < 2*M+1:
                return sum(piles[start:])

            score_max = 0
            total_sum = sum(piles[start:])
            for x in range(1, 2*M+1):
                opponent_score = optimalTurn(fmax(x, M), start+x)
                score_max = fmax(score_max, total_sum - opponent_score)
            return score_max

        return optimalTurn(1, 0)


s = Solution()
i = [2, 7, 9, 4, 4]
o = s.stoneGameII(i)

print(o)
