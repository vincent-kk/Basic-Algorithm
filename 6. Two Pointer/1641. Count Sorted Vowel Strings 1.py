from typing import List
def initzero(r, c): return [[0]*c for _ in range(r)]


class Solution:
    def countVowelStrings(self, n: int):
        answer: List[List[int]] = initzero(n, 5)
        answer[0] = [1, 1, 1, 1, 1]

        for row in range(1, n):
            for column in range(5):
                answer[row][column] += answer[row-1][column]
                if column > 0:
                    answer[row][column] += answer[row][column-1]
        return sum(answer[n-1])


s = Solution()

print(s.countVowelStrings(2))
