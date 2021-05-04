from typing import List
from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]):
        row_size = len(matrix)
        col_size = len(matrix[0])

        @cache
        def findPath(row, col):
            if row == row_size:
                return 0

            global_minimum = float("inf")
            for i in range(-1, 2):
                next_col = 0 if (col + i < 0) else min(col_size - 1, col + i)
                local_minimum = matrix[row][col] + findPath(row + 1, next_col)
                global_minimum = min(global_minimum, local_minimum)
            return global_minimum

        result = float("inf")
        for c in range(col_size):
            result = min(result, findPath(0, c))
        return result


s = Solution()
i = [[-48]]
o = s.minFallingPathSum(i)
print(o)
