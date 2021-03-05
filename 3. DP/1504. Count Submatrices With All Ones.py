from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]):
        row, cal = len(mat), len(mat[0])
        cache = [[0 for _ in range(cal)] for _ in range(row)]
        for r in range(row):
            for c in range(cal):
                if c == 0:
                    cache[r][c] = mat[r][c]
                else:
                    if mat[r][c] == 1:
                        cache[r][c] = cache[r][c - 1] + 1

        counter = 0
        for r in range(row):
            for c in range(cal):
                local_minimum = cache[r][c]
                for ir in range(r, -1, -1):
                    local_minimum = min(local_minimum, cache[ir][c])
                    counter += local_minimum
                    if local_minimum == 0:
                        break
        return counter


s = Solution()
i = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
o = s.numSubmat(i)
print(o)